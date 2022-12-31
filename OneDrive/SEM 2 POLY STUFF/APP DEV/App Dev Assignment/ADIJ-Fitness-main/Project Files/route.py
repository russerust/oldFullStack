from flask import Flask, Blueprint, render_template, request, redirect, session, url_for,flash
from Forms import paymentAE,paymentVisa,paymentMaster,cartPayment,updateItemForm,createItemForm,makeProgramme, UpdateProgrammes, paymentMasterGym,paymentVisaGym,paymentAEGym,CreateUserForm,LoginForm, UpdateUserForm, accountdetail, forgotpassword, searchuser, UpdateBookForm, CreateBookForm, CreateLocation, UpdateLocation
from User import User
from user_service import get_user_list, get_user, save_user, get_user_for_login, exist_email, delete_user_email, get_user_info, user_id,get_user_profile,get_timeline,get_number_user,get_user_gender,get_user_gender_reverse,get_user_type,get_user_type_reverse
from flask import current_app
from programmes import Programme
from programmes_service import prog_list_form,save_prog, get_prog_list, delete_prog, get_prog, update_programme
import os
from comments import Comments
from comments_service import unique_comment_dict,get_comments_list, get_comments, save_comments, delete_comment
from datetime import datetime
from constants import datetime_format, date_format
import matplotlib.pyplot as plt
from booking import Bookings
from booking_service import delete_all_bookings,get_booking_time_updated,get_booking_time_updated_reverse,get_booking_date,get_booking_date_reverse,get_booking_email,get_booking_email_reverse,get_booking_time,get_booking_time_reverse,get_booking_loc,get_booking_loc_reverse,remove_session,get_timebook,get_number_gym, retrieve_booking, retrieve_save_booking, retrieve_delete_booking,get_booking, save_booking, delete_booking, get_booking_list, get_booking_gender, get_booking_gender_reverse, get_activity_reverse, get_activity
from locationTest_service import save_location,get_location_image,get_location_id,update_location,activate_location,location_verify, for_location_form,add_location, get_location_list, del_location, get_location
from location import Location
from manageItem import save_item, get_item_list, get_item, delete_item_id, add_to_cart, list_cart, remove_from_cart, \
    user_cart
from item import Item


app = Flask(__name__)
route = Blueprint('user', __name__)
UPLOAD_FOLDER = 'static/uploads/'
LOCATION_FOLDER = 'static/uploads_location'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LOCATION_FOLDER'] = LOCATION_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@route.route('/Signup', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        email = create_user_form.email.data
        password = create_user_form.password.data
        name = create_user_form.name.data
        gender = create_user_form.gender.data
        birthday = create_user_form.birthday.data
        user_type = create_user_form.user_type.data
        email_verify = exist_email()
        if email.upper() in email_verify:
            error ='Email already Exists!'
            return render_template('createUser.html', form=create_user_form,error=error)
        else:
            user = User(email, password, name, gender,birthday,user_type)
            # print(user)
            save_user(user)
            flash("Account created! Please try logging in.", category='success')
            return redirect(url_for('user.login'))
    if bool(session) != False:
        # print("dfnlsdnflsdnf\n {}".format(session))
        return render_template('home.html')
    else:
        return render_template('createUser.html', form=create_user_form)


