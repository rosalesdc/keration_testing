# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions, _

class Wizard_Keration(models.TransientModel): 
	_name='wizard_keration'
	

	def _default_category(self):
		print('RASTREANDO',str(self.env['product.product'].browse(self._context.get('categ_id'))))
		return self.env['product.category'].browse(self._context.get('product.category'))


	product_ids=fields.Many2many('product.product',string='Categorias', default=_default_category)

	def update_categs(self):
		for record in self.product_ids:
			print('PROBANDO',str(record.categ_id))
			print('SEGUNDA PRUEBA',str(record.categ_id.id))
			if record.categ_id.id == 1:
				print('TERCERA PRUEBA',str(record.categ_id.id))
				record.write({'categ_id':34})
				
