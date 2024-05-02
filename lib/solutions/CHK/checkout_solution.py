# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    result = 0
    price_table = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    offer_price = {"A": (3, 130), "B": (2, 45)}
    items_cart = {}

    for sku in skus:
        if sku not in price_table.keys():
            return -1
        items_cart[sku] = items_cart[sku] + 1

    pass

