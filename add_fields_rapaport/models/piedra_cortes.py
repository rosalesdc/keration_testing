# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_cortes(models.Model):
    _name = 'add_fields_rapaport_model.piedra_cortes'

    name = fields.Char(
                       string="Corte",
                       required=True,
                       )