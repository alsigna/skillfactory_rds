import json
import logging
import pickle
import time
import uuid
from sys import stdout
from datetime import datetime
import pika

log = logging.getLogger("model")
log.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler(stdout)
ch.setFormatter(formatter)
log.addHandler(ch)
log.info("model was started")


with open("./prod_2.pkl", "rb") as pkl_file:
    regressor = pickle.load(pkl_file)

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq"),
    )
    channel = connection.channel()

    channel.queue_declare(queue="features")
    channel.queue_declare(queue="y_pred")

    def callback(ch, method, properties, body):
        data = json.loads(body)
        log.info(f"got X: req_id: {properties.correlation_id}, msg_id: {properties.message_id}, body: {data}")

        now_unix = int(time.time())
        now_human = str(datetime.fromtimestamp(now_unix))
        msg_id = str(uuid.uuid4())
        y_pred = regressor.predict([data])
        body_pred = json.dumps(round(y_pred[0], 2))
        properties = pika.BasicProperties(
            correlation_id=properties.correlation_id,
            message_id=msg_id,
            timestamp=now_unix,
        )
        channel.basic_publish(
            exchange="",
            routing_key="y_pred",
            body=body_pred,
            properties=properties,
        )
        log.info(
            f"y_pred was sent. req_id: {properties.correlation_id}, msg_id: {msg_id}, ts: {now_human}, msg: {body_pred}"
        )

    channel.basic_consume(
        queue="features",
        on_message_callback=callback,
        auto_ack=True,
    )
    channel.start_consuming()

except:
    log.error("cannot connect to rabbitmq")
    time.sleep(5)
