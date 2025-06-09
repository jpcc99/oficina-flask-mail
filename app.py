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


@app.post("/enviar-email")
def enviar_email():
    msg = Message(
        subject=request.form["subject"],
        sender="oficinaflaskmail@gmail.com",
        recipients=[request.form["nome"], request.form["destinatario"]],
        body=request.form["mensagem"],
    )
    mail.send(msg)
    return render_template("sucesso.html", person=request.form["nome"])


if __name__ == "__main__":
    app.run(debug=True)
