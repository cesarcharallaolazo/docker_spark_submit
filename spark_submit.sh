make build &&\
cd target &&\

spark_submit_cmd="spark-submit --master local[*] --deploy-mode client --py-files spark.zip newrun.py "
eval $spark_submit_cmd
