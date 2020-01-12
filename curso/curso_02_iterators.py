def mi_funcion():
    for i in range(5):
        print("mi_funcion return {}".format(i))
        yield i


def mi_funcion2():
    return [i for i in mi_funcion()]


if __name__ == '__main__':
    print(mi_funcion())
    print(mi_funcion2())
