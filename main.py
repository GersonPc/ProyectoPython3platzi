import sys

clientes = [
    {
        'name': 'Juan',
        'company': 'Maxidespensa',
        'email' : 'Juan@maxi.com',
        'position' : 'Sofware Engineer'
    },
    {
        'name': 'Pedro',
        'company': 'Google',
        'email' : 'Pedro@google.com',
        'position' : 'UX Designer'
    },
]

def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes.append(client_name)
    else:
        print('Client alredy is in client\'s list')

def list_clients():
    for idx, cliente in enumerate(clientes):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=cliente['name'],
            company=cliente['company'],
            email=cliente['email'],
            position=cliente['position']

        ))

def update_client_search(client_name):
    global clientes
    indice = 0
    for idx in clientes:
        indice += 1
        for values in idx.values():
            if client_name == values:
                return indice - 1

def update_client(client_name, update_people):
    global clientes
    indice =  int(update_client_search(client_name))
    clientes [indice] = update_people

def searh_client(name):
    global clientes
    for idx in clientes:
        for persona in idx.values():
            if name == persona:
                return True
            else:
                False

def delete_client(client_name):
    global clientes
    if client_name in clientes:
        clientes.remove(client_name)
    else:
        print('Not Found Client')

def _print_welcome():
    print('Welcome To Platzi Ventas')
    print('*' * 50)
    print('What would yo like to day')
    print('[L]ist clients')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name

if __name__ == "__main__":
    _print_welcome()

    commad = input()
    commad = commad.upper()
    if commad == 'C':
        client_name = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client_name)
        list_clients()
    elif commad == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif commad == 'U':
        client_name = _get_client_name()
        found = searh_client(client_name)
        if found:
            update_client_name = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
            update_client(client_name,update_client_name)
            list_clients()
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

    elif commad == "S":
        client_name = _get_client_name()
        found = searh_client(client_name)
        if found:
            print("The client is in the list client\'s")
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

    elif commad == 'L':
        list_clients()
    else:
        print('Command Invalid')