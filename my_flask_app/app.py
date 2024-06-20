from flask import Flask, render_template
import os
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

@app.route('/galeria-de-graficos')
def results():
    image_folder = os.path.join(app.static_folder, 'graphs') # type: ignore
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('results.html', images=images)


@app.route('/blog')
def blog():

    return render_template('blog.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
