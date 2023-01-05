from app import app, mail
from flask import Flask, render_template, url_for, request, redirect, g, session, flash
from form_contact import ContactForm, csrf
from flask_mail import Mail, Message
from config import mail_username


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return f"Hello, {name}! Your ID is {id}."


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_message(request.form)
        return redirect('/success')

    return render_template('contact.html', form=form)


@app.route('/success')
def success():
    flash('Сообщение успешно отправлено!')
    return render_template('success.html')


def send_message(message):
    text = 'Спасибо. Мы получили ваше письмо.\n\nТекст сообщения:\n' + message.get('message') + '\n\nОт кого: ' + message.get('name') + '\nEmail: ' + message.get('email')
    msg = Message(message.get('subject'), sender=mail_username,
            recipients=['canzonetta@mail.ru', message.get('email')],
            body=text
    )
    mail.send(msg)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404