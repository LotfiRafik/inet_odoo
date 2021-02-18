# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': "Module for managing the hospitals",
    'description': """
        Long description of module's purpose
    """,

    'author': "Intelligent Network | Bouchafa Lotfi Rafik",
    'website': "http://www.inet.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,

}
