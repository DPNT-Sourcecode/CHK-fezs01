from collections import Counter
from ..price_offer_sheet import (
    price_table,
    multi_buy_offer,
    free_item_offer,
    group_offer,
)


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
    apply_group_offer(items_cart)

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

            if name == discount_item_name:
                free_self_item(items_cart, name, count, discount_item_name)
            else:
                free_other_item(items_cart, name, count, discount_item_name)


def free_other_item(items_cart, name, count, discount_item_name):
    item_num_free = divmod(items_cart[name], count)[0]
    if name == discount_item_name:
        if items_cart[discount_item_name] == count:
            item_num_free = 0
        if item_num_free > 1:
            item_num_free[0]

    while item_num_free > 0:
        if items_cart[discount_item_name] == 0:
            break
        items_cart[discount_item_name] -= 1
        item_num_free -= 1


def free_self_item(items_cart, name, count, discount_item_name):
    item_bundle_number = divmod(items_cart[name], count + 1)[0]
    single_item_remainder_number = divmod(items_cart[name], count + 1)[1]
    items_cart[discount_item_name] = (
        item_bundle_number * count + single_item_remainder_number
    )


def apply_group_offer(items_cart):
    price = 0
    for count, offer in group_offer.items():
        print(offer.values()[1])
        sort_by_price = sorted(
            offer.values()[0], keys=lambda x: price_table[x], reverse=True
        )
        available_items_for_offer = "".join(
            item_name * items_cart[item_name] for item_name in sort_by_price
        )
        num_offers, num_left_items = divmod(len(available_items_for_offer), count)

        if num_offers == 0:
            continue

        price += offer.keys()[0] * num_left_items

        items_name = set(available_items_for_offer)

        for i in items_name:
            items_cart[i] = 0

        if num_left_items == 0:
            continue

        for name, num in Counter(available_items_for_offer[-num_left_items:]).items():
            items_cart[name] = num

    return price



