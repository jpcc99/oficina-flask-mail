from flask import Flask, render_template, request
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
    return render_template("index.html")


"""
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
"""


@app.route("/enviar-email", methods=["GET", "POST"])
def enviar_email():
    if request.method == "GET":
        return render_template("send_email.html")

    if request.method == "POST":
        return "Its posting..."


if __name__ == "__main__":
    app.run(debug=True)
