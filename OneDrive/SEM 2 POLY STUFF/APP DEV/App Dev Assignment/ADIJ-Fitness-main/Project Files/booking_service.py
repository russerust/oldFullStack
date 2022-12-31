import shelve
from wtforms import validators
from datetime import datetime
from booking import Bookings
from flask import session
from constants import *

db_name = 'booking'
db_booking_key = 'book'


db = shelve.open(db_name, 'c')
db.close()


def by_activity(booking):
    return booking.activity


def by_date(booking):
    return datetime.strptime(booking.date, date_format)


def by_time_updated(booking):
    return datetime.strptime(booking.get_booktime_updated_str(), datetime_format)


def by_email(booking):
    return booking.email


def by_gender(user):
    return user.gender


def by_location(booking):
    return booking.location


def by_time(booking):
    return booking.time


def get_booking_gender():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    booking_list = booking_dict
    da_list = sorted(da_list, key=by_gender)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_list, da_list


def get_booking_gender_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_gender, reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_activity_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_activity, reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_activity():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_activity)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_loc():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_location)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_time():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_time)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_date():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_date)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_date_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_date,reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_time_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_time, reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_loc_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_location, reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_email():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_email, reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_time_updated():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_time_updated)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_time_updated_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_time_updated, reverse=True)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list


def get_booking_email_reverse():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        booking_dict = db[db_booking_key]
    db.close()
    da_list = []
    for k, v in booking_dict.items():
        for key, user in v.items():
            da_list.append(user)
    da_list = sorted(da_list, key=by_email)
    print("pp[[]]]]]]\n{}".format(da_list))
    return booking_dict, da_list



def remove_session():
    session.pop('activity', None)
    session.pop('date', None)
    session.pop('location', None)
    session.pop('location_id', None)
    session.pop('time', None)
    session.pop('payment', None)


def get_booking(id):
    result = None
    book_dict = {}
    email = session['user_email']
    db = shelve.open(db_name)
    if db_booking_key in db:
        book_dict = db[db_booking_key]
    db.close()
    if id in book_dict[email]:
        result = book_dict[email][id]
    return result


def save_booking(b):
    b.time_updated = datetime.now()
    user_dict = {}
    email = session['user_email']
    db = shelve.open(db_name)
    if db_booking_key in db:
        user_dict = db[db_booking_key]
        if email not in db[db_booking_key]:
            user_dict[email] = {}
        user_dict[email].update({b.id: b})
    db[db_booking_key] = user_dict
    db.close()


def delete_booking(id):
    user_dict = {}
    email = session['user_email']
    db = shelve.open(db_name)
    if db_booking_key in db:
       user_dict = db[db_booking_key]
       user_dict[email].pop(id)
       db[db_booking_key]= user_dict
       # print("[delete_booking] Deleted booking!\n")
       db.close()


def get_booking_list():
    book_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        book_dict = db[db_booking_key]
        # print("[get_booking_list] Booking list grabbed:\n{}\n".format(book_dict))
    db.close()
    book_list = book_dict
    return book_list


def retrieve_booking(id):
    book_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        book_list = {}
        book_list = db[db_booking_key]
        for key, value in book_list.items():
            for k, v in value.items():
                if k == id:
                    email = key
                    result = book_list[email]
                    db.close()
                    result = book_list[email][id]
                    print(result)
                    return result


def retrieve_save_booking(b):
    b.time_updated = datetime.now()
    # print("[retrieve_save_booking]User ID used for saving:\n{}\n".format(b.id))
    user_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
        user_dict = db[db_booking_key]
        for key, value in user_dict.items():
            # print("key {}, value {}\n".format(key, value))
            for k, v in value.items():
                if k == b.id:
                    email = key
                    # print("[retrieve_save_booking]Saved booking email:\n{}\n".format(email))
                    # print("[retrieve_save_booking]User dictionary before saving:\n{}\n".format(user_dict))
                    user_dict[email][b.id] = b
                    # print("[retrieve_save_booking]User dictionary after saving:\n{}\n".format(user_dict))
                    db[db_booking_key] = user_dict
                    db.close()
                    break


def retrieve_delete_booking(id):
    user_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
       user_dict = db[db_booking_key]
       for key, value in user_dict.items():
        print("[retrieve_delete_booking]Key:\n{}\nValue:\n{}\n".format(key, value))
        for k, v in value.items():
            print("[retrieve_delete_booking]Key:\n{}\nValue:\n{}\n".format(k, v))
            if k == id:
                email = key
                print("[retrieve_delete_booking]Deleted booking email:\n{}\n".format(email))
                user_dict[email].pop(id)
                db[db_booking_key] = user_dict
                db.close()
                break
            # break


