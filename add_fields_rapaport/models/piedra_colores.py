# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_colores(models.Model):
    _name = 'add_fields_rapaport_model.piedra_colores'

    name = fields.Char(
                       string="Color",
                       required=True,
                       )