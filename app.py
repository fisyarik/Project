from flask import Flask
from flask import render_template

import sqlite3 

app = Flask(__name__)

connection = sqlite3.connect('my_datebase.db', check_same_thread=False)
cursor = connection.cursor()

# функции для работы с db
def productDB():# возвращаем данные в товары 
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall() # возвращаем данные в list

# контроллер
@app.route('/') #Главная страница
def index():
    shop = productDB()
    return render_template("index.html", shop = shop)

@app.route('/catalog') #Главная страница
def catalog ():
    return render_template("catalog.html")

@app.route('/support') # Обратная связь 
def support():
    return render_template("support.html")

@app.route('/about') # о нас
def about():
    return render_template("about.html")

@app.route('/sale') #скидки и акции
def sale():
    return render_template("sale.html")

@app.route('/news') # новости
def news():
    return render_template("news.html")

@app.route('/user/<username>')
def user_profile(username):
    return render_template("hello.html",name = username)


if __name__ == '__main__': #точка входа программы
    print("привет, мир")
    app.run(debug=True)