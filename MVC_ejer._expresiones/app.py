import os
from flask import Flask
from controller import expresiones_controller

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))
app.secret_key = 'clave_secreta'

app.add_url_rule('/', view_func=expresiones_controller.index)
app.add_url_rule('/convertir', view_func=expresiones_controller.convertir, methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
