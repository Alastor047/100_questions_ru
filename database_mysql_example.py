#pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")


```
В приведенном выше коде мы определили новую функцию create_connection(), которая принимает три параметра:
host_name
user_name
user_password

Модуль mysql.connector определяет метод connect(), используемый в седьмой строке для подключения к серверу MySQL.
Как только соединение установлено, объект connection возвращается вызывающей функции.
В последней строке функция create_connection() вызывается с именем хоста, именем пользователя и паролем.

Пока мы только установили соединение. Самой базы ещё нет. Для этого мы определим другую функцию – create_database(),
которая принимает два параметра:
1.Объект connection;
2.query – строковый запрос о создании базу данных.
Вот как выглядит эта функция
```


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


```
Для выполнения запросов используется объект cursor.
Создадим базу данных sm_appдля нашего приложения на сервере MySQL
```

create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)


```
Теперь у нас есть база данных на сервере.
Однако объект connection, возвращаемый функцией create_connection() подключен к серверу MySQL.
А нам необходимо подключиться к базе данных sm_app.
Для этого нужно изменить create_connection() следующим образом
```


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


```
Функция create_connection() теперь принимает дополнительный параметр с именем db_name.
Этот параметр указывает имя БД, к которой мы хотим подключиться
Имя теперь можно передать при вызове функции.
```

connection = create_connection("localhost", "root", "", "sm_app")

```
Скрипт успешно вызывает create_connection() и подключается к базе данных sm_app
```
