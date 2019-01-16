# -*- coding: utf-8 -*-
{
    'name': "Wizard para cambiar categoria",

    'summary': """Ejercicios
    """,

    'description': """
        Modulos funcionales para Keration
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',        
    ],

    # always loaded
	'data': [
	'views/wizard_category_view.xml',
#    'views/new_wizard_view.xml',
	'templates.xml',
	'reports.xml',
    ],
	'demo':[

	],
    'installable':True,
}
