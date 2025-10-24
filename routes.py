from main import app
from datetime import date
import json
from flask import render_template

dia_atual = date.today().strftime('%Y-%m-%d')
mensagem_de_hj = json.load(open('mensagens.json', encoding='utf-8'))[dia_atual]

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/mensagem-do-dia')
def mensagem():
    return render_template('mensagem.html', mensagem_do_dia=mensagem_de_hj)

