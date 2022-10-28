# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ArchiveStatus(models.Model):
    _inherit = 'archive.item'
        
    state = fields.Selection([('draft','Draft'),('editing','In Editing'),('done','Done')], string='Status', default="draft") 