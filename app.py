from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html", titulo_pagina = "Alisson Araújo de Lima 😄")

@app.route("/curriculo/")
def curriculo():
    return render_template("curriculo.html", titulo_pagina = "Currículo Digital 📄")

@app.route("/portfolio/")
def portfolio():
    return render_template("portfolio.html", titulo_pagina = "Portfólio 👜")