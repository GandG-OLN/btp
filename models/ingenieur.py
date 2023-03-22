from odoo import models, fields

class BtpIngenieur(models.Model):
    _name = 'btp.ingenieur'

    nom = fields.Char('Nom')
    prenom = fields.Char('Prenom')


    