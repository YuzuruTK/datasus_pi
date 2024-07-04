from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

# Função para carregar os posts do arquivo JSON
def load_posts():
    with open('static/posts.json', 'r') as file:
        return json.load(file)

# Carregar posts
posts = load_posts()

def get_body_class(route):
    # Dicionário de rotas para classes
    route_classes = {
        '/': 'is-white',
        '/sobre': 'custom-beige-background',
        '/resultados': 'custom-beige-background',
        '/materias-jornalisticas': 'custom-gradient-background',
        '/materia/base-materia-template': 'custom-beige-background',
        '/feed': 'custom-beige-background',
        '/materia/Saude-mental-infantojuvenil': 'custom-beige-background',
        '/materia/doenças-mentais-que-mais-afetam-a-população-ijuiense': 'custom-beige-background',
        '/materia/Saude-mental-infantojuvenil': 'custom-beige-background',
        # Adicione outras rotas e classes conforme necessário
    }
    return route_classes.get(route, 'default-class')

@app.route('/')
def index():
    body_class = get_body_class(request.path)
    return render_template('index.html', css_file='style.css', body_class=body_class)

@app.route('/materias-jornalisticas')
def materiaTeste():
    body_class = get_body_class(request.path)
    return render_template('materias/materia-teste.html', body_class=body_class)

@app.route('/materia/base-materia-template')
def materiaCorpoBase():
    body_class = get_body_class(request.path)
    return render_template('materias/materia-corpo-base.html', body_class=body_class)

@app.route('/materia/Saude-mental-infantojuvenil')
def materia1():
    body_class = get_body_class(request.path)
    return render_template('materias/materia-1.html', body_class=body_class)

@app.route('/materia/doenças-mentais-que-mais-afetam-a-população-ijuiense')
def materia2():
    body_class = get_body_class(request.path)
    
    # Galeria 1
    image_folder1 = os.path.join(app.static_folder, 'photos/galeria-1')  # type: ignore
    images_g1 = [f for f in os.listdir(image_folder1) if os.path.isfile(os.path.join(image_folder1, f))]
    
    # Galeria 2
    image_folder2 = os.path.join(app.static_folder, 'photos/galeria-2')  # type: ignore
    images_g2 = [f for f in os.listdir(image_folder2) if os.path.isfile(os.path.join(image_folder2, f))]
    
    return render_template('materias/materia-2.html', body_class=body_class, images_g1=images_g1, images_g2=images_g2 )

@app.route('/galeria-1')
def galeria1():
    image_folder = os.path.join(app.static_folder, 'photos/galeria-1')  # type: ignore
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('galerias/galeria-1.html', imagesg1=images)

@app.route('/sobre')
def about():
    body_class = get_body_class(request.path)
    return render_template('about.html', body_class=body_class)

@app.route('/galeria-de-graficos')
def results():
    image_folder = os.path.join(app.static_folder, 'graphs')  # type: ignore
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('results.html', images=images)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/resultados')
def pesquisaResults():
    body_class = get_body_class(request.path)
    return render_template('pesquisa-results.html', body_class=body_class)

@app.route('/feed')
def feed():
    body_class = get_body_class(request.path)
    return render_template('feed.html', body_class=body_class, posts=posts)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
