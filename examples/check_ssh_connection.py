# -*- coding: utf-8 -*-
'''
Check SSH connection between Airflow and a remote server
This dag uses SSH operator to connect to remote host and execute a shell script
Hooks:
    SSH
Operators:
    Dummy, SSH
Tasks:
    echo_hello_to_a_file
'''

__author__ = 'Ramesh Sigamani'
__copyright__ = '(c) Copyright Sophus Technologies 2021'
__credits__ = ['Ramesh S']
__maintainer__ = 'Sophus Technologies'
__email__ = 'ramesh.sigamani@sophus.io'

# Standard library imports
from datetime import timedelta

# Third party imports
import airflow
from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy_operator import DummyOperator

# Local application imports


# define default arguments for the dag
default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
    }

# define hooks here
# ssh_remote_server is the connection string defined in airflow for the remote server
ssh_task_id = SSHHook(
    ssh_conn_id='ssh_remote_server'
    )

# define methods here


# define dag
dag = DAG(
    dag_id='ssh_conn_remote_server',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
)

# tasks to connect ql prod iae and touch a file
with dag:
    # dummy start task
    start = DummyOperator(
        task_id='start'
    )

    # dummy end task
    end = DummyOperator(
        task_id='end'
    )

    # echo a message to a file on the remote host
    echo_hello_to_a_file = SSHOperator(
        task_id='echo_hello_to_a_file',
        command='ksh <path_to_ksh_file>/echo_hello_to_a_file.ksh',
        ssh_hook=ssh_task_id
    )

    # Orchestrate the tasks to print hello
    start >> echo_hello_to_a_file >> end
