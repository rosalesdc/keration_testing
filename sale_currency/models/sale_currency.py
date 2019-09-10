# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class SaleCurrency(models.Model):
	_inherit = 'sale.order'

	x_tipo_cambio = fields.Float(string='Tipo de cambio')

	@api.multi
	def _prepare_invoice(self):
		"""
		Prepare the dict of values to create the new invoice for a sales order. This method may be
		overridden to implement custom invoice generation (making sure to call super() to establish
		a clean extension chain).
		"""
		self.ensure_one()
		journal_id = self.env['account.invoice'].default_get(['journal_id'])['journal_id']
		if not journal_id:
			raise UserError(_('Please define an accounting sales journal for this company.'))
		invoice_vals = {
			'name': self.client_order_ref or '',
			'origin': self.name,
			'type': 'out_invoice',
			'account_id': self.partner_invoice_id.property_account_receivable_id.id,
			'partner_id': self.partner_invoice_id.id,
			'partner_shipping_id': self.partner_shipping_id.id,
			'journal_id': journal_id,
			'currency_id': self.pricelist_id.currency_id.id,
			'comment': self.note,
			'payment_term_id': self.payment_term_id.id,
			'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
			'company_id': self.company_id.id,
			'user_id': self.user_id and self.user_id.id,
			'team_id': self.team_id.id,
			'transaction_ids': [(6, 0, self.transaction_ids.ids)],
			'x_tipo_cambio':self.x_tipo_cambio
		}
		return invoice_vals

class SaleLineCurrencya(models.Model):
	_inherit = 'sale.order.line'

	x_tipo_cambio = fields.Float(related="order_id.x_tipo_cambio",string='Tipo de cambio',readonly=True)

	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'x_tipo_cambio')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:
			if line.x_tipo_cambio != 0:
				line.price_unit = line.product_id.lst_price * line.x_tipo_cambio
				price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
			else:
				price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
			line.update({
				'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})

	@api.multi
	def _prepare_invoice_line(self, qty):
		"""
		Prepare the dict of values to create the new invoice line for a sales order line.
		:param qty: float quantity to invoice
		"""
		self.ensure_one()
		res = {}
		account = self.product_id.property_account_income_id or self.product_id.categ_id.property_account_income_categ_id

		if not account and self.product_id:
			raise UserError(_('Please define income account for this product: "%s" (id:%d) - or for its category: "%s".') %
				(self.product_id.name, self.product_id.id, self.product_id.categ_id.name))

		fpos = self.order_id.fiscal_position_id or self.order_id.partner_id.property_account_position_id
		if fpos and account:
			account = fpos.map_account(account)

		res = {
			'name': self.name,
			'sequence': self.sequence,
			'origin': self.order_id.name,
			'account_id': account.id,
			'price_unit': self.price_unit,
			'quantity': qty,
			'discount': self.discount,
			'uom_id': self.product_uom.id,
			'product_id': self.product_id.id or False,
			'invoice_line_tax_ids': [(6, 0, self.tax_id.ids)],
			'account_analytic_id': self.order_id.analytic_account_id.id,
			'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
			'display_type': self.display_type,
			'x_tipo_cambio':self.x_tipo_cambio
		}
		return res

class AccountInvoiceCurrency(models.Model):
	_inherit = 'account.invoice'

	x_tipo_cambio = fields.Float(string='Tipo de cambio')

class AccountInvoiceLineCurrency(models.Model):
	_inherit = 'account.invoice.line'

	x_tipo_cambio = fields.Float(related="invoice_id.x_tipo_cambio",string='Tipo de cambio',readonly=True)

	@api.one
	@api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
		'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
		'invoice_id.date_invoice', 'invoice_id.date','x_tipo_cambio')
	def _compute_price(self):
		currency = self.invoice_id and self.invoice_id.currency_id or None
		if self.x_tipo_cambio != 0:
			self.price_unit = self.product_id.lst_price * self.x_tipo_cambio
			price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
		else:
			price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
		taxes = False
		if self.invoice_line_tax_ids:
			taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id, partner=self.invoice_id.partner_id)
		self.price_subtotal = price_subtotal_signed = taxes['total_excluded'] if taxes else self.quantity * price
		self.price_total = taxes['total_included'] if taxes else self.price_subtotal
		if self.invoice_id.currency_id and self.invoice_id.currency_id != self.invoice_id.company_id.currency_id:
			currency = self.invoice_id.currency_id
			date = self.invoice_id._get_currency_rate_date()
			price_subtotal_signed = currency._convert(price_subtotal_signed, self.invoice_id.company_id.currency_id, self.company_id or self.env.user.company_id, date or fields.Date.today())
		sign = self.invoice_id.type in ['in_refund', 'out_refund'] and -1 or 1
		self.price_subtotal_signed = price_subtotal_signed * sign