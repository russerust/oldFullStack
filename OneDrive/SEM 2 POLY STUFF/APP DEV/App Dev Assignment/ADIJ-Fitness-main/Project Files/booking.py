import uuid
from datetime import datetime
from constants import datetime_format, date_format
from User import User



class Bookings:

    activity = {
        "Programme",
        "Gym"
    }

    gender = {
        "Male",
        "Female",
    }

    timings = {
        "0630-0730",
        "0730-0830",
        "0830-0930",
        "0930-1030",
        "1030-1130",
        "1230-1330",
        "1330-1430",
        "1430-1530",
        "1530-1630",
        "1630-1730",
        "1730-1830",
        "1830-1930",
        "1930-2030",
        "2030-2130",
        "2130-2230",
        "2230-2330",
        "2330-0030",
        "0030-0130",
        "0130-0230",
        "0230-0330",
        "0330-0430"
    }

    def __init__(self, email, activity, date, location, time, gender, payment):
        self.id = str(uuid.uuid4())
        self.gender = gender
        self.email = email
        self.activity = activity
        self.location = location
        self.time = time
        self.payment = payment
        self.time_created = datetime.now()
        self.time_updated = datetime.now()
        temp = datetime.strptime(date, date_format).date()
        self.date = temp.strftime(date_format)

    def get_email(self):
        return self.email

    def set_date(self, date):
        self.date = date
        return self.date

    def set_location(self, location):
        self.location = location
        return self.location

    def set_time(self, time):
        self.time = time
        return self.time

    def set_activity(self):
        return self.activity

    def get_location(self):
        return self.location

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_activity(self):
        return self.activity

    def get_programme(self):
        return self.activity

    def get_booktime_created_str(self):
        return self.time_created.strftime(datetime_format)

    def get_booktime_updated_str(self):
        return self.time_updated.strftime(datetime_format)

    def __str__(self):
        return f'Email: {self.email}\n' \
               f'Gender: {self.gender}\n'\
               f'Activity: {self.activity}\n' \
               f'Date: {self.get_date()}\n' \
               f'Location: {self.location}\n' \
               f'Time: {self.time}\n' \
               f'Payment: {self.payment}\n' \
               f'Date Created: {self.get_booktime_created_str()}\n' \
               f'Date Updated: {self.get_booktime_updated_str()}\n'


def months():
    list = []
    start = 1
    while start <= 12:
        list.append(str(start))
        start += 1

    return list


def year():
    list = []
    start = 2022
    while start <= 2040:
        list.append(str(start))
        start += 1
    return list


paymentTypes = ['Visa', 'MasterCard', 'American Express']

