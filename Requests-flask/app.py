from flask import Flask, request
from Routes import query_example, form_example, json_example, manage_files

app = Flask(__name__)

if __name__ == '__main__':
    app.add_url_rule('/query-example', methods=['GET'], view_func=query_example.query_example)
    # allow both GET and POST requests
    app.add_url_rule('/json-example', methods=['POST'], view_func=json_example.json_example)
    app.add_url_rule('/form-example', methods=['GET', 'POST'], view_func=form_example.form_example)
    app.add_url_rule('/files-example', methods=['GET', 'POST'], view_func=manage_files.read_file)
    app.run(debug=1, port=5000)