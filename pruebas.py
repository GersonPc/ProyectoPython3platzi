import sys
import random
import csv
import os
CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []
PASSWORD = '1234'

def _initialize_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(cliente):
    global clients
    if cliente not in clients:
        clients.append(cliente)
    else:
        print('Is client al ready in list client\'s')

def update_client(name,update_client_name):
    global clients
    for idx,cliente in enumerate(clients):
        if name == cliente['name']:
            clients[idx] = update_client_name
            list_clients()
        else:
            print('*'*10)
            print('Client Not Found')
            print('*'*10)

        
def delete_client(name):
    global clients
    if name in clients:
        clients.remove(name)
    else:
        print('*'*10)
        print('Client Not Found')
        print('*'*10)
        list_clients()

def search_client(client_name):
    global clients
    for cliente in clients:
        if cliente['name'] != client_name:
            continue
        else:
            return True


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('uid | name | company | email | position.')
        print('{uid} | {name} | {company} | {email} | {position}.'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],
        ))

def _print_welcome():
    print('Welcome to my code')
    print('*' * 50)
    print('What would yo like do today?')
    print('[L]ist clients')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')
    print('*****************************')
    print('[B]usqueda Binaria')
    print('[DE]coradores')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}: '.format(field_name))
    return field

def _get_client_name():
    client_name = None
    while not client_name:
        if client_name == 'exit':
            break
        client_name = input('What is the cliente name?: ')

    if not client_name:
        sys.exit()
    return client_name

def binary_search(data, target, low, high):
    if low > high:
        return False
    mitad = (low + high) // 2
    if target == data[mitad]:
        return True
    elif target < data[mitad]:
        return binary_search(data, target, low, mitad -1)
    else:
        return binary_search(data, target, mitad + 1, high)

def busqueda_binaria2(data, target, low, high):
    while True:
        if low > high:
            return False
        mid = (low + high) // 2
        if target == data [mid]:
            return True
        elif target < data [mid]:
            high = mid - 1
        else:
            low = mid + 1

def busqueda_binaria():
    data = [random.randint(0,100) for i in range(15)]
    data.sort()
    print(data)
    target = int(input("Que numero quieres buscar? "))
    found = binary_search(data, target, 0, len(data) - 1)
    found2 = binary_search(data, target, 0, len(data) - 1)
    print('La busqueda que si funciona: {}'.format(found))
    print('La busqueda que talvez funciona: {}'.format(found2))

def password_requirements(func):
    def wrapper():
        password = input('Cual es tu contrasena? ')
        if password == PASSWORD:
            return func()
        else:
            print('La contrasena no es correcra')
    return wrapper

def decoradores():
    #needs_password()
    print(say_my_name('Gerson'))

@password_requirements
def needs_password():
    print('The password is correct')

def _upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@_upper
def say_my_name(name):
    return 'Hola! {}'.format(name)

if __name__ == '__main__':
    _initialize_from_storage()
    _print_welcome()
    command = input()
    command = command.upper() 
    if command == 'C':
        cliente = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(cliente)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
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
    elif command == 'B':
        busqueda_binaria()
    elif command == 'DE':
        decoradores()
    else:
        print('Comand Invalid')
    _save_clients_to_storage()
