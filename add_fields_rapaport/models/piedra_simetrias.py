# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_simetrias(models.Model):
    _name = 'add_fields_rapaport_model.piedra_simetrias'

    name = fields.Char(
                       string="Simetría",
                       required=True,
                       )
