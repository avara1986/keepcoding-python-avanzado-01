from datetime import datetime


class MyServer:
    __routes = {}

    def route(self, rule, *args, **kwargs):
        def decorator(f):
            self.add_url_rule(rule, f)
            return f

        return decorator

    def add_url_rule(self, rule, view_func=None):
        self.__routes[rule] = view_func
        print("regla {} añadida".format(rule))

    def dispatch(self, rule, *args, **kwargs):
        return self.__routes[rule](*args, **kwargs)


app = MyServer()


@app.route("/")
def mi_funcion():
    return "Hello index!"


@app.route("/user/")
def mi_funcion2(iduser=None):
    return "Recuperando el usuario ID #{}".format(iduser)


if __name__ == '__main__':
    print("Start script")
    print(app.dispatch("/"))
    print(app.dispatch("/user/", 24))