@route.route('/Login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    # print(bool(session))
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = login_form.password.data
        user = get_user_for_login(email, password)
        if user is not None:
            session['user_name'] = user.name
            session['user_type'] = user.user_type
            session['user_email'] = user.email
            session['user_gender'] = user.gender
            flash(f"Login success! Welcome {user.name} ",category='success')
            return redirect('/')
        else:
            error = 'Invalid email or password'
            return render_template('login.html', form=login_form, error=error)
    if bool(session) != False:
        # print("dfnlsdnflsdnf\n {}".format(session))
        return render_template('home.html')
    else:
        return render_template('login.html', form=login_form)


@route.route('/retrieveUsers',methods=['GET', 'POST'])#s
def retrieve_users():
    search_user_form = searchuser(request.form)
    if request.method == 'POST' and search_user_form.validate():
        email = search_user_form.email.data
        email_verify = exist_email()
        if email.upper() in email_verify:
            user_list = get_user_profile(email)
            user_name = user_list.name
            user_email = user_list.email
            user_gender = user_list.get_gender_str()
            user_time_updated = user_list.get_time_updated_str()
            user_user_type = user_list.get_user_type_str()
            user_id = user_list.id
            return render_template('searchuser.html',form=search_user_form, user_list=user_list,user_name=user_name,
                                   user_email = user_email, user_gender=user_gender,user_time_updated=user_time_updated,user_user_type=user_user_type,
                                   user_id=user_id)
        else:
            user_list = get_user_list()
            error = 'Email does not exist'
            return render_template('retrieveUsers.html', count=len(user_list), user_list=user_list,form=search_user_form,error=error)
    user_list = get_user_list()
    if bool(session) == False:
        return render_template('home.html')
    if session['user_type'] == 'C':
        return render_template('home.html')
    else:
        return render_template('retrieveUsers.html', count=len(user_list), user_list=user_list,form=search_user_form)


@route.route('/retrieveUsersgender',methods=['GET', 'POST'])#s
def retrieve_users_gender():
    search_user_form = searchuser(request.form)
    if request.method == 'POST' and search_user_form.validate():
        email = search_user_form.email.data
        email_verify = exist_email()
        if email.upper() in email_verify:
            user_list = get_user_profile(email)
            user_name = user_list.name
            user_email = user_list.email
            user_gender = user_list.get_gender_str()
            user_time_updated = user_list.get_time_updated_str()
            user_user_type = user_list.get_user_type_str()
            user_id = user_list.id
            return render_template('searchuser.html',form=search_user_form, user_list=user_list,user_name=user_name,
                                   user_email = user_email, user_gender=user_gender,user_time_updated=user_time_updated,user_user_type=user_user_type,
                                   user_id=user_id)
        else:
            user_list = get_user_gender()
            error = 'Email does not exist'
            return render_template('retrieveusergender.html', count=len(user_list), user_list=user_list,form=search_user_form,error=error)
    user_list = get_user_gender()
    if bool(session) == False:
        return render_template('home.html')
    if session['user_type'] == 'C':
        return render_template('home.html')
    else:
        return render_template('retrieveusergender.html', count=len(user_list), user_list=user_list,form=search_user_form)


@route.route('/retrieveUsersgenderreverse',methods=['GET', 'POST'])#s
def retrieve_users_gender_reverse():
    search_user_form = searchuser(request.form)
    if request.method == 'POST' and search_user_form.validate():
        email = search_user_form.email.data
        email_verify = exist_email()
        if email.upper() in email_verify:
            user_list = get_user_profile(email)
            user_name = user_list.name
            user_email = user_list.email
            user_gender = user_list.get_gender_str()
            user_time_updated = user_list.get_time_updated_str()
            user_user_type = user_list.get_user_type_str()
            user_id = user_list.id
            return render_template('searchuser.html',form=search_user_form, user_list=user_list,user_name=user_name,
                                   user_email = user_email, user_gender=user_gender,user_time_updated=user_time_updated,user_user_type=user_user_type,
                                   user_id=user_id)
        else:
            user_list = get_user_gender_reverse()
            error = 'Email does not exist'
            return render_template('retrieveusergenderreverse.html', count=len(user_list), user_list=user_list,form=search_user_form,error=error)
    user_list = get_user_gender_reverse()
    if bool(session) == False:
        return render_template('home.html')
    if session['user_type'] == 'C':
        return render_template('home.html')
    else:
        return render_template('retrieveusergenderreverse.html', count=len(user_list), user_list=user_list,form=search_user_form)


@route.route('/retrieveUserstype',methods=['GET', 'POST'])#s
def retrieve_users_type():
    search_user_form = searchuser(request.form)
    if request.method == 'POST' and search_user_form.validate():
        email = search_user_form.email.data
        email_verify = exist_email()
        if email.upper() in email_verify:
            user_list = get_user_profile(email)
            user_name = user_list.name
            user_email = user_list.email
            user_gender = user_list.get_gender_str()
            user_time_updated = user_list.get_time_updated_str()
            user_user_type = user_list.get_user_type_str()
            user_id = user_list.id
            return render_template('searchuser.html',form=search_user_form, user_list=user_list,user_name=user_name,
                                   user_email = user_email, user_gender=user_gender,user_time_updated=user_time_updated,user_user_type=user_user_type,
                                   user_id=user_id)
        else:
            user_list = get_user_type()
            error = 'Email does not exist'
            return render_template('retrieveusertype.html', count=len(user_list), user_list=user_list,form=search_user_form,error=error)
    user_list = get_user_type()
    if bool(session) == False:
        return render_template('home.html')
    if session['user_type'] == 'C':
        return render_template('home.html')
    else:
        return render_template('retrieveusertype.html', count=len(user_list), user_list=user_list,form=search_user_form)


@route.route('/retrieveUserstypereverse',methods=['GET', 'POST'])#s
def retrieve_users_type_reverse():
    search_user_form = searchuser(request.form)
    if request.method == 'POST' and search_user_form.validate():
        email = search_user_form.email.data
        email_verify = exist_email()
        if email.upper() in email_verify:
            user_list = get_user_profile(email)
            user_name = user_list.name
            user_email = user_list.email
            user_gender = user_list.get_gender_str()
            user_time_updated = user_list.get_time_updated_str()
            user_user_type = user_list.get_user_type_str()
            user_id = user_list.id
            return render_template('searchuser.html',form=search_user_form, user_list=user_list,user_name=user_name,
                                   user_email = user_email, user_gender=user_gender,user_time_updated=user_time_updated,user_user_type=user_user_type,
                                   user_id=user_id)
        else:
            user_list = get_user_type_reverse()
            error = 'Email does not exist'
            return render_template('retrieveusertypereverse.html', count=len(user_list), user_list=user_list,form=search_user_form,error=error)
    user_list = get_user_type_reverse()
    if bool(session) == False:
        return render_template('home.html')
    if session['user_type'] == 'C':
        return render_template('home.html')
    else:
        return render_template('retrieveusertypereverse.html', count=len(user_list), user_list=user_list,form=search_user_form)


@route.route('/updateUser/<id>', methods=['GET', 'POST'])#s
def update_user(id):
    user = get_user(id)
    update_user_form = UpdateUserForm(request.form)
    originalEmail = user.email
    if request.method == 'POST' and update_user_form.validate():
        user.email = update_user_form.email.data
        user.name = update_user_form.name.data
        user.gender = update_user_form.gender.data
        user.birthday = update_user_form.birthday.data
        user.user_type = update_user_form.user_type.data

        uploaded_file = request.files['image_file']
        if uploaded_file.filename != '':
            new_filename = f'{user.id}.jpg'
            uploaded_file.save(
                os.path.join(os.path.dirname(current_app.instance_path),
                             "static\\image\\profile", new_filename))
            user.profile_image = new_filename

        # print(user)
        save_user(user)
        return redirect('/retrieveUsers')
    else:
        update_user_form.email.data = user.email
        update_user_form.name.data = user.name
        update_user_form.gender.data = user.gender
        update_user_form.birthday.data = user.birthday
        update_user_form.user_type.data = user.user_type
        if user.id == '99b7c08d-2742-410f-bc42-41efadfe130e':
            return redirect('/retrieveUsers')
        if bool(session) == False:
            return render_template('home.html')
        if session['user_type'] == 'C':
            return render_template('home.html')
        else:
            return render_template('updateUsers.html', form=update_user_form, user=user)


@route.route('/updateUserProfile/<id>', methods=['GET', 'POST'])#mutual
def update_user_profile(id):
    if 'activity' in session:
        remove_session()
    if bool(session) == False:
            return render_template('home.html')
    user = get_user(id)
    update_user_form = UpdateUserForm(request.form)
    originalEmail = user.email
    if request.method == 'POST' and update_user_form.validate():
        user.email = update_user_form.email.data
        user.name = update_user_form.name.data
        user.gender = update_user_form.gender.data
        user.birthday = update_user_form.birthday.data

        uploaded_file = request.files['image_file']
        if uploaded_file.filename != '':
            new_filename = f'{user.id}.jpg'
            uploaded_file.save(
                os.path.join(os.path.dirname(current_app.instance_path),
                             "static\\image\\profile", new_filename))
            user.profile_image = new_filename


        # print(user)
        save_user(user)
        return redirect('/userprofile')
    else:
        update_user_form.email.data = user.email
        update_user_form.name.data = user.name
        update_user_form.gender.data = user.gender
        update_user_form.birthday.data = user.birthday
        email = session['user_email']
        if email == user.email:
            return render_template('updateuserprofile.html', form=update_user_form, user=user)
        else:
            return render_template('home.html')


@route.route('/deleteUser/<id>', methods=['POST'])#s
def delete_user(id):
    user = get_user(id)
    user.status = User.status_deleted
    #user.email = None
    save_user(user)
    delete_user_email(id)
    delete_all_bookings(user.email)
    # print("delete user:\n{}".format(id))
    if session['user_email'] == user.email:
        session.pop('user_name', None)
        session.pop('user_type', None)
        session.pop('csrf_token', None)
        session.pop('user_email', None)
        session.pop('user_gender', None)
        flash('Your account has been deleted.', category='success')
        return redirect('/')
    else:
        return redirect('/retrieveUsers')


@route.route('/deleteUserprofile/<id>', methods=['POST'])#s
def delete_user_profile(id):
    user = get_user(id)
    user.status = User.status_deleted
    #user.email = None
    save_user(user)
    delete_user_email(id)
    delete_all_bookings(user.email)
    if session['user_type'] == 'C' or 'S':
        session.pop('user_name', None)
        session.pop('user_type', None)
        session.pop('csrf_token', None)
        session.pop('user_email', None)
        session.pop('user_gender', None)
        flash('Your account has been deleted.', category='success')
        return redirect('/')
    else:
        return redirect('/retrieveUsers')

@route.route('/logout')
def logout():
    if 'activity' in session:
        remove_session()
    if bool(session) != False:
        session.pop('user_name', None)
        session.pop('user_type', None)
        session.pop('user_gender', None)
        session.pop('csrf_token', None)
        session.pop('user_email', None)
        flash('You have been logged out.', category='success')
        return redirect('/')
    else:
        return redirect('/')


@route.route('/accountdetails', methods=['GET', 'POST'])
def account_details():
    if bool(session) == True:
        return render_template('home.html')
    input_user_form = accountdetail(request.form)
    if request.method == 'POST' and input_user_form.validate():
        email = input_user_form.email.data
        name = input_user_form.name.data
        birthday = input_user_form.birthday.data
        info = get_user_info(email,name,birthday)
        if info is not None:
            info_id = user_id(email,name,birthday)
            user = get_user(info_id)
            user.password = input_user_form.password.data
            save_user(user)
            flash("Password Changed! Please try logging in.", category='success')
            return redirect(url_for('user.login'))
        else:
            error = 'Invalid Email,Name or Birthday'
            return render_template('accountdetails.html',form=input_user_form,error=error)

    return render_template('accountdetails.html', form=input_user_form)


@route.route('/forgotpassword/<id>', methods=['GET', 'POST']) # Mutual
def forgot_password(id):
    user = get_user(id)
    forgot_password_form = forgotpassword(request.form)
    if request.method == 'POST' and forgot_password_form.validate():
        old_password = forgot_password_form.old_password.data
        new_password = forgot_password_form.new_password.data
        if user.password == old_password:
            if new_password == old_password:
                error = 'Please enter a password different from old password'
                return render_template('forgotpassword.html', form=forgot_password_form, error=error)
            else:
               user.password = new_password
               save_user(user)
               flash('Password changed! successfully')
               return redirect('/userprofile')
        else:
            error ='Invalid old password'
            return render_template('forgotpassword.html', form=forgot_password_form, error=error)
    if bool(session) == False:
        return render_template('home.html')
    email = session['user_email']
    if email == user.email:
        return render_template('forgotpassword.html', form=forgot_password_form)
    else:
        return render_template('home.html')


@route.route('/userprofile', methods=['GET', 'POST'])
def user_profile():
    if 'activity' in session:
        remove_session()
    if bool(session) == False:
        return render_template('home.html')
    email = session['user_email']
    user_list = get_user_profile(email)
    user_name = user_list.name
    user_id = user_list.id
    user_email = user_list.email
    user_gender = user_list.gender
    user_birthday = user_list.birthday
    user_user_type = user_list.user_type
    user_time_created = user_list.get_time_created_str()
    user_time_updated = user_list.get_time_updated_str()
    user_profile_image = user_list.profile_image
    return render_template('userProfile.html',user_list=user_list,user_name=user_name, user_id=user_id, user_email=user_email,
                           user_gender=user_gender, user_birthday=user_birthday, user_user_type=user_user_type, user_time_created=user_time_created,
                           user_time_updated=user_time_updated,user_profile_image=user_profile_image)

@route.route('/userchart')#s
def user_chart():
    if bool(session) == False:
        return render_template('home.html')
    if session['user_type'] == 'S':
        timeline = get_timeline()
        user_list = get_number_user()
        plt.plot(timeline, user_list)
        plt.title('User Sign up Chart')
        plt.xlabel('Date')
        plt.ylabel('number of accounts signed')
        plt.show()
        return redirect('/retrieveUsers')
    else:
        return render_template('home.html')


@route.route('/bookings', methods=['GET', 'POST'])
def create_booking():
    if 'activity' in session:
        remove_session()
    if 'user_type' not in session:
        flash("Please login before trying to book!", category="error")
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        user_list = get_booking_list()
        locations = for_location_form()
        programmes = get_prog_list()
        count = 0
        return render_template('bookings.html', user_list=user_list, count=len(user_list), loc=locations, prog_list=programmes, tcount=count)


# Payment of Booking [James]
@route.route('/paymentVisa', methods=['GET', 'POST'])
def payment_visa():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    elif 'date' not in session:
        return render_template('home.html')
    else:
        update_user_form = paymentVisaGym()
        location_name = get_location(session['location_id'])
        location_image = get_location_image(session['location_id'])
        activity = session['activity']
        prog_list = get_prog_list()
        if update_user_form.validate_on_submit():
            temp = datetime.strptime(session['date'], '%a, %d %b %Y %H:%M:%S %Z').date()
            session['date'] = temp.strftime(date_format)
            booking = Bookings(session['user_email'], session['activity'], session['date'], session['location'], session['time'], session['user_gender'], session['payment'])
            save_booking(booking)
            session.pop('activity')
            session.pop('date')
            session.pop('location')
            session.pop('location_id')
            session.pop('time')
            session.pop('payment')
            flash("Booking successful!")
            return redirect('/bookings')
        return render_template('bookingVisa.html', prog_list = prog_list,activity = activity, form=update_user_form, location_name = location_name, location_image = location_image)


@route.route('/paymentMaster', methods=['GET', 'POST'])
def payment_master():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    elif 'date' not in session:
        return render_template('home.html')
    else:
        update_user_form = paymentMasterGym()
        location_name = get_location(session['location_id'])
        location_image = get_location_image(session['location_id'])
        activity = session['activity']
        prog_list = get_prog_list()
        if update_user_form.validate_on_submit():
            temp = datetime.strptime(session['date'], '%a, %d %b %Y %H:%M:%S %Z').date()
            session['date'] = temp.strftime(date_format)
            booking = Bookings(session['user_email'], session['activity'], session['date'], session['location'], session['time'], session['user_gender'], session['payment'])
            save_booking(booking)
            session.pop('activity')
            session.pop('date')
            session.pop('location')
            session.pop('location_id')
            session.pop('time')
            session.pop('payment')
            flash("Booking successful!")
            return redirect('/bookings')
        return render_template('bookingMaster.html', prog_list = prog_list,activity = activity, form=update_user_form, location_name = location_name, location_image = location_image)


@route.route('/paymentAE', methods=['GET', 'POST'])
def payment_ae():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    elif 'date' not in session:
        return render_template('home.html')
    else:
        update_user_form = paymentAEGym()
        location_name = get_location(session['location_id'])
        location_image = get_location_image(session['location_id'])
        activity = session['activity']
        prog_list = get_prog_list()
        if update_user_form.validate_on_submit():
            temp = datetime.strptime(session['date'], '%a, %d %b %Y %H:%M:%S %Z').date()
            session['date'] = temp.strftime(date_format)
            booking = Bookings(session['user_email'], session['activity'], session['date'], session['location'], session['time'], session['user_gender'], session['payment'])
            save_booking(booking)
            session.pop('activity')
            session.pop('date')
            session.pop('location')
            session.pop('location_id')
            session.pop('time')
            session.pop('payment')
            flash("Booking successful!")
            return redirect('/bookings')
        return render_template('bookingAE.html', prog_list = prog_list,activity = activity,form=update_user_form, location_name=location_name, location_image=location_image)


# Retrieval booking
@route.route('/retrieveBooking', methods=['GET', 'POST'])
def create_bookingR():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_time_updated()
        locations = for_location_form()
        # print("Locations:\n{}\n".format(locations))
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBooking.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingReverse', methods=['GET', 'POST'])
def create_bookingReverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_time_updated_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)



