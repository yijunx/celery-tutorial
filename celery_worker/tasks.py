# amqp://rabbitmq
from celery import Celery
from celery.utils.log import get_task_logger
from time import sleep


logger = get_task_logger(__name__)

# app = Celery('tasks', broker="amqp://rabbitmq")
app = Celery("tasks", broker="amqp://rabbitmq:5672", backend="redis://redis:6379")


@app.task()
def longtime_add(x, y):
    logger.info('Got request - start to work')
    sleep(20) # simulating long running task
    logger.info('work finished')
    return x + y

# celery -A tasks worker --loglevel=info