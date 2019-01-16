# - * - coding: utf-8 - * -

from odoo import api
from odoo import fields
from odoo import models

class add_rapaport_cost(models.Model):
    _inherit = 'account.invoice'

    #x_rapaport_cost = fields.Float(string='Costo R', digits=(4, 2),default=1)
    #x_n_rapaport=fields.Float(string='numero R', default='-1')
    
    x_n_pedimento=fields.Char(string='No. de Pedimento')
    #numero_rapaport
    
#    https://www.odoo.com/es_ES/forum/ayuda-1/question/in-what-cases-we-should-use-related-fields-101666