from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.coin import Coin
from random import randrange

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def reggie():
    return render_template("register.html")

@app.route('/create_user', methods= ['POST'])
def created():

    if not User.validate(request.form):
        return redirect('/register')
    data = {
        'firstname' : request.form['firstname'],
        'lastname' : request.form['lastname'],
        'email' : request.form['email'],
        "emplid": request.form['emplid']
    }



    x = {'email':request.form['email']}
    checker = User.verify_email(x)
    if checker == False:
        return redirect('/register')

    else:
        y = User.create(data)
        x = User.retrieve_by(data)

        new_data = {
          "user_id": x[0]['id'],
          "balance": randrange(10,70)
          }
        Coin.add_specific(new_data)
        print("THIS IS NEW DATA!!!",new_data)
        flash('Succesfully Added in database', 'success')
        return redirect('/register')

@app.route("/login_page")
def login_page():
    return render_template('login.html')


@app.route('/login', methods = ['POST'])
def logger():
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email", 'login')
        return redirect("/login_page")
    # session['user'] = user_in_db.id
    # session['name'] = f"{user_in_db.firstname} {user_in_db.lastname}"
    # x = session['user']
    return redirect("/login_page")
