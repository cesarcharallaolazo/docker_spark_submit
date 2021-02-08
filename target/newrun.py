from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

from utils.settings import ROOT_PATH, CHECKPOINT_PATH


if __name__ == '__main__':

    # Start Spark Environment
    spark = SparkSession.builder.getOrCreate()

    # Checkpointing tuning strategy
    sc = SparkContext.getOrCreate()
    sc.setCheckpointDir(CHECKPOINT_PATH)

    # spark logic
    print("Spark pipeline")






