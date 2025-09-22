from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index ():
    return "Главная страница"

@app.route('/shop')
def shop():
    return "Каталог"

@app.route('/support')
def support():
    return "Поддержка"

@app.route('/about')
def about():
    return "О нас"

@app.route('/sale')
def sale():
    return "Скидки"

@app.route('/news')
def news():
    return "новости"

@app.route('/user/<username>')
def user_profile(username):
    return render_template("hello.html",name = username)


if __name__ == '__main__': #точка входа программы
    print("привет, мир")
    app.run(debug=True)