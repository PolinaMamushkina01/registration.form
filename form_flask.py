from flask import Flask, request, redirect, url_for, render_template
from flask_mail import Mail, Message
from form_sql import add_person

import os


def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        add_person(name, surname, phone, email)
        print('Данные зарегистрировавшегося пользователя:\n' + \
        name + '\n' + surname + '\n' + phone + '\n' + email)
        return redirect(url_for('thanks'))


def thanks():
    return render_template('thanks.html')


folder = os.getcwd()

app = Flask(__name__, template_folder=folder, static_folder=folder)

mail = Mail(app)

app.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
app.add_url_rule('/index', 'index', index, methods=['POST', 'GET'])
app.add_url_rule('/thanks', 'thanks', thanks)

if __name__ == '__main__':
    app.run()


'''
msg = Message('Регистрация в форме', sender='polinamamushkina@yandex.ru', recipients=['umamushkina@yandex.ru'])
msg.body = 'Данные зарегистрировавшегося пользователя:\n' + name + '\n' + surname + '\n' + phone + '\n' + email
print(msg.body)
mail.send(msg)
'''