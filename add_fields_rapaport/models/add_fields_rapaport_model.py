# -*- coding: utf-8 -*-

from odoo import _
from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class add_fields_rapaport_model(models.Model):
    _inherit = 'product.template'
    numero_rapaport = fields.Integer('Costo Rapaport', store=True)
    descuento_rapaport = fields.Float('Porcentaje de descuento Rapaport', digits=(9, 2), store=True)
    costo_quilate_usd = fields.Float('Costo unitario del quilate en USD ', digits=(9, 2), compute='_compute_costo_quilate_usd')
    costo_total = fields.Float('Costo total de la pieza en USD', digits=(9, 2), compute='_compute_costo_total')
    quilate = fields.Float(string='Quilate', digits=(4, 2), default=0.0)
    balance_quilate = fields.Float(string='Balance quilate', digits=(4, 2), default=0.0)
    medida = fields.Char(string='Medida')
    lote = fields.Boolean()
    numero_certificado = fields.Char(string='Numero de certificado')
    
    parsel_code = fields.Char('Parsel Serial Number', default=lambda obj:
                              obj.env['ir.sequence'].next_by_code('parsel.code'))
    _sql_constraints = [
        ('field_unique', 
         'unique(parsel_code)',
         'Secuencia incorrecta, Parsel Serial Number repetido')
        ]

    @api.onchange('numero_rapaport', 'descuento_rapaport', 'quilate')
    def _compute_costo_quilate_usd(self):
        for record in self:
            #self.costo_quilate_usd = (100 * self.numero_rapaport) * (1-(self.descuento_rapaport / 100))
            self.costo_quilate_usd =self.numero_rapaport-(self.numero_rapaport*self.descuento_rapaport/100)
            if self.costo_quilate_usd < 0.0:
                raise exceptions.ValidationError(_("No puedes tener un costo negativo"))
            else:
                if self.costo_quilate_usd != record.costo_quilate_usd:
                    record.description = "El costo por quilate recalculado es: $'{0}'".format(costo_quilate_usd)
                    record.costo_quilate_usd = self.costo_quilate_usd
                    return {'warning': {'title':"Advertencia", 'message': record.description}}

#          raise exceptions.ValidationError(_("El costo es igual al último registro"))

    @api.onchange('costo_quilate_usd', 'quilate')
    def _compute_costo_total(self): 
        for record in self:
            self.costo_total = self.costo_quilate_usd * self.quilate
            if self.costo_total != record.costo_total:
                record.description = "El costo recalculado de la pieza es: $'{0}'".format(costo_total)
                record.costo_total = self.costo_total
                return {'warning': {'title':"Advertencia", 'message': record.description}}
#        return costo_total
#      else:
#        return costo_total

    piedra_formas_id = fields.Many2one(
                                       'add_fields_rapaport_model.piedra_formas', #modelo relacionado
                                       string="Forma",
                                       required=True,
                                       )
    piedra_colores_id = fields.Many2one(
                                        'add_fields_rapaport_model.piedra_colores', #modelo relacionado
                                        string="Color",
                                        required=True,
                                        )
    piedra_laboratorios_id = fields.Many2one(
                                             'add_fields_rapaport_model.piedra_laboratorios', #modelo relacionado
                                             string="Laboratorio",
                                             required=True,
                                             )
    piedra_cortes_id = fields.Many2one(
                                       'add_fields_rapaport_model.piedra_cortes', #modelo relacionado
                                       string="Corte",
                                       required=True,
                                       )
    piedra_claridades_id = fields.Many2one(
                                           'add_fields_rapaport_model.piedra_claridades', #modelo relacionado
                                           string="Claridad",
                                           required=True,
                                           )
    piedra_pulidos_id = fields.Many2one(
                                        'add_fields_rapaport_model.piedra_pulidos', #modelo relacionado
                                        string="Pulido",
                                        required=True,
                                        )
    piedra_fluorescencias_id = fields.Many2one(
                                               'add_fields_rapaport_model.piedra_fluorescencias', #modelo relacionado
                                               string="Fluorescencia",
                                               required=True,
                                               )
    piedra_simetrias_id = fields.Many2one(
                                          'add_fields_rapaport_model.piedra_simetrias', #modelo relacionado
                                          string="Simetría",
                                          required=True,
                                          )

	
