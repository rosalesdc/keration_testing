{
    'name': "Agregar Menu Especificaciones",

    'summary': """
    """,

    'description': """
        Módulo para agregar un menú que permite generar las opciones de las Especificaciones de las piedras
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
        'views/add_menu_especificaciones.xml',
    ],
    'installable':True,
    'auto_install':False,
}