# Данные для проверки

# Заголовки кнопок запросов
requests_titles = ['LIST USERS', 'SINGLE USER', 'SINGLE USER NOT FOUND', 'LIST <RESOURCE>',
                   'SINGLE <RESOURCE>', 'SINGLE <RESOURCE> NOT FOUND', 'CREATE', 'UPDATE',
                   'UPDATE', 'DELETE', 'REGISTER - SUCCESSFUL', 'REGISTER - UNSUCCESSFUL', 'LOGIN - SUCCESSFUL',
                   'LOGIN - UNSUCCESSFUL', 'DELAYED RESPONSE']

# Списки ключей в ответе
list_res_keys = ['page',
                      'per_page',
                      'total',
                      'total_pages',
                      'data',
                      'support']
single_res_keys = ['data',
                        'support']
update_res_keys = ['name', 'job', 'updatedAt']
create_res_keys = [*update_res_keys[0:2], 'id', 'createdAt']
login = ['token']
register = ['id', *login]
error = ['error']

# Эталонные данные по ответам
responses = {
    'users': [
        {
            'name': 'list',
            'path': '/api/users?page=2',
            'status': '200',
            'res_keys': list_res_keys
        },
        {
            'name': 'user',
            'path': '/api/users/2',
            'status': '200',
            'res_keys': single_res_keys
        },
        {
            'name': 'not_found',
            'path': '/api/users/23',
            'status': '404',
            'res_keys': []
        },
        {
            'name': 'create',
            'path': '/api/users',
            'status': '201',
            'res_keys': create_res_keys
        },
        {
            'name': 'update_put',
            'path': '/api/users/2',
            'status': '200',
            'res_keys': update_res_keys
        },
        {
            'name': 'update_patch',
            'path': '/api/users/2',
            'status': '200',
            'res_keys': update_res_keys
        },
        {
            'name': 'delete',
            'path': '/api/users/2',
            'status': '204',
            'res_keys': []
        },
        {
            'name': 'delayed',
            'path': '/api/users?delay=3',
            'status': '200',
            'res_keys': list_res_keys
        }
    ],
    'register': [
        {
            'name': 'success',
            'path': '/api/register',
            'status': '200',
            'res_keys': register
        },
        {
            'name': 'unsuccess',
            'path': '/api/register',
            'status': '400',
            'res_keys': error
        }
    ],
    'login': [
        {
            'name': 'success',
            'path': '/api/login',
            'status': '200',
            'res_keys': login
        },
        {
            'name': 'unsuccess',
            'path': '/api/login',
            'status': '400',
            'res_keys': error
        }
    ],
    'unknown': [
        {
            'name': 'list',
            'path': '/api/unknown',
            'status': '200',
            'res_keys': list_res_keys
        },
        {
            'name': 'unknown',
            'path': '/api/unknown/2',
            'status': '200',
            'res_keys': single_res_keys
        },
        {
            'name': 'not_found',
            'path': '/api/unknown/23',
            'status': '404',
            'res_keys': []
        }
    ]
}
