from celery import Celery

worker = Celery('tasks', backend='rpc://', broker='amqp://guest:guest@localhost:5672')


def send_mail():
    return 42


@worker.task()
def send_mail_task(data):
    print(data)
    _ = send_mail()
    return _