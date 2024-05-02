from ..price_offer_sheet import price_table, multi_buy_offer, free_item_offer


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    result = 0
    items_cart = {}

    for sku in skus:
        if sku not in price_table.keys():
            return -1
        items_cart[sku] = items_cart.get(sku, 0) + 1

    apply_free_item_offer(items_cart)

    for name, quantity in items_cart.items():
        if name in multi_buy_offer.keys():
            result += apply_multi_buy_offer(name, quantity)
        else:
            result += price_table[name] * quantity

    return result


def apply_multi_buy_offer(item_name, num_item):
    sorted_offers = list(reversed(sorted(multi_buy_offer[item_name].keys())))
    price_for_item = 0
    item_left = num_item

    for count in sorted_offers:
        apply_offer_count = divmod(item_left, count)
        items_price_with_offer = (
            apply_offer_count[0] * multi_buy_offer[item_name][count]
        )
        price_for_item += items_price_with_offer
        item_left = apply_offer_count[1]

    item_with_no_discount = price_table[item_name] * item_left
    return price_for_item + item_with_no_discount


def apply_free_item_offer(items_cart):
    for name, discount in free_item_offer.items():
        for count, discount_item_name in discount.items():
            if (
                name not in items_cart.keys()
                or discount_item_name not in items_cart.keys()
            ):
                continue
            item_num_free = divmod(items_cart[name], count)[0]

            if name == discount_item_name:
                if items_cart[discount_item_name] == count:
                    item_num_free = 0
                if item_num_free > 1:
                    item_num_free -= 1

            while item_num_free > 0:
                if items_cart[discount_item_name] == 0:
                    break
                items_cart[discount_item_name] -= 1
                item_num_free -= 1


