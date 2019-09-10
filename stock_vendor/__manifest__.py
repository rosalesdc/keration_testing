# -*- coding: utf-8 -*-
{
    'name': "Vendedor Stock",

    'summary': """
        Muestra el vendedor con productos de Stock
        """,

    'description': """
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','stock','product','add_fields_rapaport','inventory_price'],

    'data': [
        'views/stock_vendor_view.xml',
        'views/stock_report_picking_vendor.xml'
    ],

    'installable':True,
    'auto_install':False,
}