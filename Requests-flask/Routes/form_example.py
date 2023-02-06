from flask import request

def form_example():
    """
    Las claves serán leídas a través del atributo 'name'.
    Dentro de la función se deberá chequear si la petición es a traves del método GET o POST.
    Si es GET se muestra el formulario de lo contrario se procesará la información obtenida.
    """
    if request.method == 'POST':
        lenguage = request.form.get('lenguage')
        framework = request.form.get('framework')
        return '''
                <h1>The lenguage value is: {}</h1>
                <h2>The Framework is: {}</h2>'''.format(lenguage, framework)
    return '''
        <form method="POST">
            <div><label>Lenguage: <input type="text" name="lenguage"</label></div>
            <div><label>Framework: <input type="text" name="framework"</label></div>
            <input type="submit" value="Submit">
        </form>'''