import json
import logging
import time
import uuid
from datetime import datetime
from sys import stdout

import numpy as np
import pika
from sklearn.datasets import load_diabetes

log = logging.getLogger("features")
log.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler(stdout)
ch.setFormatter(formatter)
log.addHandler(ch)
log.info("Features was started")

X, y = load_diabetes(return_X_y=True)

while True:
    random_row = np.random.randint(0, X.shape[0] - 1)
    now_unix = int(time.time())
    now_human = str(datetime.fromtimestamp(now_unix))
    usr_id = str(uuid.uuid4())
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters("rabbitmq"),
        )
        channel = connection.channel()

        channel.queue_declare(queue="y_true")
        channel.queue_declare(queue="features")

        body = json.dumps(y[random_row])
        msg_id = str(uuid.uuid4())
        properties = pika.BasicProperties(
            correlation_id=usr_id,
            message_id=msg_id,
            timestamp=now_unix,
        )
        channel.basic_publish(
            exchange="",
            routing_key="y_true",
            body=body,
            properties=properties,
        )
        log.info(f"y_true was sent. req_id: {usr_id}, msg_id: {msg_id}, ts: {now_human}, msg: {body}")

        body = json.dumps(list(X[random_row]))
        msg_id = str(uuid.uuid4())
        properties = pika.BasicProperties(
            correlation_id=usr_id,
            message_id=msg_id,
            timestamp=now_unix,
        )
        channel.basic_publish(
            exchange="",
            routing_key="features",
            body=body,
            properties=properties,
        )
        log.info(f"X was sent. req_id: {usr_id}, msg_id: {msg_id}, ts: {now_human}, msg: {body}")

        connection.close()
    except:
        log.error("cannot connect to rabbitmq")
        time.sleep(5)

    time.sleep(2)
