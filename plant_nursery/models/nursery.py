from odoo import models, fields


class plants(models.Model):
    _name = 'plant.nursery'

    name = fields.Char(string="Plant Name")
    price = fields.Float()
