from flask import Flask, render_template, request,redirect
from form import registration_form
from flask_sqlalchemy import SQLAlchemy
from model import db, User
from flask_wtf.csrf import CsrfProtect
from models.user import User

import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/index')
def hello_world():
    numbers = ["one", "two", "three"]
    word = "some words"
    context = {"some_list": numbers, "word1": word}
    return render_template("index.html", **context)

if __name__ == '__main__':
    app.run()


#database.create_all()



#@app.route('/register', methods=["GET", "POST"])
#def register():
   # form = registration_form()
   # if request.method == "POST":
   #     form = registration_form(request.form)
    #    if form.validate_on_submit():
    #        user = User(None, form.email, form.username, form.password)
     #       database.session.add(user)
     #       database.session.commit()

   #     return redirect('/index')
   # return render_template("register.html", form=form)

#-------------------------------------------------------
#ORM (Object rational mapper) -> SQL -> Mapping -> Python
#ORM = Python -> Mapping -> SQL

# get, post, put
# user -> register -> get(register form from server) -> user files the form ->
# post(filled register form and click submit) -> data goes to server and validates data ->
# Database create user -> if creation is successful activate another method to send a response
# get(send information to user about successful registration)


# MVC -> MODEL VIEW CONTROLLER(PVZ: Intenetine parduotuve)
# Model -> Dalis kuri komunikuoja su duombaze ir biznio logika(PVZ: Modelis bus atsakingas uz vartotojo sasajos ir produktu gavima is duombazes)
# View -> View atsakingas uz reprezentacija vartotojui(front-end)
# Controller -> Kontrolerije turime biznio logika(PVZ: uzsiregistruoti, nupirkti prekes)
# MVT
# Model -> Dalis kuri komunikuoja su duombaze ir biznio logika(PVZ: Modelis bus atsakingas uz vartotojo sasajos ir produktu gavima is duombazes)
# View -> View turime biznio logika(PVZ: uzsiregistruoti, nupirkti prekes)
# Template -> Template atsakingas uz reprezentacija vartotojui(front-end)
#import sqlite3

#def create_user():
 #   query = """SELECT * FROM User"""

 #   connection = sqlite3.connect("parduotuve")
#   cursor = connection.cursor()
#    cursor.execute(query)
#    connection.commit()
 #   connection.close()

#------------------------------------------------------
#def sum(*args):
  #  return args[0] + args[1] * args[2]


#print(sum(5, 10, 10))


#def sum(**kwargs):
 #   return kwargs['pirmas_skaicius'] + kwargs['antras_skaicius'] * kwargs['trecias_skaicius']


#print(sum(pirmas_skaicius=5, antras_skaicius=10, trecias_skaicius=10))


#def funkcija(numeris, numeris2, numeris3):
 #   return numeris + numeris2 * numeris3


#funkcija(5, 10, 10)


