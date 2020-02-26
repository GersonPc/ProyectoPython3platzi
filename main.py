clientes = 'pablo,juan,'

def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes += client_name
        _add_comma()
    else:
        print('Client alredy is in client\'s list')

def list_clients():
    global clientes
    print(clientes)

def update_client(client_name, update_client_name):
    global clientes
    if client_name in clientes:
        clientes = clientes.replace(client_name + ',', update_client_name + ',')
    else:
        print('Not found client')

def delete_client(client_name):
    global clientes
    if client_name in clientes:
        clientes = clientes.replace(client_name + ',' , '')
    else:
        print('Not Found Client')

def _add_comma():
    global clientes
    clientes += ','

def _print_welcome():
    print('Welcome To Platzi Ventas')
    print('*' * 50)
    print('What would yo like to day')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')
if __name__ == "__main__":
    _print_welcome()

    commad = input()
    commad = commad.upper()
    if commad == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif commad == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif commad == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name,update_client_name)
        list_clients()
    else:
        print('Command Invalid')