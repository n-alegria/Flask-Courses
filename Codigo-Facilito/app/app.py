from flask import Flask, render_template

app = Flask(__name__)

def index():
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

# @app.route('/holaMundo')
# def hola_mundo():
#     return 'Hola Mundo'

if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=8000)