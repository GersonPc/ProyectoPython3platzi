import random

def busqueda_binario(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) /2
    mid = int(mid)
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return busqueda_binario(data, target, low, mid -1)
    else:
        return busqueda_binario(data, target, mid + 1, high)

def busqueda_binaria(data, target, low, high):
    while True:
        if low > high:
            return False
        mid = (low + high) /2
        mid = int(mid)

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid +1


if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(10)]
    data.sort()
    print(data)
    target = int(input("Que numero quieres buscar"))
    found = busqueda_binario(data, target, 0, len(data) -1)
    found2 = busqueda_binaria(data, target, 0, len(data) -1)
    print('Busqueda Binaria con recursion: {}'.format(found))
    print('Busqueda Binaria con Loop: {}'.format(found2))