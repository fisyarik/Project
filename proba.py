import sqlite3
# Создаем подключение к базе данных (файл называется"my_database.bd)
connection = sqlite3.connect('my_datebase.bd')
# закрытие базы данных 
connection.close

cursor = connection.cursor()

def productDB():
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

if __name__ == '__main__':
    print(productDB())