import pika
import pickle
import numpy as np
import json
import sklearn
import uuid
import time


# with open("./prod_2.pkl", "rb") as pkl_file:
with open("./prod_2.pkl", "rb") as pkl_file:
    regressor = pickle.load(pkl_file)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="Features")
channel.queue_declare(queue="y_pred")


def callback(ch, method, properties, body):
    data = json.loads(body)
    y_pred = regressor.predict([data])
    print(f"Получен вектор признаков: {body}")
    body_pred = json.dumps(round(y_pred[0], 2))
    channel.basic_publish(
        exchange="",
        routing_key="y_pred",
        body=body_pred,
    )
    print(f"Сообщение отправлено: {body_pred}")


# on_message_callback показывает какую функцию вызвать при получении сообщения
channel.basic_consume(
    queue="Features",
    on_message_callback=callback,
    auto_ack=True,
)
print("...Ожидание сообщений, для выхода нажмите CTRL+C")

channel.start_consuming()