@route.route('/retrieveBookingGender',methods=['GET', 'POST'])
def retrieve_booking_gender():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_gender()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingGender.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingGenderReverse',methods=['GET', 'POST'])
def retrieve_booking_gender_reverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_gender_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingGenderReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingActivity',methods=['GET', 'POST'])
def retrieve_booking_activity():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_activity()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingActivity.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingDate', methods=['GET', 'POST'])
def retrieve_booking_date():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_date()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingDate.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingDateReverse', methods=['GET', 'POST'])
def retrieve_booking_date_reverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_date_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingDateReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingActivityReverse',methods=['GET', 'POST'])
def retrieve_booking_activity_reverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_activity_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingActivityReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingLocationReverse',methods=['GET', 'POST'])
def retrieve_booking_location_reverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_loc_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingLocationReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingLocation',methods=['GET', 'POST'])
def retrieve_booking_location():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_loc()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingLocation.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingTimeReverse',methods=['GET', 'POST'])
def retrieve_booking_time_reverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_time_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingTimeReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingTime',methods=['GET', 'POST'])
def retrieve_booking_time():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_time()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingTime.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingEmail',methods=['GET', 'POST'])
def retrieve_booking_email():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_email()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingEmail.html', user_list=user_list, count=count, loc=locations, liz=listed)


