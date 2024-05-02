# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    result = 0
    price_table = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    offer_price = {"A": (3, 130), "B": (2, 45)}
    free_item_offer = {"E": (2, "B")}
    items_cart = {}

    for sku in skus:
        if sku not in price_table.keys():
            return -1
        items_cart[sku] = items_cart.get(sku, 0) + 1

    for name, discount in free_item_offer.items():
        discount_item_name = discount[1]
        if discount_item_name not in items_cart.keys():
            continue
        item_num_free = divmod(items_cart[name], discount[0])[0]
        while item_num_free > 0:

            items_cart[discount_item_name] -= 1
            item_num_free -= 1

    for name, quantity in items_cart.items():
        if name in offer_price.keys():
            result += calculate_price_for_item_with_offer(
                offer_price, price_table, name, quantity, items_cart
            )
        else:
            result += price_table[name] * quantity

    return result


def calculate_price_for_item_with_offer(offer_price, price_table, name, quantity):

    apply_offer_count = divmod(quantity, offer_price[name][0])

    items_price_with_offer = apply_offer_count[0] * offer_price[name][1]
    items_price_with_out_offer = price_table[name] * apply_offer_count[1]
    items_total_price = items_price_with_offer + items_price_with_out_offer

    return items_total_price




