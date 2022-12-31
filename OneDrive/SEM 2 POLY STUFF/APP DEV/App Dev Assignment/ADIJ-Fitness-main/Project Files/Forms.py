from wtforms import Form, StringField, PasswordField,SelectField,EmailField, DateField, IntegerField, \
    validators, RadioField, ValidationError, TextAreaField,FileField, DecimalField, SubmitField
from flask_wtf import FlaskForm
from User import User
from booking import Bookings, months, year, paymentTypes
from locationTest_service import for_location_form, get_location_list
from programmes_service import prog_list_form
import shelve
from datetime import date, datetime
from constants import datetime_format, date_format

db_name = 'locations'
db_location_key = 'loc'

db = shelve.open(db_name, 'c')
db.close()



class CreateUserForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=15), validators.DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', [validators.Length(min=6, max=15), validators.DataRequired(),
                             validators.EqualTo('password', message='Passwords must match.')])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=User.gender_dict.items(), default='')
    birthday = DateField('Birthday', [validators.Optional()])
    user_type = RadioField('User Type', choices=User.user_type_dict.items(), default='C')


class UpdateUserForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=User.gender_dict.items(), default='')
    birthday = DateField('Birthday', [validators.Optional()])
    user_type = RadioField('User Type', choices=User.user_type_dict.items(), default='C')


class LoginForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=15), validators.DataRequired()])


class accountdetail(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    birthday = DateField('Birthday', [validators.Optional()])
    password = PasswordField('New Password', [validators.Length(min=6, max=15), validators.DataRequired()])
    confirm_password = PasswordField(
        'Confirm New Password', [validators.Length(min=6, max=15), validators.DataRequired(),
                             validators.EqualTo('password', message='Passwords must match.')])


class forgotpassword(Form):
    old_password = PasswordField('Old password', [validators.Length(min=6, max=15), validators.DataRequired()])
    new_password = PasswordField('New Password', [validators.Length(min=6, max=15), validators.DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', [validators.Length(min=6, max=15), validators.DataRequired(),
                             validators.EqualTo('new_password', message='Passwords must match.')])


class searchuser(Form):
    email = EmailField('Seach Email:', [validators.DataRequired(), validators.Email()])


# james calendar Info Form

class UpdateBookForm(FlaskForm):
    today = date.today()
    book = Bookings
    date = DateField('Date', [validators.DataRequired()], default='')
    location = SelectField('Location', [validators.DataRequired()], default='')
    time = SelectField('Time', [validators.DataRequired()], choices=sorted(Bookings.timings), default='')

    def validate_date(form, date):
        if date.data < UpdateBookForm.today:
            raise ValidationError("The date booked cannot be before today! {}".format(UpdateBookForm.today.strftime(date_format)))


class CreateBookForm(FlaskForm):
    today = date.today()
    date = DateField('Date', validators=[validators.DataRequired()])
    location = SelectField('Location', [validators.DataRequired()], default='')
    time = SelectField('Time', [validators.DataRequired()], choices=sorted(Bookings.timings), default='')
    activity = SelectField("Activity", [validators.DataRequired()], choices=prog_list_form(), default='')
    payment = SelectField("Payment Method", [validators.DataRequired()], choices=paymentTypes, default='')

    def validate_date(form, date):
        if date.data < CreateBookForm.today:
            raise ValidationError("The date booked cannot be before today! {}".format(CreateBookForm.today.strftime(date_format)))


# James location form


class CreateLocation(Form):
    location = StringField("Location to add:", [validators.DataRequired()], default='')


class UpdateLocation(Form):
    location = StringField("Location to update:", [validators.DataRequired()], default='')


# Payment form


class paymentVisaGym(FlaskForm):
    number = StringField("Card Number:", validators=[validators.DataRequired(), validators.Length(min=16, max=16), validators.Regexp(regex='^4[0-9]{12}(?:[0-9]{3})?$')], default='')
    name = StringField("Card Holder Name:", [validators.DataRequired()], default='')
    month = SelectField("Expiry Month:", [validators.DataRequired()], choices=months())
    year = SelectField("Expiry Year:", [validators.DataRequired()], choices=year())
    security = PasswordField("Security Number (CVV):", validators=[validators.DataRequired(message="Invalid security number"), validators.Length(min=3, max=3)], default='')

    def validate_number(form, number):
        print("Validate number!\n{}".format(number.data[0]))
        if number.data[0] != "4" and number.data.isdigit():
            print("IT PASSED BRO\n")
            raise ValidationError("Invalid Visa Credit Card Number")


class paymentAEGym(FlaskForm):
    cardNumber = StringField("Card Number:", validators=[validators.DataRequired(), validators.Length(min=15, max=15), validators.Regexp(regex='^3[47][0-9]{13}$')], default='')
    cardName = StringField("Card Holder Name:", [validators.DataRequired()], default='')
    expiryMonth = SelectField("Expiry Month:", [validators.DataRequired()], choices=months())
    expiryYear = SelectField("Expiry Year:", [validators.DataRequired()], choices=year())
    securityNumber = PasswordField("Security Number (CVV):", [validators.DataRequired(message="Invalid security number"), validators.Length(min=3, max=3)], default='')

    def validate_cardNumber(self, cardNumber):
        number = cardNumber.data
        if (number[0] != "3") and ((number[2] != "4") or (number[2] != "7")) and cardNumber.data.isnumeric():
            raise ValidationError("Invalid American Express Credit Card Number")


class paymentMasterGym(FlaskForm):
    cardNumber = StringField("Card Number:", [validators.DataRequired(), validators.Length(min=16, max=16), validators.Regexp(regex='^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$')], default='')
    cardName = StringField("Card Holder Name:", [validators.DataRequired()], default='')
    expiryMonth = SelectField("Expiry Month:", [validators.DataRequired()], choices=months())
    expiryYear = SelectField("Expiry Year:", [validators.DataRequired()], choices=year())
    securityNumber = PasswordField("Security Number (CVV):", [validators.DataRequired(message="Invalid security number"), validators.Length(min=3, max=3)], default='')

    def validate_cardNumber(self, cardNumber):
        if (cardNumber.data[0] != "5") and cardNumber.data.isnumeric():
            raise ValidationError("Invalid MasterCard Number")

# Daniel's add programme forms

class makeProgramme(Form):
    title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Length(min=1, max=300), validators.DataRequired()])


