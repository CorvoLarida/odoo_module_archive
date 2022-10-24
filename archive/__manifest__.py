# -*- coding: utf-8 -*-
{
    'name': "Archive",
    'summary': """Manage archive files.""",
    'description': """
        Simple module for storing files in the archive.
    """,
    'author': "Corvo Larida",
    'website': "https://github.com/CorvoLarida/odoo_module_archive",
    'category': 'Knowledge Management',
    'version': '13.0.1.0.0',
    'license': 'LGPL-3',
    'sequence': -50,
    'application':True,
    
    'depends': ['base','mail'],
    
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/archive_item.xml',
    ],
   
    'demo': [
        'demo/demo.xml',
    ],
    
}