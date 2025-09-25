from flask import Flask
from flask import render_template, request
import sqlite3 

app = Flask(__name__)

connection = sqlite3.connect('my_datebase.db', check_same_thread=False)
cursor = connection.cursor()

# функции для работы с db
def productDB():# возвращаем данные в товары 
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall() # возвращаем данные в list

def product_accessoriesDB(id):
    listDB=cursor.execute('SELECT * FROM product where category="'+id+'"')
    return listDB.fetchall()

def product_oneBD(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()

# контроллер
@app.route('/') #Главная страница
def index():
    shop = productDB()
    return render_template("index.html", shop = shop)

def product_oneDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()


@app.route('/about') # о нас
def about():
    return render_template("about.html")

@app.route("/proba") #Регистрация
def proba():
    return render_template("proba.html")

@app.route("/basket/<id>" )#корзина
def basket(id):
    shop= product_oneDB(id)
    print(shop)
    return render_template('basket.html', shop=shop)

@app.route("/cat/<id>")
def accessories(id):
    shop= product_accessoriesDB(id)
    product_accessoriesDB
    return render_template("accessories.html", shop=shop)

@app.route("/cat/<id>") # мужчины
def men(id):
    shop= product_menDB(id)
    product_menDB
    return render_template("men.html", shop=shop)

@app.route("/cat/<id>")# девушки
def women(id):
    shop= product_womenDB(id)
    product_womenDB
    return render_template("women.html", shop=shop)

@app.route("/search/<id>")#Поиск
def search(id):
    shop= product_oneDB(id)
    print(index)
    return render_template("search.html",shop=shop)

@app.route('/user/<username>')
def user_profile(username):
    return render_template("hello.html",name = username)


if __name__ == '__main__': #точка входа программы
    print("привет, мир")
    app.run(debug=True)