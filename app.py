from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "oficinaflaskmail@gmail.com"
app.config["MAIL_PASSWORD"] = "ffrr erkd xxgj xwba"
mail = Mail(app)


@app.route("/")
def home():
    return "Hello World"


@app.route("/enviar-email")
def enviar_email():
    msg = Message(
        subject="Teste de Flask-Mail",
        sender="oficinaflaskmail@gmail.com",
        recipients=["bxs@discente.ifpe.edu.br", "jpcc@discente.ifpe.edu.br"],
        body="Testando...",
    )
    mail.send(msg)
    return "Email enviado! Verifique sua caixa de entrada"


if __name__ == "__main__":
    app.run(debug=True)
