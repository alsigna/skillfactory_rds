import json
import logging
import time
from sys import stdout

import pika
from sklearn.metrics import mean_squared_error

log = logging.getLogger("metric")
log.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler(stdout)
fh = logging.FileHandler("./metric.log")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
log.addHandler(ch)
log.addHandler(fh)
log.info("metric was started")


req_dict = {}

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq"),
    )
    channel = connection.channel()

    channel.queue_declare(queue="y_true")
    channel.queue_declare(queue="y_pred")

    def callback(ch, method, properties, body):
        y = json.loads(body)
        req_id = properties.correlation_id
        msg_id = properties.message_id
        log.info(f"got {method.routing_key}. req_id: {req_id}, msg_id: {msg_id}, value: {y}")

        if req_id in req_dict.keys():
            rmse = mean_squared_error([req_dict[req_id]], [y], squared=False).round(2)
            log.info(f"RMSE calculated. req_id: {req_id}, rmse: {rmse}")
            _ = req_dict.pop(req_id, None)
        else:
            req_dict[req_id] = y

    channel.basic_consume(queue="y_pred", on_message_callback=callback, auto_ack=True)
    channel.basic_consume(queue="y_true", on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

except:
    log.error("cannot connect to rabbitmq")
    time.sleep(5)
