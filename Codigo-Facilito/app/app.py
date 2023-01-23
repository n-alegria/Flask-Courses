from flask import Flask, render_template

app = Flask(__name__)

def index():
    return render_template('index.html', titulo='Index')

@app.route('/holaMundo')
def hola_mundo():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=8000)