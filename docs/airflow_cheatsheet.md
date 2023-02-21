# Airflow Cheatsheet

Airflow has a very rich command line interface that allows for many types of operation on a DAG, starting services, and supporting development and testing.

## Overview

Practice, Practice, Practice!! Perfect practice makes you perfect. When you are new to any technology, remember to use command line (if available) to undertsand and memorize the commands as well as behavior of the applications. The below commands are some of the most useful commands, to work with Airflow. Please see airflow documentation [here](https://airflow.apache.org/docs/apache-airflow/1.10.2/cli.html#) for detail list of commands and their sub-commands.

### Installation

Use the following command to quickly install airflow on the host machine. Airflow can be dockerized and docker version of airflow is available [here](https://github.com/data-engineering/docker-airflow)

```code
# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)

export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080
```

| Command | Description |
|---------|-------------|
|airflow clear dag_id|Clear a set of task instance, as if they never ran|
|airflow connections -l|List all airflow connections|
|airflow create_user -r Op -u rsigamani -p password|Create user rsigamani with role as Operations |
|airflow dag_state dag_id execution_date|Get the status of dag_id for a given date|
|airflow delete_dag dag_id|Delete all DB records related to the specified DAG|
|airflow delete_user -u rsigamani|Delete user rsigamani|
|airflow list_dag_runs dag_id|List all the runs for dag_id|
|airflow list_dags|Print the list of active DAGs|
|airflow list_tasks tutorial --tree|Print the hierarchy of tasks in the tutorial DAG|
|airflow list_tasks tutorial|Print the list of tasks the "tutorial" dag_id|
|airflow list_users|List all the airflow users|
|airflow pause dag_id|Pause the DAG with dag_id|
|airflow run dag_id task_id execution_date|Run a single task instance from a DAG|
|airflow task_state dag_id task_id execution_date|Get the status of a task instance|
|airflow test tutorial print_date 2021-01-01 -dr|Dry run the task from tutorial|
|airflow test tutorial print_date 2021-01-01|Test "print_date" task in tutorial DAG|
|airflow unpause dag_id|Reusme a paused DAG|
|airflow version [-h]|Show the version of airflow|
|airflow ~/airflow/dags/tutorial.py|Validate the installation by executing a tutorial script|
