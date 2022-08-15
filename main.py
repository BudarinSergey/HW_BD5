
import psycopg2
# conn = psycopg2.connect(database="HW_PG_Py", user="postgres", password="Sergey12")
# with conn.cursor() as cur:
#     cur.execute("""
#         DROP TABLE mob_number;
#         DROP TABLE users;
#         """)
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(20) NOT NULL,
#             surname VARCHAR(20) ,
#             email VARCHAR(30) UNIQUE
#         );
#         """)
#
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS mob_number(
#             id SERIAL PRIMARY KEY,
#             mob_num INTEGER NOT NULL,
#             user_id INTEGER NOT NULL REFERENCES users(id)
#         );
#         """)
#
#     conn.commit()
#
#     cur.execute("""
#         INSERT INTO users(name) VALUES('Sergey') RETURNING id, name;
#         """)
#     print(cur.fetchone())
#         # conn.commit()
#
# conn.close()


def create_bd(conn):
    # conn = psycopg2.connect(database="HW_PG_Py", user="postgres", password="Sergey12")
    with conn.cursor() as cur:
        cur.execute("""
            DROP TABLE mob_number;
            DROP TABLE users;
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(20) NOT NULL,
                surname VARCHAR(20),
                email VARCHAR(30) UNIQUE
            );
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS mob_number(
                id SERIAL PRIMARY KEY,
                mob_num INTEGER NOT NULL,
                user_id INTEGER NOT NULL REFERENCES users(id)
            );
            """)

        conn.commit()

        # cur.execute("""
        #             INSERT INTO users(name) VALUES('Sergey') RETURNING id;
        #             """)
        # print(cur.fetchone())
        # conn.commit()





def add_client(conn):
    name = input("ведите имя : ")
    surname = input("введите фамилию : ")
    email = input("введите e-mail : ")
    with conn.cursor() as cur:

        cur.execute("""
            INSERT INTO users (name, surname,email) VALUES (%s, %s, %s) RETURNING id, name""", (name, surname, email))

        print(cur.fetchone())
        conn.commit()

        # cur.execute(""" SELECT * FROM users;""")

def add_phone(conn):
    userid = input("Введите ID пользователя : ")
    user_number = input("Введите номер телефона : ")
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO mob_number (mob_num, user_id) VALUES (%s, %s) RETURNING mob_num""", (user_number, userid))
        print(cur.fetchone())
        conn.commit()



def change_user(conn):
    userid = input("Введите ID пользователя : ")
    name = input("ведите новое имя : ")
    surname = input("введите новую фамилию : ")
    email = input("введите новый e-mail : ")
    with conn.cursor() as cur:
        cur.execute(""" UPDATE users SET name=%s, surname=%s, email =%s WHERE id=%s; """,(name, surname, email, userid))

        cur.execute("""SELECT * FROM users;
        """)
        print(cur.fetchall())
        conn.commit()

def del_number(conn):
    userid = input("Введите ID пользователя : ")
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM mob_number WHERE id=%s; """,(userid))

        cur.execute("""SELECT * FROM mob_number;
                """)
        print(cur.fetchall())
        conn.commit()

def del_user(conn):
    userid = input("Введите ID пользователя : ")
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM users WHERE id=%s; """,(userid))

        cur.execute("""SELECT * FROM users;
                """)
        print(cur.fetchall())
        conn.commit()

def finde_user(conn):
    finde_param = input("Выберете один из параметры поиска (1 - имя, 2 - фамилия, 3- email, 4 - номер телефона ) : ")
    if finde_param == '1':
        name = input("ведите имя пользователя : ")
        with conn.cursor() as cur:
            cur.execute("""SELECT id,  name, surname, email FROM users WHERE name=%s; """,(name,))
            print(cur.fetchone())
    elif finde_param == '2':
        surname = input("ведите фамилию пользователя : ")
        with conn.cursor() as cur:
            cur.execute("""SELECT id,  name, surname, email FROM users WHERE surname=%s; """, (surname,))
            print(cur.fetchone())
    elif finde_param == '3':
        email = input("ведите email пользователя : ")
        with conn.cursor() as cur:
            cur.execute("""SELECT id,  name, surname, email FROM users WHERE email=%s; """, (email,))
            print(cur.fetchone())

    elif finde_param == '4':
        mob_num1 = input("ведите номер телефона пользователя : ")
        with conn.cursor() as cur:
            cur.execute("""SELECT u.id,  u.name, u.surname, u.email FROM users u
            JOIN mob_number mn ON mn.user_id = u.id
            WHERE mn.mob_num=%s; """, (mob_num1,))
            print(cur.fetchone())
    else:
        print('Вы неправильно задали параметры')


        conn.commit()

with psycopg2.connect(database="HW_PG_Py", user="postgres", password="Sergey12") as conn:
    create_bd(conn)
    add_client(conn)
    add_phone(conn)
    # change_user(conn)
    # del_number(conn)
    # del_user(conn)
    finde_user(conn)

conn.close()