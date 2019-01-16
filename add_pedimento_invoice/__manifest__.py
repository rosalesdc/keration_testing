# -*- coding: utf-8 -*-
{
    'name': "Agregar pedimento",

    'summary': """
    """,

    'description': """
        Agrega campo de pedimento a factura de compra
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
        'views/add_pedimento_invoice_view.xml',
    ],
	'demo':[

	],
    'installable':True,
}
