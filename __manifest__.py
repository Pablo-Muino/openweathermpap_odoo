{
    'name': 'OpenWeatherMap Integration',
    'version': '1.0',
    'summary': 'Integración con la API de OpenWeatherMap',
    'description': 'Obtención de datos meteorológicos en tiempo real.',
    'author': 'Pablo Muiño',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/weather_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'icon': '/openweathermpap_odoo/static/description/icon57.png'
}