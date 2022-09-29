import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
import socket

def is_port_in_use(port: int) -> bool:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def mlflow_track_example():
    """
    #>>>mlflow ui
    to start the UI in localhost
    """
    log_param("param1", randint(0, 100))
    log_metric("foo", random())
    log_metric("foo", random()+1)
    log_metric("foo", random()+2)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    log_artifacts("outputs")
    if not is_port_in_use(5000):
        os.system("mlflow ui")

def mlflow_project_example():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mlflow_tack_example()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
