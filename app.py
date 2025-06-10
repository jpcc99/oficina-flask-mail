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
    return '<h1>Oficina Flask-Mail</h1><button><a href="enviar-email">Enviar email!</a></button>'


@app.route("/enviar-email")
def enviar_email():
    msg = Message(
        subject="Teste de Flask-Mail",
        sender="oficinaflaskmail@gmail.com",
        # recipients=["destinatario@exemplo.com"],
        recipients=["jpcc@discente.ifpe.edu.br"],
        body="Parabéns! Você enviou um email com Flask-Mail!",
    )
    mail.send(msg)
    return "<h1>Oficina Flask-Mail</h1><p>Email enviado! Verifique sua caixa de entrada</p>"


if __name__ == "__main__":
    app.run(debug=True)
