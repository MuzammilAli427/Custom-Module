from server.odoo import models,osv,fields
class your_class(models.Model):
    _name = 'first.hospital'
    _description = 'Hospital discription'

    name = fields.Char(string="patient_name")
    age = fields.Integer(string="patient_age")
    height = fields.Integer(string="Patient Height")
    notes =fields.Text(string="Notes")
    # notes1 =fields.Text(string="Notes1")
    image =fields.Binary(string="patient_image")
    # phone =fields.Text(string="phone number")


your_class()

#     _fields ={
#     "product1" : fields.Char('Name'),
#     "product2" :  fields.Integer('Age'),
#     "product3" :  fields.Text('notes'),
#     "product4" :  fields.Binary("image"),
# }


