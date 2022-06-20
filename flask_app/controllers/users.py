from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
# from flask_app.models.show import Show
# from flask_app.models.liked import Liked

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
        flash('Succesfully Added in database', 'success')
        return redirect('/register')