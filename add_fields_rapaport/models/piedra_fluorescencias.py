# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_fluorescencias(models.Model):
    _name = 'add_fields_rapaport_model.piedra_fluorescencias'

    name = fields.Char(
                       string="Fluorescencia",
                       required=True,
                       )

