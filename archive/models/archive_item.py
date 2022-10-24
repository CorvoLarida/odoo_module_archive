# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ArchiveItem(models.Model):
    _name = 'archive.item'
    _description = 'Archive Item'
    _order = 'date_creation desc, name'
    attachment = fields.Binary(string='Attached File', required=True)
    attachment_name = fields.Char(string='File Name')
    tags = fields.Many2many('archive.tag', string='Tags')
    name = fields.Char(string='Entry', required=True)
    date_release = fields.Date(string='Release Date', default= fields.Date.today(), required=True)
    date_creation = fields.Date(string='Item Creation Date', default= fields.Date.today(), readonly=True)
    date_updated = fields.Datetime(string='Last Updated', default= fields.Datetime.now(), readonly=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
    description = fields.Html(string='Description')
    _sql_constraints = [('name_uniq', 'UNIQUE (name)','Entry field must be unique.')]
    
    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
                raise models.ValidationError('Release date must be in the past.')
    
    
    @api.model
    def create(self, vals):
        init = super(ArchiveItem,self).create(vals)
        init.date_updated = fields.Datetime.now()        
        return init     
    
    def write(self, vals):
        if self.date_updated < fields.Datetime.now():
            vals['date_updated'] = fields.Datetime.now()
        return super(ArchiveItem,self).write(vals)

   
    
   


    
        
            

    
    



    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
