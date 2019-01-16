# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_formas(models.Model):
    _name = 'add_fields_rapaport_model.piedra_formas'

    name = fields.Char(
                       string="Formas",
                       required=True,
                       )