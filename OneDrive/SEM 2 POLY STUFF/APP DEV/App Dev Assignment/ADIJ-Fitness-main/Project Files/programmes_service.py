import shelve
import os
from programmes import Programme

db_programme = 'programmes'
db_programme_key = 'programmeKey'


def save_prog(prog):
    prog_dict = {}
    db = shelve.open(db_programme)
    if db_programme_key in db:
        prog_dict = db[db_programme_key]
    prog_dict[prog.id] = prog
    db[db_programme_key] = prog_dict
    db.close()


def update_programme(new_title, new_d, img, id2):
    db = shelve.open(db_programme)
    filename = None
    programme_dict = {}
    programme_dict = db[db_programme_key]
    if db_programme_key in db:
        programme_dict = db[db_programme_key]
    prog_list = programme_dict.items()
    for id1, programme in prog_list:
        if id1 == id2:
            programme.title = new_title
            programme.desc = new_d
            programme.image = img
            programme.id = id2
            db[db_programme_key] = programme_dict


def get_prog_list():
    prog_dict = {}
    db = shelve.open(db_programme)
    if db_programme_key in db:
        prog_dict = db[db_programme_key]
    db.close()
    prog_list = prog_dict.values()

    return prog_list


def get_prog(title):
    result = None
    prog_dict = {}
    db = shelve.open(db_programme)
    if db_programme_key in db:
        prog_dict = db[db_programme_key]
    db.close()
    if title in prog_dict:
        result = prog_dict[title]
    return result


def delete_prog(id2):
    prog_dict = {}
    db = shelve.open(db_programme)
    prog_dict = db[db_programme_key]
    if db_programme_key in db:
       prog_dict = db[db_programme_key]
    filename = None
    prog_list = prog_dict.values()
    for i in prog_list:
        if i.id == id2:
            filename = i.image
    imagePath = "static/uploads/" + filename
    os.remove(imagePath)

    if db_programme_key in db:
       prog_dict = db[db_programme_key]
       prog_dict.pop(id2)
       db[db_programme_key] = prog_dict
       db.close()


def prog_list_form():
    prog_dict = {}
    db = shelve.open(db_programme)
    if db_programme_key in db:
        prog_dict = db[db_programme_key]
    db.close()
    prog_list = prog_dict.values()
    # print("[prog]:\n{}\n".format(prog_list))
    list = ["Gym"]
    for i in prog_list:
        list.append(i.title)
    return list


# prog_dict = {}
# db = shelve.open(db_programme)
# if db_programme_key in db:
#     prog_dict = db[db_programme_key]
# db.close()
# prog_list = prog_dict.values()
# for i in prog_list:
#     print(i)
#
# print(prog_dict.items())


