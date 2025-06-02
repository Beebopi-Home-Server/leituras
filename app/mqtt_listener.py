import paho.mqtt.client as mqtt
from . import db
from .models import Leitura
from flask import current_app
from time import sleep
import datetime

# 1. Callback chamado quando a conexão ao broker for estabelecida
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker com sucesso!")
        # Inscreve no tópico desejado assim que conectar
        client.subscribe("leituras/#")
    else:
        print(f"Falha ao conectar, código de retorno: {rc}")

# 2. Callback chamado sempre que chegar uma mensagem
def on_message(client, userdata, msg):
    # msg.topic é o tópico, msg.payload é o conteúdo em bytes
    mensagem = msg.payload.decode('utf-8')  # converte bytes para string
    print(f"[{msg.topic}] {mensagem}")

    # Registrar no banco de dados
    with current_app.app_context():
        leitura = Leitura(
            topico=msg.topic,
            valor=mensagem,
            data_registro=datetime.datetime.now()
        )
        db.session.add(leitura)
        db.session.commit()
        



def _main():
    # 3. Cria instância do cliente MQTT
    client = mqtt.Client(client_id="cliente_flask_db")
    
    # 4. Atribui callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # 5. Conecta ao broker (pode ser local: localhost, ou público, ex: broker.hivemq.com)
    broker = "mosquitto"
    porta = 1883
    print("Tentando se conectar com broker")
    try:
        client.connect(broker, porta, keepalive=60)
    except:
        print("Procurando broker...")

    print('Conectado ao broker')

    # 6. Entra no loop, aguardando e processando eventos de rede
    client.loop_forever()

def main(app):
    with app.app_context():
        _main()
