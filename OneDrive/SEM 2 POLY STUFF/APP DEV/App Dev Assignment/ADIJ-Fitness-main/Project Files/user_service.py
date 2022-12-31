import shelve
from datetime import datetime
from User import User

db_name = 'library'
db_users_key = 'users'


def check_status(user):
    return user.status > 0


# get the time updated
def by_time_updated(user):
    return user.time_updated


def by_gender(user):
    return user.gender


def by_user_type(user):
    return user.user_type


def get_user_type():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    user_list = filter(check_status, user_list)
    user_list = sorted(user_list, key=by_user_type, reverse=True)
    return user_list


def get_user_type_reverse():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    user_list = filter(check_status, user_list)
    user_list = sorted(user_list, key=by_user_type)
    return user_list


def get_user_gender():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    print(type(user_list))
    user_list = filter(check_status, user_list)
    user_list = sorted(user_list, key=by_gender, reverse=True)
    return user_list


def get_user_gender_reverse():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    user_list = filter(check_status, user_list)
    user_list = sorted(user_list, key=by_gender)
    return user_list


def get_user_list():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    user_list = filter(check_status, user_list)
    user_list = sorted(user_list, key=by_time_updated, reverse=True)
    return user_list


def get_user(id):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    if id in user_dict:
        result = user_dict[id]
    return result


def get_user_for_login(email, password):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    for user in user_dict.values():
        if user.email.upper() == email.upper() and \
                user.password == password and \
                user.status == User.status_active:
            result = user
    return result


def save_user(user):
    user.time_updated = datetime.now()
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    user_dict[user.id] = user
    db[db_users_key] = user_dict
    db.close()


def exist_email():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_email = []
    for user in user_dict.values():
        user_email.append(user.email.upper())
    return user_email


def delete_user_email(id):
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
       user_dict = db[db_users_key]
       user_dict.pop(id)
       db[db_users_key]= user_dict
       db.close()


def get_user_info(email,name,birthday):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    for user in user_dict.values():
        if user.email.upper() == email.upper() and \
                user.name.upper() == name.upper() and \
                user.birthday == birthday:
            result = user
    return result


def user_id(email,name,birthday):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    for i in user_list:
        if i.email.upper() == email.upper() and \
             i.name.upper() == name.upper() and\
             i.birthday == birthday:
           result = i.id
    return result


def get_user_profile(email):
    result = None
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
        user_dict = db[db_users_key]
    db.close()
    user_list = user_dict.values()
    for i in user_list:
        if i.email.upper() == email.upper():
            result = i
    return result


def get_timeline():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
       user_dict = db[db_users_key]
       db[db_users_key]= user_dict
    db.close()
    user_time_created = []
    for user in user_dict.values():
         user_time_created.append(user.get_time_created_str()[0:10])
    timeline = []
    for time in user_time_created:
        if time not in timeline:
            timeline.append(time)
    return timeline


def get_number_user():
    user_dict = {}
    db = shelve.open(db_name)
    if db_users_key in db:
       user_dict = db[db_users_key]
       db[db_users_key]= user_dict
    db.close()
    user_time_created = []
    for user in user_dict.values():
        user_time_created.append(user.get_time_created_str()[0:10])
    number_user_dict ={}
    for date in user_time_created:
       if date not in number_user_dict:
          count = 1
          number_user_dict[date] = count
       elif date in number_user_dict:
          number_user_dict[date] +=1
    number_user =[]
    for date in number_user_dict:
         number_user.append(number_user_dict[date])
    return number_user





# user_dict = {}
# db = shelve.open(db_name)
# if db_users_key in db:
#     user_dict = db[db_users_key]
#     db[db_users_key]= user_dict
# db.close()
# for user in user_dict.values():
#     print(user)
# user_time_created = []
# for user in user_dict.values():
#     user_time_created.append(user.get_time_created_str()[0:10])
# print(user_time_created)
# timeline = []
# for time in user_time_created:
#     if time not in timeline:
#        timeline.append(time)
# print(timeline)
# count = 0
# number_user_dict ={}
# for date in user_time_created:
#     if date not in number_user_dict:
#        count = 1
#        number_user_dict[date] = count
#     elif date in number_user_dict:
#        number_user_dict[date] +=1
# print(number_user_dict)
# number_user =[]
# for date in number_user_dict:
#     number_user.append(number_user_dict[date])
# print(number_user)

# db = shelve.open(db_name)
# for i in db[db_users_key].values():
#     if i.email == "diend@gmail.com":
#         i.profile_image = "09e396aa-6134-412c-b795-a0ca028d09bd.jpg"
#         print(i)
# db.close()
