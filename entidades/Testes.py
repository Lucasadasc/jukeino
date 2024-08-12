import os
import requests

from flask.views import MethodView
from flask import jsonify, Blueprint, request, session
from datetime import datetime

esp_ip = os.getenv('ESP_IP')
rotas_testes = Blueprint('Testes', __name__)

# MethodView uma estruturação clara e modular do código para diferentes operações HTTP em um único ponto de endpoint.
class Testes(MethodView):
    
    @rotas_testes.route('/led/ligar', methods=['PUT'])
    def ligar_led():        
        # Realizando a requisição POST 
        url = f'http://{esp_ip}/echo'
        response = requests.post(url, '0')
        
        return jsonify({
            'codigo': '1',
            'status': 'sucesso',
            'mensagem': 'Led ligado'
        })
    
    @rotas_testes.route('/led/desligar', methods=['PUT'])
    def desligar_led():
        # Realizando a requisição POST 
        url = f'http://{esp_ip}/echo'
        response = requests.post(url, '1')
        
        return jsonify({
            'codigo': '1',
            'status': 'sucesso',
            'mensagem': 'Led desligado'
        })