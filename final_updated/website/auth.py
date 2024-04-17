from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   

auth = Blueprint('auth', __name__)

# hospital login and signup

@auth.route('/login-h', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.hospital_dashboard_View'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('main.hospital_dashboard_View'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("loginH.html")


@auth.route('/sign-up-h', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('main.hospital_dashboard_View'))
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        if len(email) < 5:
            flash('Email must be at least 5 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be at least 2 characters.', category='error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', category='error')
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
            else:
                new_user = User(email=email, name=name, password=generate_password_hash(password),role="hospital")
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('main.hospital_dashboard_View'))
    
    return render_template("signupH.html")


# login and signup for patient


@auth.route('/sign-up-p', methods=['GET', 'POST'])
def sign_up_patient():
    if current_user.is_authenticated:
        return redirect(url_for('main.patient_dashboard_View'))
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        if len(email) < 5:
            flash('Email must be at least 5 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be at least 2 characters.', category='error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', category='error')
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
            else:
                new_user = User(email=email, name=name, password=generate_password_hash(password),role="patient")
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('main.patient_dashboard_View'))
    
    return render_template("signupP.html")


@auth.route('/login-p', methods=['GET', 'POST'])
def login_patient():
    if current_user.is_authenticated:
        return redirect(url_for('main.patient_dashboard_View'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('main.patient_dashboard_View'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("loginP.html")


# logout for both hospital and patient

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', category='success')
    return redirect(url_for('main.index_View'))