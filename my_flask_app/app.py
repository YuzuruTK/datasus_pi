from flask import Flask, render_template, request
import os
import subprocess

# Executa o comando 'ls -l'
subprocess.run(['sass', 'static/bulma/bulma.scss:static/css/style.css'])



app = Flask(__name__)

def get_body_class(route):
    # Dicionário de rotas para classes
    route_classes = {
        '/': 'custom-beige-background',
        '/sobre': 'custom-beige-background',
        '/materia/nome-da-materia': 'custom-gradient-background'
        # Adicione outras rotas e classes conforme necessário
    }
    return route_classes.get(route, 'default-class')

@app.route('/')
def index():
    body_class = get_body_class(request.path)

    return render_template('index.html', css_file='style.css', body_class=body_class)

@app.route('/materia/nome-da-materia')
def materiaTeste():
        body_class = get_body_class(request.path)
        return render_template('materias/materia-teste.html', body_class=body_class)


@app.route('/sobre')
def about():
    body_class = get_body_class(request.path)
    return render_template('about.html', body_class=body_class)

@app.route('/galeria-de-graficos')
def results():
    image_folder = os.path.join(app.static_folder, 'graphs') # type: ignore
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('results.html', images=images)


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/resultados')
def pesquisaResults():
    return render_template('pesquisa-results.html')


@app.route('/feed')
def feed():
    return render_template('feed.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