@route.route('/retrieveBookingEmailReverse',methods=['GET', 'POST'])
def retrieve_booking_email_reverse():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        user_list, listed = get_booking_email_reverse()
        locations = for_location_form()
        count = 0
        for key, value in user_list.items():
            for id, booking in value.items():
                count += 1
        return render_template('retrieveBookingEmailReverse.html', user_list=user_list, count=count, loc=locations, liz=listed)



# Admin Update Booking
@route.route('/updateBookingR/<id>', methods=['GET', 'POST'])
def update_bookingR(id):
    if 'user_type' not in session:
        return render_template('home.html')
    if session['user_type'] == "C":
        return render_template('home.html')
    else:
        booking = retrieve_booking(id)
        update_user_form = UpdateBookForm()
        update_user_form.location.choices = for_location_form()
        if update_user_form.validate_on_submit():
            booking.date = update_user_form.date.data.strftime(date_format)
            booking.location = update_user_form.location.data
            booking.time = update_user_form.time.data
            retrieve_save_booking(booking)
            flash("Booking updated successfully!", category='success')
            return redirect('/retrieveBooking')
        else:
            # print("[UpdateBookForm] choices:\n{}".format(get_location_list()))
            temp = datetime.strptime(booking.date, date_format)
            update_user_form.date.data = temp
            update_user_form.location.data = booking.location
            update_user_form.time.data = booking.time
            return render_template('updateBookingR.html', form=update_user_form)


