import json


def render_html(func):
    def wrapped(**kwargs):
        yield ["<html>\n<head><head>\n<body>\n", ]
        for stock in func(**kwargs):
            yield ["\n=============", stock[0], "=============", ]
            yield ["Talla: {}. Color: {}".format(size, color) for color, size in stock[1]]
        yield ["</body>\n</html>\n", ]

    return wrapped


def render_api(func):
    def wrapped(**kwargs):
        api_result = []
        for stock in func(**kwargs):
            list_colors_and_sizes = [(color, size) for color, size in stock[1]]
            ziped_list = list(zip(*list_colors_and_sizes))
            colors = list(set(ziped_list[0]))
            size = list(set(ziped_list[1]))
            api_result.append({
                "name": stock[0],
                "colors": colors,
                "size": size,
            })
        app_json = json.dumps(api_result, indent=2)
        yield [app_json, ]

    return wrapped


def shirts(sizes_whitelist=[], colors_whitelist=[]):
    colors = ["black", "white", "red"]
    sizes = ["S", "M", "L"]
    return ((color, size) for color in colors if color in colors_whitelist
            for size in sizes if size in sizes_whitelist)


@render_api
def get_shops_stock():
    shops = [
        {
            "name": "Shop 1",
            "sizes": ["M", "L"],
            "colors": ["white", "red"]
        },
        {
            "name": "Shop 2",
            "sizes": ["S", "M"],
            "colors": ["black", "white"]
        }
    ]
    for shop in shops:
        yield shop["name"], shirts(shop["sizes"], shop["colors"])


if __name__ == '__main__':
    for stock in get_shops_stock():
        print(*stock, sep='\n')