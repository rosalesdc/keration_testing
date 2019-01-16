# - * - coding: utf-8 - * -

from odoo import api
from odoo import fields
from odoo import models

class porcentaje_rapaport(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('price_unit')
    def _compute_costo_quilate_usd(self):
        for record in self:
            variable=self.x_n_rapaport
            if variable!=0:
                self.porcentaje_rap = (self.price_unit/(self.x_n_rapaport *100) * 100) - (100)
              
    porcentaje_rap = fields.Float(string='Rap %', digits=(4, 2), default=0.0,readonly=True)