# User update booking
@route.route('/updateBooking/<id>', methods=['GET', 'POST'])
def update_booking(id):
    if 'activity' in session:
        remove_session()
    if 'user_type' not in session:
        return render_template('home.html')
    if session['user_type'] == "S":
        return render_template('home.html')
    else:
        booking = get_booking(id)
        update_user_form = UpdateBookForm()
        update_user_form.location.choices = for_location_form()
        if update_user_form.validate_on_submit():
            booking.date = update_user_form.date.data
            booking.location = update_user_form.location.data
            booking.time = update_user_form.time.data
            temp = update_user_form.date.data.strftime(date_format)
            booking.date = temp
            save_booking(booking)
            flash("Booking updated successfully!", category='success')
            return redirect('/bookings')
        else:
            temp = datetime.strptime(booking.date, date_format)
            update_user_form.date.data = temp
            update_user_form.location.data = booking.location
            update_user_form.time.data = booking.time
            return render_template('bookingUpdate.html', form=update_user_form)


@route.route('/bookingGym',  methods=['GET', 'POST'])
def booking_gym():
    if 'activity' in session:
        remove_session()
    if 'user_type' not in session:
        flash("Please login before trying to book!", category="error")
        return render_template('home.html')
    if session['user_type'] == "S":
        return render_template('home.html')
    else:
        create_user_form = CreateBookForm()
        create_user_form.location.choices = for_location_form()
        create_user_form.activity.choices = prog_list_form()
        if create_user_form.validate_on_submit():
            session['activity'] = create_user_form.activity.data
            session['time'] = create_user_form.time.data
            session['location'] = create_user_form.location.data
            session['location_id'] = get_location_id(str(session['location']))
            session['date'] = create_user_form.date.data
            session['payment'] = create_user_form.payment.data
            if create_user_form.payment.data == "Visa":
                session['payment'] = create_user_form.payment.data
                return redirect('/paymentVisa')
            if create_user_form.payment.data == "MasterCard":
                session['payment'] = create_user_form.payment.data
                return redirect('/paymentMaster')
            if create_user_form.payment.data == "American Express":
                session['payment'] = create_user_form.payment.data
                return redirect('/paymentAE')
        return render_template('bookingGym.html', form=create_user_form)


