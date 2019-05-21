from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'cafe'

@app.route('/')
def index():
    return render_template('index.html', titulo = 'SIMU')


@app.route('/mapa')
def mapa():
    return render_template('mapa.html', titulo= 'SIMU')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)