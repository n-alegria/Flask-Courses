from flask import request

def json_example():
    """
    Se envian dos datos como Raw -> json
    """
    request_data = request.get_json()

    # es recomendable chequear si existen las claves previo a procesarlas
    
    lenguage = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'lenguage' in request_data:
            lenguage = request_data['lenguage']
        
        if 'framework' in request_data:
            framework = request_data['framework']

        # se utilizan dos claves debido a que esta anidado
        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        # se debe señalar el indice debido a que es un array
        if 'examples' in request_data:
            if((type(request_data['examples']) == list) and (len(request_data) > 0)):
                example = request_data['examples'][0]
        
        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']
    
    return '''
        The lenguage value is: {}
        The framework value is: {}
        The Python version is: {}
        The item at index 0 in the example list is: {}
        The boolean value is: {}'''.format(lenguage, framework, python_version, example, boolean_test)