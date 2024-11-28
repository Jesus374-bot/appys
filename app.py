from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Clave secreta para sesiones

# Configuración de Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "jl10052023@gmail.com"
app.config["MAIL_PASSWORD"] = "ueyf yzle omlz fzhq" 
app.config["MAIL_DEFAULT_SENDER"] = "jl10052023@gmail.com"

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]

        msg = Message(
            subject=f"Nuevo mensaje de {nombre}",
            recipients=["72151802@iestpluisnegreiros.edu.pe"],  
            body=f"Nombre: {nombre}\nCorreo: {email}\nMensaje: {mensaje}",
        )
        try:
            # Enviar el mensaje
            mail.send(msg)
            flash("¡Tu mensaje ha sido enviado con éxito!", "success")
        except Exception as e:
            # En caso de error, mostrar el mensaje de error
            flash(f"Hubo un error al enviar el mensaje: {str(e)}", "danger")

        # Redirigir al usuario nuevamente al formulario
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)



