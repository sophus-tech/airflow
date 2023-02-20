# airflow -  examples

This directory contains airflow application examples that are developed using best practices and standards.

## Links

- [Cheeck SSH connection to a remote server](check_ssh_connection.py)
  This dag uses SSH hook to connect a remoote server and print a hello message by executing a shell script.
- [Running multiple tasks from DAG](invoke_multiple_tasks.py)
  This dag is an example to run multiple tasks in sequence, with each tasks dependent on the previous task.
