from flask import render_template, url_for, request, redirect

from bll.view_functions.login_forms_completion import validate_login_data
import db.models.user as user
import db.db_operations as dal


def start():
    return render_template('base.html')


def registration():
    if request.method == 'POST':
        user_name = request.form.get('username', type=str)
        pwd1 = request.form.get('password', type=str)
        pwd2 = request.form.get('rptd-password', type=str)
        if validate_login_data(user_name, pwd1, pwd2):
            new_user = user.User(username=user_name, password=pwd1)
            dal.create(new_user)
            return redirect('/login/')

        else:
            return render_template('signup-error.html')

    else:
        return render_template('registration.html')


def login():
    if request.method == 'POST':
        user_name = request.form.get('username', type=str)
        pwd = request.form.get('password', type=str)
        if user_name and pwd:
            new_user = user.User(username=user_name, password=pwd)
            dal.create(new_user)

        return redirect('/login/')

    else:
        return render_template('login.html')