class UpdateProgrammes(Form):
    title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Length(min=1, max=300), validators.DataRequired()])


# Ivan's shop forms

class createItemForm(Form):
    brand = StringField('Brand', [validators.Length(min=1, max=20), validators.DataRequired()])
    product = StringField('Product', [validators.Length(min=1, max=20), validators.DataRequired()])
    size = SelectField('Size', [validators.DataRequired()], choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')],
                       default='S')
    color = SelectField('Color',
                        choices=[('B', 'Black'), ('W', 'White'), ('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'),
                                 ('G', 'Green'), ('Bl', 'Blue'), ('I', 'Indigo'), ('P', 'Purple')], default='B')
    price = IntegerField('Price', [validators.NumberRange(min=1, max=1000), validators.DataRequired()])


class updateItemForm(Form):
    brand = StringField('Brand', [validators.Length(min=1, max=20), validators.DataRequired()])
    product = StringField('Product', [validators.Length(min=1, max=20), validators.DataRequired()])
    size = SelectField('Size', [validators.DataRequired()], choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')],
                       default='S')
    color = SelectField('Color',
                        choices=[('B', 'Black'), ('W', 'White'), ('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'),
                                 ('G', 'Green'), ('Bl', 'Blue'), ('I', 'Indigo'), ('P', 'Purple')], default='B')
    price = IntegerField('Price', [validators.NumberRange(min=1, max=1000), validators.DataRequired()])


class cartPayment(FlaskForm):
    name = StringField("Full Name:", [validators.DataRequired()], default='')
    email = EmailField('Email', [validators.DataRequired(), validators.Email()], default='')
    address = StringField("Address", [validators.DataRequired()], default='')
    city = StringField("City", [validators.DataRequired()], default='')
    payment = SelectField("Payment Method", [validators.DataRequired()], choices=paymentTypes, default='')


class paymentVisa(FlaskForm):
    number = StringField("Card Number:", validators=[validators.DataRequired(), validators.Length(min=16, max=16), validators.Regexp(regex='^4[0-9]{12}(?:[0-9]{3})?$')], default='')
    name = StringField("Card Holder Name:", [validators.DataRequired()], default='')
    month = SelectField("Expiry Month:", [validators.DataRequired()], choices=months())
    year = SelectField("Expiry Year:", [validators.DataRequired()], choices=year())
    security = PasswordField("Security Number (CVV):", validators=[validators.DataRequired(message="Invalid security number"), validators.Length(min=3, max=3)], default='')

    def validate_number(form, number):
        print("Validate number!\n{}".format(number.data[0]))
        if number.data[0] != "4" and number.data.isnumeric():
            print("IT PASSED BRO\n")
            raise ValidationError("Invalid Visa Credit Card Number")


class paymentAE(FlaskForm):
    cardNumber = StringField("Card Number:", validators=[validators.DataRequired(), validators.Length(min=15, max=15), validators.Regexp(regex='^3[47][0-9]{13}$')], default='')
    cardName = StringField("Card Holder Name:", [validators.DataRequired()], default='')
    expiryMonth = SelectField("Expiry Month:", [validators.DataRequired()], choices=months())
    expiryYear = SelectField("Expiry Year:", [validators.DataRequired()], choices=year())
    securityNumber = PasswordField("Security Number (CVV):", [validators.DataRequired(message="Invalid security number"), validators.Length(min=3, max=3)], default='')

    def validate_cardNumber(self, cardNumber):
        number = cardNumber.data
        if (number[0] != "3") and ((number[2] != "4") or (number[2] != "7")) and cardNumber.data.isnumeric():
            raise ValidationError("Invalid American Express Credit Card Number")


class paymentMaster(FlaskForm):
    cardNumber = StringField("Card Number:", [validators.DataRequired(), validators.Length(min=16, max=16), validators.Regexp(regex='^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$')], default='')
    cardName = StringField("Card Holder Name:", [validators.DataRequired()], default='')
    expiryMonth = SelectField("Expiry Month:", [validators.DataRequired()], choices=months())
    expiryYear = SelectField("Expiry Year:", [validators.DataRequired()], choices=year())
    securityNumber = PasswordField("Security Number (CVV):", [validators.DataRequired(message="Invalid security number"), validators.Length(min=3, max=3)], default='')

    def validate_cardNumber(self, cardNumber):
        if (cardNumber.data[0] != "5") and cardNumber.data.isnumeric():
            raise ValidationError("Invalid MasterCard Number")

