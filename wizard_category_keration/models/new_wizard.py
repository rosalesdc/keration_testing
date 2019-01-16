# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions, _

class Wizard_Deletion(models.TransientModel): 
	_name='wizard_deletion'	
	
	def _default_rfq(self):
		return self.env['purchase.order'].browse(self._context.get('active_ids'))


	purchase_ids=fields.Many2many('purchase.order',string='Compras', default=_default_rfq)

	def delete_rfqs(self):
		for record in self.purchase_ids:
			if record.state == 'draft':
				print('PURCHASE IDS',str(record.id))
				record.write({'state':'cancel'})
				record.unlink()
