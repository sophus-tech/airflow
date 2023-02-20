# Airflow

Airflow is an open-source workflow management platform developed by Airbnb to programatically autor and manage workflows. Provides an intutive UI to monitor and execute workflows. Airflow uses directed acyclic graphs (DAGs) to manage workflow orchestration.

Tasks and dependencies are defined in Python and then Airflow manages the scheduling and execution. DAGs can be run either on a defined schedule (e.g. hourly or daily) or based on external event triggers (e.g. a file appearing in Hive). Previous DAG-based schedulers like Oozie and Azkaban tended to rely on multiple configuration files and file system trees to create a DAG, whereas in Airflow, DAGs can often be written in one Python file.

## Overview

Repository for airflow related artifacts and resources including best practices, standards, cheatsheets  and templates.

### Wiki Links

- [Airflow Best practices and standards](docs/airflow_best_practices_standards.md)
- [Airflow Cheatsheet](docs/airflow_cheatsheet.md)
- [Python Best Practices and Standards](https://github.ibm.com/data-engineering/python/docs/python_best_practices_standards.md)

  Airflow uses python as programming language to create DAGs. Please use the best practices and standards defined in this document before start working your first DAG.

### Navigation

- .gitignore
  - List the files and directories to be ignored while check in to airflow
- docs  
  - Directory for documentation exported to different file formats
- examples
  - Contains examples for reference or hands on practice
- images
  - images used in documentation within airflow
- labs  
  - Contains code, artifacts for hands on exercises
- README.md
  - Readme page for each repo or folders within airflow, explaining the process, code or instructions  
- templates
  - Standard templates developed based on best practices that case used to build dags 

### References

- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Running Airflow Locally](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

### Contacts

ramesh.sigamani@ibm.com
