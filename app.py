import os
import json

from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')

# Habilitando CORS para os domínios permitidos
# CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)

# Carregando env 
load_dotenv()
print(os.getenv('ESP_IP'))

# Importando rotas 
from entidades.Testes import rotas_testes
from entidades.Sequencias import rotas_sequencias

app.register_blueprint(rotas_testes, url_prefix='/api')
app.register_blueprint(rotas_sequencias, url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 3000), debug=True) 