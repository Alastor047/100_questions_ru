#pip install psycopg2
```
Определим функцию create_connection() для подключения к базе данных PostgreSQL
```

from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
	connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


```
Подключение осуществляется через интерфейс psycopg2.connect().
Далее используем написанную нами функцию
```

connection = create_connection(
    "postgres", "postgres", "abc123", "127.0.0.1", "5432"
)



```
Теперь внутри дефолтной БД postgres нужно создать базу данных sm_app.
Ниже определена соответствующая функция create_database()
```

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)


```
Запустив вышеприведенный скрипт, мы увидим базу данных sm_app на своем сервере PostgreSQL.
Подключимся к ней
```

connection = create_connection(
    "sm_app", "postgres", "abc123", "127.0.0.1", "5432"
)


```
Здесь 127.0.0.1 и 5432 это соответственно IP-адресу и порт хоста сервера.
```