@route.route('/deleteBooking/<id>', methods=['POST'])
def delete_book(id):
    if 'activity' in session:
        remove_session()
    if 'user_type' not in session:
        return render_template('home.html')
    if session['user_type'] == "S":
        return render_template('home.html')
    else:
        delete_booking(id)
        return redirect('/bookings')


# Retrieval of Booking
@route.route('/deleteBookingR/<id>', methods=['POST'])
def delete_bookR(id):
    if 'activity' in session:
        remove_session()
    if 'user_type' not in session:
        return render_template('home.html')
    if session['user_type'] == "C":
        return render_template('home.html')
    else:
        # print("Deleted booking ID:\n{}\n".format(id))
        retrieve_delete_booking(id)
        return redirect('/retrieveBooking')


# James' Chart for booking

@route.route('/bookingchart')
def book_chart():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        timeline = get_timebook()
        gym_list = get_number_gym()
        plt.plot(timeline, gym_list)
        plt.title('Booking chart')
        plt.xlabel('Date')
        plt.ylabel('Booking sign up rate')
        plt.show()
        return redirect('/retrieveBooking')




# James' Managing locations
@route.route('/manageLocations',  methods=['GET', 'POST'])
def manage_locations():
    if 'user_type' not in session:
        return render_template('home.html')
    if session['user_type'] == "C":
        return render_template('home.html')
    else:
        locations = get_location_list()
        return render_template('manageLocations.html', loc=locations,count=len(locations))


@route.route('/addLocation',  methods=['GET', 'POST'])
def adding_location():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        create_user_form = CreateLocation(request.form)
        if request.method == 'POST' and create_user_form.validate():
            location = create_user_form.location.data
            if location_verify(location) == "new":
                image = request.files['file'].filename
                request.files['file'].save(os.path.join(app.config['LOCATION_FOLDER'], request.files['file'].filename))
                loc = Location(location, image)
                add_location(loc)
                flash("Location added successfully!", category='success')
                return redirect(url_for('user.manage_locations'))
            elif location_verify(location) == "activate":
                activate_location(location)
                return redirect(url_for('user.manage_locations'))
            else:
                error = "Location already exists!"
                return render_template('addLocation.html', form=create_user_form, error=error)
        return render_template('addLocation.html', form=create_user_form)


@route.route('/updateLocation/<id>',  methods=['GET', 'POST'])
def update_locations(id):
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        loc = get_location(id)
        print(loc)
        create_user_form = UpdateLocation(request.form)
        if request.method == 'POST' and create_user_form.validate():
            # del_location(id)
            loc.location = create_user_form.location.data

            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                new_filename = f'{loc.id}.jpg'
                uploaded_file.save(
                    os.path.join(os.path.dirname(current_app.instance_path),
                                 "static\\uploads_location", new_filename))
                loc.image = new_filename

            save_location(loc)
            flash("Location updated successfully!", category='success')
            return redirect(url_for('user.manage_locations'))
        else:
            create_user_form.location.data = loc.location
            return render_template('updateLocation.html', form=create_user_form, loc = loc)


@route.route('/deleteLocation/<id>',  methods=['GET', 'POST'])
def delete_locations(id):
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        del_location(id)
        return redirect('/manageLocations')

# Daniel's programmes


@route.route('/createProgrammes', methods=['GET', 'POST'])
def make_programmes():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        make_programmes_form = makeProgramme(request.form)
        if request.method == 'POST' and make_programmes_form.validate():
            image = request.files['file'].filename
            request.files['file'].save(os.path.join(app.config['UPLOAD_FOLDER'], request.files['file'].filename))
            title = make_programmes_form.title.data
            description = make_programmes_form.description.data
            Prog1 = Programme(title, description, image)
            save_prog(Prog1)
            return redirect('/retrieveProgrammes')
        return render_template('createProgrammes.html', form=make_programmes_form)


@route.route('/retrieveProgrammes', methods=['GET', 'POST'])
def retrieve_programmes():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        prog_list = get_prog_list()
        return render_template('/retrieveProgrammes.html', prog_list=prog_list)


@route.route('/deleteProg/<title>', methods=['POST'])
def del_prog(title):
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        prog = get_prog(title)
        save_prog(prog)
        delete_prog(title)
        return redirect('/retrieveProgrammes')


