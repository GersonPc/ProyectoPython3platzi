import sys

clients = 'Juan,Pedro,Mario,'

def create_client(name):
    global clients
    if name not in clients:
        clients += name
        _add_comma()
    else:
        print('Is client al ready in list client\'s')

def update_client(name,update_client_name):
    global clients

    if name in clients:
        clients = clients.replace(name + ',', update_client_name + ',')
        list_clients()
    else:
        print('*'*10)
        print('Client Not Found')
        print('*'*10)
        list_clients()

def delete_client(name):
    global clients
    if name in clients:
        clients = clients.replace(name + ',' , '')
    else:
        print('*'*10)
        print('Client Not Found')
        print('*'*10)
        list_clients()

def search_client(client_name):
    global clients
    lista_de_clientes = clients.split(',')
    for cliente in lista_de_clientes:
        if cliente != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients
    clients += ','

def list_clients():
    global clients
    print(clients)

def _print_welcome():
    print('Welcome to my code')
    print('*' * 50)
    print('What would yo like do today?')
    print('[L]ist clients')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')

def _get_client_name():
    client_name = None
    while not client_name:
        if client_name == 'exit':
            break
        client_name = input('What is the cliente name?: ')

    if not client_name:
        sys.exit()
    return client_name

    
if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper() 
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name, update_client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('El cliente esta en la lista de clientes')
        else:
            print('El cliente {} no esta en la lisat de clientes'.format(client_name))
    elif command == 'L':
        list_clients()
    else:
        print('Comand Invalid')