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
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')

def _get_client_name():
    return input('What is the cliente name? ')

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
    else:
        print('Comand Invalid')