# -*- coding: utf-8 -*-
'''
This dag orchestrates a set of tasks that are executed in a sequence.
This dag uses SSH operator to connect to remote host and execute set of scripts.

Hooks:
    SSH
Operators:
    Dummy, SSH
Tasks:
    copy_location_from_s3_to_cos
    preprocess_location_step_1
    preprocess_location_step_2
'''

__author__ = 'Ramesh Sigamani'
__copyright__ = '(c) Copyright Sophus Technologies 2020'
__credits__ = ['Ramesh S']
__maintainer__ = 'Sophus Technologies'
__email__ = 'ramesh.sigamani@sophus.io'

# Standard library imports
from datetime import datetime, timedelta

# Third party imports
import airflow
from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor

# Local application imports


# define default arguments for the dag
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 1, 1),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# define hooks here, dp_prod is the ssh connection name defined in the airflow
ssh_dp_prod = SSHHook(
    ssh_conn_id='dp_prod'
)

ssh_app_prod = SSHHook(
    ssh_conn_id='ssh_prod_app'
)

# application scripts path on the remote server
ssh_bin_path = "/home/rsigamani/scripts/bin"

# define methods here


# define dag
dag = DAG(
    dag_id='di_raw_location',
    schedule_interval='30 2 * * *',
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

    # task to copy datasets from s3 bucket to cos
    copy_location_from_s3_to_cos = SSHOperator(
        task_id='copy_location_from_s3_to_cos',
        command=f'sh /root/scripts/location/location_copy_dailyprocess_rclone.sh ',
        ssh_hook=ssh_app_prod
    )

    # Alter location table to add partitions
    alter_table_location = SSHOperator(
        task_id='alter_table_location',
        command=f'ksh {ssh_bin_path}/exec_hive_sql_location.ksh -t=ext_location -f=location_raw_add_partition.sql',
        ssh_hook=ssh_dp_prod
    )

    # preprocess the datasets to organize in daily buckets
    preprocess_location_step_1 = SSHOperator(
        task_id='preprocess_location_step_1',
        command=f'ksh {ssh_bin_path}/exec_location_pre_step_1.ksh -t=location -f=pre_process_step_1_launch.py',
        ssh_hook=ssh_dp_prod
    )

    # process datasets from daily buckets to hourly buckets
    preprocess_location_step_2 = SSHOperator(
        task_id='preprocess_location_step_2',
        command=f'ksh {ssh_bin_path}/exec_location_pre_step_2.ksh -t=location -f=pre_process_step_2_launch.py',
        ssh_hook=ssh_dp_prod
    )

    # Orchestrate the tasks to copy and preprocess the datasets
    start >> \
        copy_location_from_s3_to_cos >> \
        alter_table_location >> \
        preprocess_location_step_1 >> \
        preprocess_location_step_2 >> \
        end
