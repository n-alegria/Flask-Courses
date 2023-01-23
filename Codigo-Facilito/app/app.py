from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_requests():
    print('Antes de la peticion...')
    
@app.after_request
def after_requests(response):
    print('Despues de la peticion...')
    return response

def index():
    print('Estamos realizando la peticion...')
    data = {
        'titulo' : 'Index',
        'encabezado' : 'Bienvenido(a)',
    }
    return render_template('index.html', data=data)

@app.route('/contacto')
def contacto():
    data = {
        'titulo' : 'Contacto',
        'encabezado' : 'Bienvenido(a)',
    }
    return render_template('contacto.html', data=data)

@app.route('/saludo/<nombre>')
def saludo(nombre: str):
    return f'Hola {nombre.capitalize()}!'

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1:int, valor2:int):
    return f'{valor1 + valor2}'

@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre:str, edad:int):
    return f'Tu nombre es {nombre.capitalize()} y tu edad es {edad}'

@app.route('/lenguajes')
def lenguajes():
    data = {
        'lenguajes' : []
        #'lenguajes' : ['PHP', 'Python', 'Kotling', 'Java', 'C#', 'JavaScript']
    }
    return render_template('lenguajes.html', data=data)

# @app.route('/holaMundo')
# def hola_mundo():
#     return 'Hola Mundo'

# HTTP: Hypertext Transfer Protocol
# -> GET, POST, PUT, DELETE <- #
@app.route('/datos')
def datos():
    a = request.args.get('valor1')
    b = request.args.get('valor2')
    return 'Estos son los datos: {0}, {1}'.format(a, b)


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=8000)