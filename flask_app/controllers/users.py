from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models.user import User
# from flask_app.models.show import Show
# from flask_app.models.liked import Liked

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")


