# docker_spark_submit
Test a Pyspark code without installing Spark artifacts locally

## PYTHON 2

### Docker Build

    docker build -t pyspark2_test -f v23_test_Dockerfile_pyspark_py2_spk2 .

    docker build -t pyspark2_sub -f v23_Dockerfile_pyspark_py2_spk2 .

Get into console

    docker run --rm -dti -v $PWD:/home/jovyan/SparkProjects/Project1 --name spark_test pyspark2_test '/bin/bash'

    docker exec -it spark_test '/bin/bash'

In you current directory ($PWD root) has to exist the spark_submit.sh file, then run:

    docker run --rm -d -v $PWD:/home/jovyan/SparkProjects/Project1 pyspark2_sub

And you pyspark code will run, when it finishes the docker container dies also.

## PYTHON 3

### Docker Build

    docker build -t pyspark3_test -f v23_test_Dockerfile_pyspark_py3_spk3 .
    docker build -t pyspark3_sub -f v23_Dockerfile_pyspark_py3_spk3 .

Get into console

    docker run --rm -dti -v $PWD:/home/jovyan/SparkProjects/Project1 --name spark_test pyspark3_test '/bin/bash'

    docker exec -it spark_test '/bin/bash'

In you current directory ($PWD root) has to exist the spark_submit.sh file, then run:

    docker run --rm -d -v $PWD:/home/jovyan/SparkProjects/Project1 pyspark3_sub

And you pyspark code will run, when it finishes the docker container finishes also.
