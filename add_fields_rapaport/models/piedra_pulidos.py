# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class piedra_pulidos(models.Model):
    _name = 'add_fields_rapaport_model.piedra_pulidos'

    name = fields.Char(
                       string="Pulido",
                       required=True,
                       )
