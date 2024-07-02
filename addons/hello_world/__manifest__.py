{
    'name': 'Hello World',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A simple Hello World module',
    'description': 'This is a simple module that displays Hello World',
    'author': 'Your Name',
    'website': 'http://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hello_world_view.xml',
    ],
    'installable': True,
    'application': True,
}