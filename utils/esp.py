import os
import random
import requests

from time import sleep

esp_ip = os.getenv('ESP_IP')

comandos = [
    {
        'led' : '1',
        'comando_desligar': 'a'
    },
    {
        'led' : '2',
        'comando_desligar': 'b'
    },
    {
        'led' : '3',
        'comando_desligar': 'c'
    },
    {
        'led' : '4',
        'comando_desligar': 'd'
    },
    {
        'led' : '5',
        'comando_desligar': 'e'
    },
    {
        'led' : '6',
        'comando_desligar': 'f'
    },
    {
        'led' : '7',
        'comando_desligar': 'g'
    },
    {
        'led' : '8',
        'comando_desligar': 'h'
    },
    {
        'led' : '9',
        'comando_desligar': 'i'
    }
]

def gerar_sequencia(numero_piscadas: int) -> list:
    """
    Gera uma sequencia de leds ligados conforme o númeor de piscas informados:
    - Recebe o número de vezes que um led será ligado
    - Gera uma lista aleatoria de string com valores entre 0 e 5
    - Para cada valor da lista, liga o led correspondente (requisição POST ao ESP)
    - Retorna essa lista para o usuário
    """
    lista_sequencia = [str(random.randint(1, 7)) for _ in range(numero_piscadas)]
    
    # Ligando e desligando leds na sequencia indicada 
    sleep(2)
    for numero in lista_sequencia:
        # filtrando numero na lista de comandos
        led_it = list(filter(lambda x: x['led'] == numero, comandos))
        
        # url para requisição
        url = f'http://{esp_ip}/echo'
        
        # ligando led
        response = requests.post(url, led_it[0]['led'])
        sleep(0.3)
        
        # desligando led
        response = response = requests.post(url, str(led_it[0]['comando_desligar']))
        sleep(0.3)
    
    return lista_sequencia

def ligando_led_especifico(led_id: int):
    """
    Liga um led específico conforme o id informado
    - Recebe o id do led a ser ligado
    - Envia uma requisição POST ao ESP para ligar o led
    """
    url = f'http://{esp_ip}/echo'
    
    # filtrando led da lista de comandos 
    led_it = list(filter(lambda x: x['led'] == str(led_id), comandos))[0]
    
    #Ligando led
    requests.post(url, str(led_it['led']))
    sleep(0.5)
    
    #Desligando leds
    requests.post(url, str(led_it['comando_desligar']))