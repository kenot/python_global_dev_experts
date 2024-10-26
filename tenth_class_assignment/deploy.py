import os


def deploy_superset():
    os.system("kubectl create deployment superset --image=amancevice/superset")
    os.system("kubectl expose deployment superset --type=LoadBalancer --name=superset-service --port=80 --target-port=8088")


def deploy_airflow():
    os.system("kubectl create deployment airflow --image=puckel/docker-airflow")
    os.system("kubectl expose deployment airflow --type=LoadBalancer --name=airflow-service --port=80 --target-port=8080")


if __name__ == "__main__":
    deploy_superset()
    deploy_airflow()
