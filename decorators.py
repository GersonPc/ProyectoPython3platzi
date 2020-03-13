PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input("What is your password?: ")
        if password == PASSWORD:
            return func()
        else:
            print('The password is incorrect')
    return wrapper

@password_required
def need_password():
    print('The password is correct')

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@upper
def say_my_name(name):
    return 'Hola {}'.format(name)

if __name__ == "__main__":
    print(say_my_name('Gerson'))
    need_password()