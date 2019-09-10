# -*- coding: utf-8 -*-

from odoo import _,api,exceptions,fields,models

class add_fields_rapaport_model(models.Model):
	_inherit = 'product.template'
	numero_rapaport = fields.Integer('Rap List usd/ct', store=True)
	descuento_rapaport = fields.Float('Rap Cost %', digits=(9, 2), store=True)
	costo_quilate_usd = fields.Float('Cost usd/ct', digits=(9, 2), compute='_compute_costo_quilate_usd')
	costo_total = fields.Float('Total Cost', digits=(9, 2), compute='_compute_costo_total')
	list_price_min = fields.Float(string='Precio de venta (min)')
	price_sale = fields.Float(string='Price sale')
	rap_sale = fields.Float('Rap Sale %',compute="_compute_rap_sale")
	total_sale = fields.Float('Total sale',compute="_compute_rap_sale")
	profit_total = fields.Float(string='Profit margin',compute="_compute_rap_sale")
	lote = fields.Boolean(string='Es lote',default=False)

	@api.depends('numero_rapaport','price_sale','costo_total','quilate','total_sale')
	def _compute_rap_sale(self):
		rap_sale = 0.0
		total_sale = 0.0
		profit_total = 0.0
		for record in self:
			if record.numero_rapaport != 0:
				rap_sale += (((record.price_sale / record.numero_rapaport) * 100.0) -100.0)
			total_sale += (record.price_sale*record.quilate)
			profit_total += (total_sale-record.costo_total)
		self.update({'rap_sale':rap_sale,'total_sale':total_sale,'profit_total':profit_total,'list_price':record.price_sale})

	
	#campos joyeria
	joyeria = fields.Boolean(string='Joyeria',default=False)
	metal = fields.Selection([('oro','Oro'),('plata','Plata'),('platinium','Platinium')],string="Metal")
	#kilate = fields.Selection([('10_kt','10 KT'), ('14_kt','14 KT'), ('18_kt','18 KT')],string='Kt')
	kt_diez = fields.Char(string='10 KT, WT')
	kt_catorce = fields.Char(string='14 KT, WT')
	kt_dieciocho = fields.Char(string='18 KT, WT')
	design = fields.Char(string='Design')
	color = fields.Selection([('white','White'),('rose','Rose'),('yellow','Yellow')],string='Color')
	gold_weight = fields.Float('Gold Weight')
	diamond_qa = fields.Char('Diamond Quality')
	num_diamond = fields.Integer('N° Diamond')
	diamond_ct = fields.Float('Diamond ct.')
	stone_type_id = fields.Many2one('product.stone.type','Stone Type')
	num_stone = fields.Integer('N° of Stone')
	stone_weight = fields.Float('Stone Weight')
	gem_cet = fields.Float('Gem ct.')
	num_gem = fields.Integer('N° of Gem')

	#campos diamante
	diamante = fields.Boolean(string='Diamante',default=False)
	size = fields.Float(string='Size mm / ct.')
	sieve = fields.Char(string='Sieve')
	quilate = fields.Float(string='Quilate', digits=(4, 2), default=0.0)
	balance_quilate = fields.Float(string='Original Unit / Balance ct.', digits=(4, 2), default=0.0)
	medida = fields.Char(string='Medida')
	lote = fields.Boolean()
	numero_certificado = fields.Char(string='Certificate N°')
	table = fields.Float('Table %')
	meas = fields.Float('Meas')

	piedra_formas_id = fields.Many2one('add_fields_rapaport_model.piedra_formas',string="Shape")
	piedra_colores_id = fields.Many2one('add_fields_rapaport_model.piedra_colores',string="Color")
	piedra_laboratorios_id = fields.Many2one('add_fields_rapaport_model.piedra_laboratorios',string="Laboratory")
	piedra_cortes_id = fields.Many2one('add_fields_rapaport_model.piedra_cortes',string="Cut")
	piedra_claridades_id = fields.Many2one('add_fields_rapaport_model.piedra_claridades',string="Clarity")
	piedra_pulidos_id = fields.Many2one('add_fields_rapaport_model.piedra_pulidos',string="Polish")
	piedra_fluorescencias_id = fields.Many2one('add_fields_rapaport_model.piedra_fluorescencias',string="Fluorcence")
	piedra_simetrias_id = fields.Many2one('add_fields_rapaport_model.piedra_simetrias',string="Symmetry")


	@api.onchange('numero_rapaport', 'descuento_rapaport', 'quilate')
	def _compute_costo_quilate_usd(self):
		for record in self:
			#self.costo_quilate_usd = (100 * self.numero_rapaport) * (1-(self.descuento_rapaport / 100))
			record.costo_quilate_usd =record.numero_rapaport-(record.numero_rapaport*record.descuento_rapaport/100)
			if record.costo_quilate_usd < 0.0:
				raise exceptions.ValidationError(_("No puedes tener un costo negativo"))
			else:
				if record.costo_quilate_usd != record.costo_quilate_usd:
					record.description = "El costo por quilate recalculado es: $'{0}'".format(costo_quilate_usd)
					record.costo_quilate_usd = record.costo_quilate_usd
					return {'warning': {'title':"Advertencia", 'message': record.description}}

