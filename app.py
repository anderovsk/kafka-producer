from kafka import KafkaProducer
from flask import Flask
import os

app = Flask(__name__)

@app.route('/producer')
def producer():
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
    topic = os.getenv('TOPIC')
    #topic = 'anderovsk'
    #bootstrap_servers = ['localhost:9092']
    print(topic)
    print(bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    for _ in range(100):
       msg = f'Anderovsk kafka msg: {_}'
       future = producer.send(topic, msg.encode('utf-8'))
       print(f'Sending msg: {msg}')
       result = future.get(timeout=60)
    metrics = producer.metrics()
    print(metrics)
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)