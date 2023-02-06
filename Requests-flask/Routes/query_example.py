from flask import request

def query_example():
    """
    Los Query-String comienzan luego de terminada la ruta.
    Se utiliza '?' para marcar el inicicio del query-string siendo estos pares clave-valor, se concatenan utilizando '&'.
    :: request.args.get('clave') -> retorna 'None' en caso de no existir la clave
    :: request.args['clave]' -> retorna 'error 400' si no existe la clave
    """
    lenguage = request.args.get('lenguage')
    framework = request.args.get('framework')
    msg = '<h1>The lenguage value is: {}</h1>'.format(lenguage)
    if framework:
        msg += '<h2>The Framework is: {}</h2>'.format(framework)
    return msg 
