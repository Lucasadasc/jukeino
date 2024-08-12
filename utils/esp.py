import os
import random
import requests

from time import sleep


esp_ip = os.getenv('ESP_IP')

def gerar_sequencia(numero_piscadas: int) -> list:
    """
    Gera uma sequencia de leds ligados conforme o númeor de piscas informados:
    - Recebe o número de vezes que um led será ligado
    - Gera uma lista aleatoria de string com valores entre 0 e 5
    - Para cada valor da lista, liga o led correspondente (requisição POST ao ESP)
    - Retorna essa lista para o usuário
    """
    lista_sequencia = [str(random.randint(0, 4)) for _ in range(numero_piscadas)]
    
    # Ligando e desligando leds na sequencia indicada 
    for numero in lista_sequencia:
        url = f'http://{esp_ip}/echo'
        
        # ligando led
        response = requests.post(url, numero)
        sleep(1)
        
        # desligando led 
        numero_desligar = int(numero) + 6
        
        if numero == 4:
            numero_desligar = 'a' 
        elif numero == 5:
            numero_desligar = 'b'
        
        response = response = requests.post(url, str(numero_desligar))
        sleep(1)
    
    return lista_sequencia

def ligando_led_especifico(led_id: int):
    """
    Liga um led específico conforme o id informado
    - Recebe o id do led a ser ligado
    - Envia uma requisição POST ao ESP para ligar o led
    """
    url = f'http://{esp_ip}/echo'
    
    #Ligando led
    requests.post(url, str(led_id))
    sleep(1)
    
    #Desligando led
    numero_desligar = led_id + 6
    
    if led_id == 4:
        numero_desligar = 'a'
    elif led_id == 5:
        numero_desligar = 'b'
    
    requests.post(url, str(numero_desligar))