def get_timebook():
    book_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
       book_dict = db[db_booking_key]
       db[db_booking_key]= book_dict
    db.close()
    booking_time_created = []
    for book in book_dict.values():
        for key, value in book.items():
            tempTime = value.get_booktime_created_str()
            booking_time_created.append(tempTime[0:10])
    timeline = []
    for time in booking_time_created:
        if time not in timeline:
            timeline.append(time)
    return timeline


def get_number_gym():
    booking_dict = {}
    db = shelve.open(db_name)
    if db_booking_key in db:
       booking_dict = db[db_booking_key]
       db[db_booking_key]= booking_dict
    db.close()
    booking_time_created = []
    for book in booking_dict.values():
        for key, value in book.items():
            tempTime = value.get_booktime_created_str()
            booking_time_created.append(tempTime[0:10])
    number_user_dict ={}
    for date in booking_time_created:
       if date not in number_user_dict:
          count = 1
          number_user_dict[date] = count
       elif date in number_user_dict:
          number_user_dict[date] +=1
    print("Number dict:\n{}\n".format(number_user_dict))
    number_user = []
    for date in number_user_dict:
         number_user.append(number_user_dict[date])
    print("Number user:\n{}\n".format(number_user))
    return number_user


# def change_gender_booking(new_gender, email):
#     db = shelve.open(db_name)
#     booking_dict = {}
#     if db_booking_key in db:
#         booking_dict = db[db_booking_key]
#         print("ITS EMAIL\n{}".format(email))
#         print("ITS BOOKING_DICT\n{}".format(booking_dict))
#         if email in booking_dict:
#             print("ITS TRUE ITS TRUE\n{}".format(booking_dict))
#             for key_email, bookings in booking_dict.items():
#                 if key_email == email:
#                     if bookings != {}:
#                         for id, booking in bookings.items():
#                             print("Booking.gender\n{}".format(booking.gender))
#                             if booking.gender != new_gender:
#                                 booking.gender = new_gender
#             db[db_booking_key] = booking_dict
#             db.close()
#         else:
#             db.close()
#     else:
#         db.close()
#         pass
#
#
# def change_email_booking(new_email, old_email):
#     db = shelve.open(db_name)
#     booking_dict = {}
#     if db_booking_key in db:
#         booking_dict = db[db_booking_key]
#         if old_email in booking_dict:
#             print("booking_dict\n{}".format(booking_dict))
#             for email, bookings in booking_dict.items():
#                 if email == old_email:
#                     tempEmail = email
#                     if bookings != {}:
#                         for id, booking in bookings.items():
#                             print("booking\n{}".format(booking))
#                             if booking.email != new_email:
#                                 print("booking.email\n{}\nnew_email\n{}".format(booking.email,new_email))
#                                 booking.email = new_email
#             booking_dict[new_email] = booking_dict[old_email]
#             print("booking_dict[new_email]\n{}\nbooking_dict[old_email]\n{}".format(booking_dict[new_email], booking_dict[old_email]))
#             print("booking_dict\n{}".format(booking_dict))
#             booking_dict.pop(old_email)
#             print("booking_dict\n{}".format(booking_dict))
#             print("booking_dict[new_email]\n{}\nbooking_dict\n{}".format(booking_dict[new_email], booking_dict))
#
#             db[db_booking_key] = booking_dict
#             db.close()
#         else:
#             db.close()
#             pass
#     else:
#         db.close()
#         pass



# def main():
#     location = "Buangkok"
#     add_location(location)
#     many = get_location_list()
#     for i in many:
#         print(i)
#     # print("First stop")
#     # del_location(location)
#     # many2 = get_location_list()
#     # for i in many2:
#     #     print(i)
#
#
# main()

def delete_all_bookings(email):
    print("email\n{}\n".format(email))
    db = shelve.open(db_name)
    print("old db\n{}\n".format(db[db_booking_key]))
    if email in db[db_booking_key]:
        booking_dict = {}
        booking_dict = db[db_booking_key]
        booking_dict.pop(email)
        db[db_booking_key] = booking_dict
    print("new db\n{}\n".format(db[db_booking_key]))
    db.close()

# db = shelve.open(db_name)
# for key, value in db[db_booking_key].items():
#     print(db[db_booking_key])
#     print("Key:\n{}\nValue:\n{}".format(key, value))
# for i in db[db_booking_key]:
#     print(i)
# db.close()

# change_email_booking("dan@gmail.com", "doob@gmail.com")
# delete_all_bookings("dan@gmail.com")

