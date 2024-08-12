import os
import requests

from flask.views import MethodView
from flask import jsonify, Blueprint, request, session

from utils.esp import gerar_sequencia, ligando_led_especifico

esp_ip = os.getenv('ESP_IP')
rotas_sequencias = Blueprint('Sequencias', __name__)

# MethodView uma estruturação clara e modular do código para diferentes operações HTTP em um único ponto de endpoint.
class Sequencias(MethodView):
    
    @rotas_sequencias.route('/sequencia/gerar', methods=['POST'])
    def retornar_sequencia():
        
        dados = request.json
        
        if "numero_piscadas" not in dados:
            return jsonify({
                "codigo": "2",
                "status": "erro",
                "mensagem": "Número de piscadas não informado."
            })
        
        if dados['numero_piscadas'] < 1 or dados["numero_piscadas"] == 0 or dados["numero_piscadas"] is None:
            return jsonify({
                "codigo": "2",
                "status": "erro",
                "mensagem": "Número de piscadas inválido."
            })
        
        numero_piscadas = dados['numero_piscadas']
        
        lista_gerada = gerar_sequencia(numero_piscadas)
        
        return jsonify({
            "codigo": "1",
            "status": "sucesso",
            "mensagem": "Sequência gerada com sucesso.",
            "sequencia": lista_gerada
        })
    
    @rotas_sequencias.route('/sequencia/acender', methods=['POST'])
    def acender_led_informado():
        dados = request.json
        
        if "led_id" not in dados:
            return jsonify({
                "codigo": "2",
                "status": "erro",
                "mensagem": "Led não informado."
            })
        
        if dados["led_id"] is None or dados["led_id"] == "":
            return jsonify({
                "codigo": "2",
                "status": "erro",
                "mensagem": "Led inválido."
            })
        
        led_id = dados["led_id"]
        ligando_led_especifico(led_id)
        
        return jsonify({
            "codigo": "1",
            "status": "sucesso",
            "mensagem": "Led aceso com sucesso."
        })
        