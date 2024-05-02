# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    result = 0
    price_table = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    multi_buy_price = {"A": {3: 130, 5: 200}, "B": {2: 45}}
    free_item_offer = {"E": {2: "B"}}
    items_cart = {}

    for sku in skus:
        if sku not in price_table.keys():
            return -1
        items_cart[sku] = items_cart.get(sku, 0) + 1

    apply_free_item_offer(items_cart, free_item_offer)

    for name, quantity in items_cart.items():
        if name in multi_buy_price.keys():
            result += apply_multi_buy_offer(
                multi_buy_price, price_table, name, quantity
            )
        else:
            result += price_table[name] * quantity

    return result


def apply_multi_buy_offer(offer_price, price_table, name, quantity):

    apply_offer_count = divmod(quantity, offer_price[name][0])

    items_price_with_offer = apply_offer_count[0] * offer_price[name][1]
    items_price_with_out_offer = price_table[name] * apply_offer_count[1]
    items_total_price = items_price_with_offer + items_price_with_out_offer

    return items_total_price


def apply_free_item_offer(items_cart, free_item_offer):
    for name, discount in free_item_offer.items():
        for count, discount_item_name in discount.items():
            print("NAME", name)
            print(count)
            print(discount_item_name)
            discount_item_name = discount[discount.keys()[0]]  # B

        if name not in items_cart.keys() or discount_item_name not in items_cart.keys():
            continue
        item_num_free = divmod(items_cart[name], discount.keys()[0])[0]

        while item_num_free > 0:
            if items_cart[discount_item_name] == 0:
                break
            items_cart[discount_item_name] -= 1
            item_num_free -= 1

