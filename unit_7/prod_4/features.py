import pika
import numpy as np
from sklearn.datasets import load_diabetes
import json
import uuid
import time

X, y = load_diabetes(return_X_y=True)
random_row = np.random.randint(0, X.shape[0] - 1)

# Подключение к серверу на локальном хосте:
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Создадим очередь, с которой будем работать:
channel.queue_declare(queue="y_true")
channel.queue_declare(queue="Features")


# Опубликуем сообщение
# exchange определяет, в какую очередь отправляется сообщение.
# Если мы используем дефолтную точку обмена, то значение можно оставить пустым.
# параметр routing_key указывает имя очереди,
# параметр body тело самого сообщения,

body = json.dumps(y[random_row])
channel.basic_publish(
    exchange="",
    routing_key="y_true",
    body=body,
)
print(f"Отправлен правильный ответ: {body}")


body = json.dumps(list(X[random_row]))
properties = pika.BasicProperties(
    message_id=str(uuid.uuid4()),
    timestamp=int(time.time()),
)
channel.basic_publish(
    exchange="",
    routing_key="Features",
    body=body,
    properties=properties,
)
print(f"Отправлен вектор презннаков: {body}")

# Закроем подключение
connection.close()