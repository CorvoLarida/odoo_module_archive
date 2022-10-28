# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ArchiveTag(models.Model):
    _name = 'archive.tag'
    _description = 'Tag for grouping items.'
    
    name = fields.Char(string='Tag')
    _sql_constraints = [('name_uniq', 'UNIQUE (name)','Tags must be unique.')]
    