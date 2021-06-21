make build &&\
cd target &&\

spark_submit_cmd="spark-submit --jars /home/jovyan/SparkProjects/Project1/jars/com.github.luben_zstd-jni-1.4.4-3.jar,/home/jovyan/SparkProjects/Project1/jars/org.apache.commons_commons-pool2-2.6.2.jar,/home/jovyan/SparkProjects/Project1/jars/org.apache.kafka_kafka-clients-2.4.1.jar,/home/jovyan/SparkProjects/Project1/jars/org.apache.spark_spark-sql-kafka-0-10_2.12-3.0.1.jar,/home/jovyan/SparkProjects/Project1/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.12-3.0.1.jar,/home/jovyan/SparkProjects/Project1/jars/org.lz4_lz4-java-1.7.1.jar,/home/jovyan/SparkProjects/Project1/jars/org.slf4j_slf4j-api-1.7.30.jar,/home/jovyan/SparkProjects/Project1/jars/org.spark-project.spark_unused-1.0.0.jar,/home/jovyan/SparkProjects/Project1/jars/org.xerial.snappy_snappy-java-1.1.7.5.jar --master local[*] --deploy-mode client --py-files spark.zip newrun.py --root_path /home/jovyan/SparkProjects/Project1/source_data --checkpoint_path /home/jovyan/SparkProjects/Project1/source_data/checkpoints/"
eval $spark_submit_cmd