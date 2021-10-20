# from os import name
from flask import Flask, url_for, render_template, request, redirect, session
from flask_login import login_required, current_user
from flask.templating import render_template_string
import sqlite3
from random import randint
import os


bn = []
app = Flask(__name__)
# app.config['SECRET_KEY'] = '5da316ef2df69ce2131033312fbfc8769040d8ab'

@app.route("/", methods = ["POST", "GET"])
@login_requried
def main():
    if request.method == "POST":
        pass
    if request.method == "GET":
        bn.clear()
        bn.append(randint(1, 20))
        app.secret_key = os.urandom(32)
        return redirect(f"/account/{str(bn[-1])}")
@app.route(f"/account/<string:id>", methods = ["POST", "GET"])
@login_requried
def maims(id):
    session.permanent = False
    return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return flask.abort(400)

#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)
    
if __name__ == "__main__":
    app.run()

# @app.route('/delete-visits/')
# def delete_visits():
#     session.pop('visits', None)  # удаление данных о посещениях
#     return 'Visits deleted'

# app = Flask(__name__)
# rooms = {}
 
# @app.route('/')
# @app.route('/home')
# def index():
#     return render_template('index.html')
 
# @app.route('/create-game', methods = ['POST', 'GET'])
# def create_game():
#     print('DONE')
#     return redirect('/game/12345')
 
# @app.route('/game/<string:id>')
# def about(id):
#     print('smth')
#     return render_template('about.html')
 
# if __name__ == '__main__':
#     app.run(port=1001, debug=True)
