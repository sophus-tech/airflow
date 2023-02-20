# Airflow Best Practices and Standards

## Basic Concepts

- DAG

  Graphs of tasks/ usages

- OPERATOR

  The operator refers to the transformation step further divided into:

  - Sensor

    This type of operator performs a function to polls with frequency/timeout

  - EXECUTOR

    This type of operator performs trigger operations, for example, HiveOperator, Pig Operator

  - TASK

    Task is the main entity of the DAG. The main thing here is task instance considered to run of a task at a point of time

  - HOOK
    It is considered as the Interface for the external System such as a hook of JDBC and HTTP.