@route.route('/updateProg/<title>', methods=['GET', 'POST'])
def update_prog(title):
    if 'user_type' not in session:
        return render_template('home.html')

    elif session['user_type'] == "C":
        return render_template('home.html')

    else:
        # print(title)
        prog = get_prog(title)
        update_form = UpdateProgrammes(request.form)
        if request.method == 'POST' and update_form.validate():
            prog.title = update_form.title.data
            prog.desc = update_form.description.data
            if request.files['file'].filename != '':
                prog.image = request.files['file'].filename
                request.files['file'].save(os.path.join(app.config['UPLOAD_FOLDER'], request.files['file'].filename))
            update_programme(prog.title, prog.desc, prog.image, prog.id)
            flash("Location updated successfully!", category='success')
            return redirect('/retrieveProgrammes')
        else:
            update_form.title.data = prog.title
            update_form.description.data = prog.desc
            return render_template('updateProgrammes.html', form=update_form)


@route.route('/create-comment/<prog_id>', methods=['POST'])
def create_comment(prog_id):
    if 'user_email' not in session:
        flash("Please log in before trying to comment!", category="error")
        return redirect('/Login')
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty!')
    else:
        prog = get_prog(prog_id)

        if prog:
            username = session["user_name"]
            comment = Comments(text, username, prog_id)
            save_comments(comment)
        else:
            flash('Post does not exists!')

    return redirect('/programmes')

@route.route('/delete-comment/<comment_id>', methods=['GET', 'POST'])
def del_comment(comment_id):
    # comment = get_comments(comment_id)
    # save_comments(comment)
    if 'user_name' in session:
        current_user = session['user_name']
        if current_user != get_comments(comment_id).author:
            flash("You cannot delete this comment", category="error")
            return redirect('/programmes')
        else:
            delete_comment(comment_id)
            return redirect('/programmes')
    else:
        flash("Please log in first", category="error")
        return redirect("/Login")



@route.route('/programmes', methods=['GET', 'POST'])
def display_prog1():
    if 'user_type' in session:
        if session['user_type'] == "S":
            return render_template('home.html')
        else:
            # print("DISPLAY")
            comment_list, comment_id_list = get_comments_list(), sorted([i.post for i in get_comments_list()])
            prog_list, prog_id_list = get_prog_list(), sorted([i.id for i in get_prog_list()])
            prog_comment_count = unique_comment_dict(comment_id_list, prog_id_list)

            # print("List of Prog IDs: {}".format(prog_id_list))
            # print("List of Comments under each Prog IDs: {}".format(comment_id_list))
            # print("Dict count of Comments under each Prog IDs: {}".format(prog_comment_count))

            return render_template('/programmes.html', prog_list=prog_list, comment_list=comment_list,
                                   comment_length=list(comment_list), prog_length=list(prog_list),
                                   prog_comment_count=prog_comment_count)

    else:
        # print("DISPLAY")
        comment_list, comment_id_list = get_comments_list(), sorted([i.post for i in get_comments_list()])
        prog_list, prog_id_list = get_prog_list(), sorted([i.id for i in get_prog_list()])
        prog_comment_count = unique_comment_dict(comment_id_list, prog_id_list)

        # print("List of Prog IDs: {}".format(prog_id_list))
        # print("List of Comments under each Prog IDs: {}".format(comment_id_list))
        # print("Dict count of Comments under each Prog IDs: {}".format(prog_comment_count))

        return render_template('/programmes.html', prog_list=prog_list, comment_list=comment_list,
                               comment_length=list(comment_list), prog_length=list(prog_list),
                               prog_comment_count=prog_comment_count)


# Ivan's shop
@route.route('/createItem', methods=['GET', 'POST'])
def create_item():
    if 'user_email' not in session:
        flash("Please log in first!", category="error")
        return redirect('/Login')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:

        create_item_form = createItemForm(request.form)
        if request.method == 'POST' and create_item_form.validate():
            brand = create_item_form.brand.data
            product = create_item_form.product.data
            color = create_item_form.color.data
            size = create_item_form.size.data
            price = create_item_form.price.data

            if get_item('') is not None:
                error = 'Item already Exists!'
                return render_template('createItem.html', form=create_item_form, error=error)
            else:
                item = Item(brand, product, color, size, price)
                save_item(item)
                flash("Product created", category='success')
                return redirect('/retrieveItem')
        return render_template('createItem.html', form=create_item_form)


@route.route('/retrieveItem')
def retrieve_items():
    if 'user_email' not in session:
        flash("Please log in first!", category="error")
        return redirect('/Login')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        item_list = get_item_list()
        return render_template('retrieveItem.html', count=len(item_list), item_list=item_list)


@route.route('/updateItem/<id>', methods=['GET', 'POST'])
def update_item_detail(id):
    if 'user_email' not in session:
        flash("Please log in first!", category="error")
        return redirect('/Login')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        item = get_item(id)
        update_item_form = updateItemForm(request.form)
        if request.method == 'POST' and update_item_form.validate():

            item.brand = update_item_form.brand.data
            item.product = update_item_form.product.data
            item.color = update_item_form.color.data
            item.size = update_item_form.size.data
            item.price = update_item_form.price.data
            save_item(item)
            return redirect('/retrieveItem')
        else:
            update_item_form.brand.data = item.brand
            update_item_form.product.data = item.product
            update_item_form.color.data = item.color
            update_item_form.size.data = item.size
            update_item_form.price.data = item.price
            return render_template('updateItem.html', form=update_item_form)


