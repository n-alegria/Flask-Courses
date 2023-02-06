from flask import request
import json

def read_file():
    if request.method == 'GET':
        return '''
        <h1>File Upload</h1>
        <form method="POST" action="" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Submit">
        </form>
        '''
    else:
        upload_file = request.files['file']
        if upload_file.filename != '':
            # print the type
            print(type(upload_file))
            # print the entire object
            print(upload_file)
            # use the method '.save()' to upload the file into server
            upload_file.save(f'img/{upload_file.filename}')
        return json.dumps({"file_received" : True})

"""
* -> multiple: es usado para permitir la subida de multiples archivos en un solo input
    <input type="file" name="file" multiple>
* -> accept: es usado para filtrar que archivos son permitidos
    <input type="file" name="file" accept='.doc,.docx'>
    <input type="file" name="file" accept='image/*'>
"""