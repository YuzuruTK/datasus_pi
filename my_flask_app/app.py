from flask import Flask, render_template

import subprocess

# Executa o comando 'ls -l'
subprocess.run(['sass', 'static/bulma/bulma.scss:static/css/style.css'])



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', css_file='style.css')


@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/resultados')
def results():
    return render_template('results.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
