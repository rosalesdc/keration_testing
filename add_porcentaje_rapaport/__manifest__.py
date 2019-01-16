# -*- coding: utf-8 -*-
{
    'name': "Agregar columna con porcentaje calculado",

    'summary': """
    """,

    'description': """
        Agregar columna con porcentaje calculado  al listado de productos al momento de venta
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base','sale','product',
    ],

    # always loaded
	'data': [
        'views/add_rapaport_cost_view.xml',
    ],
	'demo':[

	],
    'installable':True,
}