#          raise exceptions.ValidationError(_("El costo es igual al último registro"))

	@api.onchange('costo_quilate_usd', 'quilate','lote')
	def _compute_costo_total(self): 
		for record in self:
			if record.lote == False:
				record.costo_total = record.costo_quilate_usd * record.quilate
				if record.costo_total != record.costo_total:
					record.description = "El costo recalculado de la pieza es: $'{0}'".format(costo_total)
					record.costo_total = record.costo_total
					return {'warning': {'title':"Advertencia", 'message': record.description}}
			else:
				record.costo_total = 0.0
				record.costo_total += (record.costo_quilate_usd*record.quilate)
#        return costo_total
#      else:
#        return costo_total

class ProductProductRapaport(models.Model):
	_inherit = 'product.product'
	
	@api.onchange('numero_rapaport','price_sale','costo_total','quilate','total_sale')
	def _compute_rap_sale(self):
		rap_sale = 0.0
		total_sale = 0.0
		profit_total = 0.0
		for record in self:
			if record.numero_rapaport != 0:
				rap_sale += (((record.price_sale / record.numero_rapaport) * 100.0) -100.0)
			total_sale += (record.price_sale*record.quilate)
			profit_total += (total_sale-record.costo_total)
		self.update({'rap_sale':rap_sale,'total_sale':total_sale,'profit_total':profit_total,'lst_price':record.price_sale})

	@api.onchange('numero_rapaport', 'descuento_rapaport', 'quilate')
	def _compute_costo_quilate_usd(self):
		for record in self:
			#self.costo_quilate_usd = (100 * self.numero_rapaport) * (1-(self.descuento_rapaport / 100))
			record.costo_quilate_usd =record.numero_rapaport-(record.numero_rapaport*record.descuento_rapaport/100)
			if record.costo_quilate_usd < 0.0:
				raise exceptions.ValidationError(_("No puedes tener un costo negativo"))
			else:
				if record.costo_quilate_usd != record.costo_quilate_usd:
					record.description = "El costo por quilate recalculado es: $'{0}'".format(costo_quilate_usd)
					record.costo_quilate_usd = record.costo_quilate_usd
					return {'warning': {'title':"Advertencia", 'message': record.description}}

#          raise exceptions.ValidationError(_("El costo es igual al último registro"))

	@api.onchange('costo_quilate_usd', 'quilate','lote')
	def _compute_costo_total(self): 
		for record in self:
			if record.lote == False:
				record.costo_total = record.costo_quilate_usd * record.quilate
				if record.costo_total != record.costo_total:
					record.description = "El costo recalculado de la pieza es: $'{0}'".format(costo_total)
					record.costo_total = record.costo_total
					return {'warning': {'title':"Advertencia", 'message': record.description}}
			else:
				record.costo_total = 0.0
				record.costo_total += (record.costo_quilate_usd*record.quilate)


class ProductStoneType(models.Model):
	_name = 'product.stone.type'
	_description = 'Product Stone Type'

	name = fields.Char(string='Name')