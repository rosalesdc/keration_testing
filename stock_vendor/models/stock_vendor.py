# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError

class StockPickingVendor(models.Model):
	_inherit = 'stock.picking'

	x_vendedor = fields.Many2one('res.partner',string='Vendedor',domain=[('category_id.name', '=','Vendedor')])
	#x_set_vendor = fields.Char(string='Asignar vendedor a productos',compute="_get_vendedor")
#
	#@api.depends('x_vendedor')
	#def _get_vendedor(self):
		#lista = []
		#for record in self:
			#lista.append(record.x_vendedor.id)
		#for product in self.move_ids_without_package:
				#product.product_id.sudo().write({'x_vendedor_ids':lista})
class StockMoveVendor(models.Model):
	_inherit = 'stock.move'

	x_vendedor_id = fields.Char(string='Vendedor',compute="_compute_partner")

	@api.depends('picking_id.x_vendedor')
	def _compute_partner(self):
		for move in self:
			move.x_vendedor_id = move.picking_id.x_vendedor.name
			if move.state in ['done']:
				quants = self.env['stock.quant'].search([('in_date','=',move.date),('location_id','=',move.location_dest_id.id)])
				for quant in quants:
					quant.x_vendedor = move.picking_id.x_vendedor.id

class stockQuantPrice(models.Model):
	_inherit = 'stock.quant'

	x_vendedor = fields.Many2one('res.partner',string='Vendedor')
	inventory_valuation = fields.Float(string='Total usd/ct',compute="_compute_inventory_value")

	@api.multi
	def _compute_inventory_value(self):
		for quant in self:
			quant.inventory_valuation = quant.product_id.costo_quilate_usd * quant.quantity

	#@api.multi
	#def get_vendedor(self):
		#for record in self.product_id.x_vendedor_ids:
			#print('Vendedor',record.product_id.x_vendedor)
			#record.x_vendedor = record.picking_id.x_vendedor
			#record.x_vendedor = record.x_vendedor.name

#class ProductProductVendor(models.Model):
	#_inherit = 'product.product'
#
	#x_vendedor_ids = fields.One2many('res.partner','x_vendedor_id',string='Vendedor')
#
#class ProductVendor(models.Model):
	#_inherit = 'res.partner'
#
	#x_vendedor_id = fields.Many2one('product.product',string='Productos')