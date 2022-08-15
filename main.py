
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




with psycopg2.connect(database="HW_PG_Py", user="postgres", password="Sergey12") as conn:
    create_bd(conn)
    add_client(conn)
    add_phone(conn)

conn.close()