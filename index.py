from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Настройки email
sender_email = "dmitrievila951@gmail.com"
receiver_email = "your_email@example.com"
subject = "новый пользователь с именем:{name}"

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        minecraft_nick = request.form['minecraft_nick']
        minecraft_experience = request.form['minecraft_experience']
        description = request.form['description']
        comments = request.form['comments']

        # Создание сообщения email
        body = f"""
        регистрация:
        Имя: {name}
        Пол: {gender}
        возраст: {age}
        майнкрафт имя: {minecraft_nick}
        опыт игры в майнкрафт(стаж): {minecraft_experience}
        описание: {description}
        коментарии для тех админов: {comments}
        """
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Отправка email
        with smtplib.SMTP('localhost') as smtp:
            smtp.send_message(msg)

        return 'спасибо за регистрацию'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)