@route.route('/deleteItem/<id>', methods=['POST'])
def delete_item(id):
    if 'user_email' not in session:
        flash("Please log in first!", category="error")
        return redirect('/Login')
    elif session['user_type'] == "C":
        return render_template('home.html')
    else:
        item = get_item(id)
        item.status = Item.status_deleted
        save_item(item)
        delete_item_id(id)
        return redirect('/retrieveItem')


@route.route('/addItem/<id>')
def add_item(id):
    if 'user_email' not in session:
        flash("Please log in first!", category="error")
        return redirect('/Login')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        email = session['user_email']
        item = get_item(id)
        add_to_cart(email, item)
        return redirect('/cart')


@route.route('/api/cart/delete/<id>')
def del_item(id):
    if 'user_type' not in session:
        flash("Please log in first!", category="error")
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        email = session['user_email']
        user_cart(email)
        item = get_item(id)
        remove_from_cart(id, item)
        return redirect('/cart')


@route.route('/check/')
def check():
    if 'user_type' not in session:
        flash("Please log in first!", category="error")
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        email = session['user_email']
        items = list_cart(email)
        sumation = 0
        for x in items:
            sumation += x.price * x.count
        return render_template('checkOut.html', items=items, sumation=sumation)


@route.route('/successful/')
def successful():
    if 'user_type' not in session:
        flash("Please log in first!", category="error")
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        email = session['user_email']
        items = list_cart(email)
        return render_template('successful.html')


@route.route('/receipt/')
def receipt():
    if 'user_type' not in session:
        flash("Please log in first!", category="error")
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        email = session['user_email']
        items = list_cart(email)
        return render_template('receipt.html', items=items)


# Payment
@route.route('/payment/', methods=['GET', 'POST'])
def payment():
    if 'user_type' not in session:
        flash("Please log in first!", category="error")
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        form = cartPayment()
        email = session['user_email']
        items = list_cart(email)
        sumation = 0
        for x in items:
            sumation += x.price * x.count
        if form.validate_on_submit():
            if form.payment.data == "Visa":
                return redirect('/cartVisa')
            if form.payment.data == "MasterCard":
                return redirect('/cartMaster')
            if form.payment.data == "American Express":
                return redirect('/cartAE')
        return render_template('payment.html', items=items, sumation=sumation, form=form)


@route.route('/single/<id>', methods=['GET', 'POST'])
def single(id):
    if 'user_email' not in session:
        flash("Please log in before trying to purchase!", category="error")
        return redirect('/Login')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        email = session['user_email']
        item = get_item(id)
        price = item.price * 1
        form = cartPayment()
        if form.validate_on_submit():
            if form.payment.data == "Visa":
                session['single'] = id
                return redirect('/cartVisa')
            if form.payment.data == "MasterCard":
                session['single'] = id
                return redirect('/cartMaster')
            if form.payment.data == "American Express":
                session['single'] = id
                return redirect('/cartAE')
        return render_template('singleItem.html', item=item, price=price, form=form)


@route.route('/cartVisa', methods=['GET', 'POST'])
def cart_visa():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        if 'single' in session:
            id = session['single']
            item = get_item(id)
            price = item.price * 1
            session.pop('single')
        else:
            email = session['user_email']
            items = list_cart(email)
            price = 0
            for x in items:
                price += x.price * x.count
        update_user_form = paymentVisa()
        if update_user_form.validate_on_submit():
            return redirect('/successful/')
        return render_template('paymentVisa.html', form=update_user_form, price=price)


@route.route('/cartMaster', methods=['GET', 'POST'])
def cart_master():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        if 'single' in session:
            id = session['single']
            item = get_item(id)
            price = item.price * 1
            session.pop('single')
        else:
            email = session['user_email']
            items = list_cart(email)
            price = 0
            for x in items:
                price += x.price * x.count
        update_user_form = paymentMaster()
        if update_user_form.validate_on_submit():
            return redirect('/successful/')
        return render_template('paymentMaster.html', form=update_user_form, price=price)


@route.route('/cartAE', methods=['GET', 'POST'])
def cart_ae():
    if 'user_type' not in session:
        return render_template('home.html')
    elif session['user_type'] == "S":
        return render_template('home.html')
    else:
        if 'single' in session:
            id = session['single']
            item = get_item(id)
            price = item.price * 1
            session.pop('single')
        else:
            email = session['user_email']
            items = list_cart(email)
            price = 0
            for x in items:
                price += x.price * x.count
        update_user_form = paymentAE()
        if update_user_form.validate_on_submit():
            return redirect('/successful/')
        return render_template('paymentAE.html', form=update_user_form, price=price)


@route.route('/shopUI')
def shop():
    item_list = get_item_list()
    return render_template('shopUI.html', count=len(item_list), item_list=item_list)


@route.route('/cart')
def cart():
    if 'user_email' not in session:
        flash("Please log in before trying to purchase!", category="error")
        return redirect('/Login')
    email = session['user_email']
    items = list_cart(email)
    return render_template('cart.html', items=items)
