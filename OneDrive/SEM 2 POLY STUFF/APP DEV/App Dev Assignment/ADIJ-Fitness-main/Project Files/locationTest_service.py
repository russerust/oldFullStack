import shelve
from location import Location
import os

db_name = 'locations'
db_location_key = 'loc'

db = shelve.open(db_name, 'c')
db.close()


def add_location(loc):
    loc_dict = {}
    db = shelve.open(db_name)
    if db_location_key in db:
        temp = db[db_location_key]
        temp[loc.id] = loc
        db[db_location_key] = temp
        print("[add_location] Location : {} added!\n".format(loc.location))
    db.close()


def update_location(id, loc, img):
    db = shelve.open(db_name)
    filename = None
    location_dict = {}
    location_dict = db[db_location_key]
    if db_location_key in db:
       location_dict = db[db_location_key]
    location_list = location_dict.items()
    print(location_list)
    for idc, value in location_list:
        print(id)
        if idc == id:
            filename = value.image
    imagePath = "static/uploads_location/" + filename
    os.remove(imagePath)

    if db_location_key in db:
        temp = db[db_location_key]
        for key, value in temp.items():
            if key == id:
                value.location = loc
                value.image = img
                db[db_location_key] = temp
                db.close()
                break
    db.close()


def get_location_list():
    temp = None
    db = shelve.open(db_name)
    if db_location_key not in db:
        db[db_location_key] = {}
    if db_location_key in db:
        temp = db[db_location_key]
    db.close()
    location_list = temp
    print("[get_location_list] Locations grabbeddededed:\n{}".format(location_list))
    return location_list


def for_location_form():
    temp = {}
    form_list = []
    db = shelve.open(db_name)
    if db_location_key not in db:
        db[db_location_key] = {}
    if db_location_key in db:
        temp = db[db_location_key]
    db.close()
    for value in temp.values():
        if value.status == 1:
            form_list.append(value.location)
    location_list = form_list
    print("[for_location_form] Locations grabbed:\n{}".format(location_list))
    return location_list


def get_location(id):
    temp = None
    db = shelve.open(db_name)
    if db_location_key in db:
        temp = db[db_location_key]
    db.close()
    for key, value in temp.items():
        if key == id:
            return value


def get_location_image(id):
    temp = None
    db = shelve.open(db_name)
    if db_location_key in db:
        temp = db[db_location_key]
    db.close()
    for key, value in temp.items():
        if key == id:
            return value.image


def get_location_id(name):
    temp = None
    db = shelve.open(db_name)
    if db_location_key in db:
        temp = db[db_location_key]
    db.close()
    for key, value in temp.items():
        if value.location == name:
            return key


def del_location(del_loc):
    temp = {}
    print(del_loc)
    db = shelve.open(db_name)
    if db_location_key in db:
        temp = db[db_location_key]
        for key, value in temp.items():
            print("key\n{}\nvalue\n{}\n".format(key, value))
            if del_loc == key:

                value.close_location()
                print(value)
                db[db_location_key] = temp
                break
    db.close()


def location_verify(new_loc):
    db = shelve.open(db_name)
    temp = db[db_location_key]
    for id, value in temp.items(): # id, value: def str()
        print("id\n{}\nvalue\n{}\n".format(id, value))
        if new_loc == value.location:
            if value.status == 0:
                db.close()
                return "activate"
            db.close()
            return "exists"

    db.close()
    return "new"


def activate_location(loc):
    db = shelve.open(db_name)
    temp = db[db_location_key]
    for id, value in temp.items():
        if loc == value.location:
            value.open_location()
            db[db_location_key] = temp
            db.close()
            break


def save_location(location):
    location_dict = {}
    db = shelve.open(db_name)
    if db_location_key in db:
        location_dict = db[db_location_key]
    location_dict[location.id] = location
    db[db_location_key] = location_dict
    db.close()


# db = shelve.open(db_name)
# for i in db[db_location_key]:
#     print(i)
# db.close()
# del_location("Yio Chu Kang")



# db = shelve.open(db_name)
# db.clear()
# db.close()
