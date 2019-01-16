# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_claridades(models.Model):
    _name = 'add_fields_rapaport_model.piedra_claridades'

    name = fields.Char(
                       string="Claridad",
                       required=True,
                       )