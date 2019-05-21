from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'cafe'

@app.route('/')
def index():
    return render_template('index.html', titulo = 'SIMU')


@app.route('/mapa')
def mapa():
    return render_template('mapa.html', titulo= 'SIMU')

app.run(debug=True)