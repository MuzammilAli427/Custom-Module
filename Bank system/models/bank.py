from odoo import models, fields


class Bank(models.Model):
    _name = 'Bank.system'

    a_id = fields.Integer(string="Enter The ID")
    fullname = fields.Char(string="Owner Name")
    account_num = fields.Integer(string="Account Number")
    date_action = fields.Datetime(string='Date current action', required=False, readonly=False, select=True)
    amount = fields.Integer(string="Enter the Amount")



