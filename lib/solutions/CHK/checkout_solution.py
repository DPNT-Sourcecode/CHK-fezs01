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

    for name, quantity in items_cart.items():
        if name in offer_price.keys():
            apply_offer_count = divmod(quantity, offer_price[name][0])
            items_price_with_offer = apply_offer_count[0] * offer_price[name][1]
            items_price_with_out_offer = price_table[name] * apply_offer_count[name][1]

    pass


