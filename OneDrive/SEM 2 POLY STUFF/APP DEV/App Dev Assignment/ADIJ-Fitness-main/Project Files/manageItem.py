import shelve

from flask import session

from item import Item
import random

db_item = 'store'
db_cart = 'cart'
db_user = 'user'
db_item_key = 'item'
db_single = 'single'


# item_dict = {}
# db = shelve.open(db_item)
# if db_product_key in db:
#     item_dict = db[db_product_key]
# db.close()
# for item in item_dict.values():
#     print(item)


def get_item_list():
    item_list = []
    db = shelve.open(db_item)
    for i in db:
        item_list.append(db[i])
    db.close()
    return item_list


def get_item(id):
    result = None
    db = shelve.open(db_item)
    for i in db:
        if i == id:
            result = db[i]
    db.close()
    return result


def user_cart(email):
    user_dict = {}
    db = shelve.open(db_user)
    for i in db:
        user_dict[email] = item_list
        return item_list
    db.close()


def save_item(item):
    db = shelve.open(db_item)
    db[item.id] = item
    db.close()


def delete_item_id(id):
    db = shelve.open(db_item)
    for i in db:
        if db[i].id == id:
            del db[i]
    db.close()


def list_cart(uid):
    cart_list = []
    db = shelve.open(db_cart)
    for i in db:
        if db[i].buyer == uid:
            cart_list.append(db[i])
    db.close()
    return cart_list


def remove_from_cart(uid, item):
    db = shelve.open(db_cart)
    item.buyer = uid
    if item.id in db:
        item = db[item.id]
        if item.count > 1:
            item.deduct_count()
        else:
            del db[item.id]
            db.close()
            return
    db[item.id] = item
    db.close()


def add_to_cart(uid, item):
    db = shelve.open(db_cart)
    print("Add to cart\n{}".format(item))
    item.buyer = uid
    print("Add to cart\n{}".format(item))
    if item.id in db:
        item = db[item.id]
        item.add_count()

    db[item.id] = item

    db.close()


# def single_purchase(uid, item):
#     db = shelve.open(db_single)
#     item.buyer = uid
#     db[item.id] = item
#     db.close()


# def add_count(uid, id):
#     cart_list = []
#     db = shelve.open(db_cart)
#     for i in db:
#         if db[i] == uid:
#             if i in cart_list:
#                 cart_list[i].count += 1
#     return cart_list

#
# item_list = []
# db = shelve.open(db_cart)
# for i in db.values():
#     item_list.append(i)
# db.close()
# for j in item_list:
#     print(j)
# print(item_list)
