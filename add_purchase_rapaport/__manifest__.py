# -*- coding: utf-8 -*-
{
    'name': "Extensión de vista de compra con parámetros rapaport",

    'summary': """ Soporte para campos de joyería en modelos purchase.order y purchase.order.line
    """,

    'description': """
    Soporte para campos de joyería en modelos purchase.order y purchase.order.line
    Costo USD Quilate (Número calculado) (costo_quilate_usd); 
    Costo Total (Número calculado moneda) (costo_total_usd);

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
        'purchase',        
    ],

    # always loaded
	'data': [
	'views/add_purchase_rapaport_view.xml',
#    'views/new_wizard_view.xml',
	'templates.xml',
	'reports.xml',
    ],
	'demo':[

	],
    'installable':True,
}
