#export AIRFLOW_HOME=.
#airflow db init
#airflow webserver -p 8080
#airflow scheduler
#sudo lsof -i tcp:<port>
#kill -9 <pid>

"""
To run airflow in docker:
    to download docker-compose yaml:
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'

    command to create folders to workspace
    mkdir -p ./dags ./logs ./plugins ./config
    echo -e "AIRFLOW_UID=$(id -u)" > .env

    docker compose up airflow-init

    docker-compose up -d

    airflow-airflow
"""