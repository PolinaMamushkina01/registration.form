import sqlite3

conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect('registered.sqlite')
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    open()
    query = '''DROP TABLE IF EXISTS registered'''
    do(query)
    close()


def create():
    open()
    do('''CREATE TABLE IF NOT EXISTS registered (
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            surname VARCHAR,
            phone VARCHAR,
            email VARCHAR )
    ''')
    close()


def add_person(name, surname, phone, email):
    open()
    query = '''INSERT INTO registered
    (name, surname, phone, email) VALUES (?, ?, ?, ?)'''
    cursor.execute(query, [name, surname, phone, email])
    conn.commit()
    close()


def show_registered():
    open()
    query = '''SELECT * from registered'''
    cursor.execute(query)
    conn.commit()
    data = cursor.fetchall()
    close()
    for person in data:
        print('Имя: ', person[1])
        print('Фамилия: ', person[2])
        print('Телефон: ', person[3])
        print('Почта: ', person[4])
        print('')


def main():
    #clear_db()
    create()
    show_registered()


if __name__ == '__main__':
    main()