from odoo import models,fields,api

class Student(models.Model):
    _name='college.student'

    first_name=fields.Char(string='First Name')
    last_name=fields.Char(string='Last Name')
    dob=fields.Date(string='DOB')
    seat_no=fields.Integer(string='Sear Number')
