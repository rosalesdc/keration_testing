# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models

class add_purchase_rapaport(models.Model):
    _inherit = 'purchase.order'

    numero_rapaport=fields.Integer('Costo Rapaport',store=True)
    descuento_rapaport=fields.Float('Porcentaje de descuento Rapaport',digits=(9,2),store=True)
    costo_quilate_usd=fields.Float('Costo unitario del quilate en USD ',digits=(9,2),compute='_compute_costo_quilate_usd')
    costo_total=fields.Float('Costo total de la pieza en USD',digits=(9,2),compute='_compute_costo_total')
    quilate=fields.Float(string='Quilate',digits=(4,2),default=0.0)
    balance_quilate=fields.Float(string='Balance quilate',digits=(4, 2),default=0.0)
    medida=fields.Char(string='Medida')
    lote=fields.Boolean()
    numero_certificado=fields.Char(string='Numero de certificado')

class add_purchase_rapaport_line(models.Model):
    _inherit = 'purchase.order.line'

    numero_rapaport=fields.Integer('Costo Rapaport',store=True)
    descuento_rapaport=fields.Float('Porcentaje de descuento Rapaport',digits=(9,2),store=True)
    costo_quilate_usd=fields.Float('Costo unitario del quilate en USD ',digits=(9,2),default=0.0)
    costo_total=fields.Float('Costo total de la pieza en USD',digits=(9,2),default=0.0)
    quilate=fields.Float(string='Quilate',digits=(4,2),default=0.0)
    balance_quilate=fields.Float(string='Balance quilate',digits=(4, 2),default=0.0)
    medida=fields.Char(string='Medida')
    lote=fields.Boolean()
    numero_certificado=fields.Char(string='Numero de certificado')
