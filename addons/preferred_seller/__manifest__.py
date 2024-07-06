{
    'name': 'preferred_seller',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'This is a simple module that adds a custom field preferred_seller to product',
    'description': 'This is a simple module that adds a custom field preferred_seller to product',
    'author': 'Matthieu - Test Neoshore',
    'website': 'http://www.example.com',
    'depends': ['base', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/preferred_seller_view.xml',
    ],
    'installable': True,
    'application': True,
}