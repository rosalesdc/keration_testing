# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_laboratorios(models.Model):
    _name = 'add_fields_rapaport_model.piedra_laboratorios'

    name = fields.Char(
                       string="Laboratorio",
                       required=True,
                       )