"""
Intro a Full Stack Web
Programa de acertar capitales
Author: 1r DAW
"""
from flask import Flask, render_template, request
import bd

# Secuencia principal de programa
app = Flask(__name__)

@app.route('/')
def root():
    pais = seleccionarPaisRandom()
    # pais  = "Francia"
    return render_template("index.html", paisHtml=pais)

@app.route('/checkCapital', methods=["GET", "POST"])
def checkCapital():
    if request.method == 'POST':
        # print(request.form)
        capitalUsuario = request.form.get("capital")
        pais= request.form.get("pais")
        # resultado = comprobarCapitalDirectamenteenWikipedia(pais,capitalUsuario)
        resultado, capitalOK = bd.comprobarCapital(pais,capitalUsuario)
        # resultado = True
        # capitalOK = "Capital del país"
        return render_template("resultado.html", resultadoHtml=resultado, 
            capitalHtml=capitalOK)
# app.run()