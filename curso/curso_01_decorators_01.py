from datetime import datetime


def timethis(fn_to_decorate, *args2, **kwargs2):
    # print("start to count time?")
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print("Arguments Decorator: %s, %s" % (args2, kwargs2))
        print("Arguments Function: %s, %s" % (args, kwargs))
        fn = fn_to_decorate(*args, **kwargs)
        print("Execution time of {}: {}".format(kwargs2.get("fn_name", "function"), datetime.now() - start_time))
        return fn

    return wrapper


@timethis
def mi_funcion():
    return [i ** 23 for i in range(10000000)]


def mi_funcion2(fn_name):
    return [i ** 23 for i in range(10000000)]


if __name__ == '__main__':
    print("Start script")

    result = mi_funcion()
    print(result[:10])
    print("\n\n======================================================\n\n")
    print(timethis(mi_funcion2, fn_name="mi super funcion con decorador")(fn_name="mi super funcion")[:10])
    print("\n\n======================================================\n\n")
    result = mi_funcion()
    print(result[:10])