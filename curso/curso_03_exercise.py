def shirts(sizes_whitelist=[], colors_whitelist=[]):
    colors = ["black", "white", "red"]
    sizes = ["S", "M", "L"]
    return ((color, size) for color in colors  if color in colors_whitelist
            for size in sizes if size in sizes_whitelist)


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
        print("\n=============", stock[0], "=============", sep='\n')
        print("", *("Talla: {}. Color: {}".format(size, color) for color, size in stock[1]), sep='\n*')
