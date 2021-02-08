from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

from credit.features import features_50_var
from credit.pre_features import raw_usable_rcc_data
from credit.pre_features import unify_rcc
from credit.pre_features import extract_rcc_population
from credit.train import train
from credit.predict import predict
from credit.train import balancing
from credit.segmentation import segmentation
from utils.settings import ROOT_PATH, CHECKPOINT_PATH


if __name__ == '__main__':

    # Start Spark Environment
    spark = SparkSession.builder.getOrCreate()

    # Checkpointing tuning strategy
    sc = SparkContext.getOrCreate()
    sc.setCheckpointDir(CHECKPOINT_PATH)

    # Input data
    df_customers = spark.read.csv(ROOT_PATH + 'rappi_buro/match_codsbs.csv', header=True,
                   schema=StructType([
                            StructField("CODSBS", StringType(), True)
                                    ])
                   )

    # Standardization & union raw data step
    unify_rcc.union_rcc_all_three(spark)# huge IO processes

    # Pre-feature engineering step
    extract_rcc_population.extract_specific_customers_all(spark, df_customers) # huge computation
    unify_rcc.union_rcc_various_cohort_sampled(spark)

    # Feature Engineering step
    features_50_var.credit_features(spark)

    #print("RAPPI BURO MODEL !!")
    # print(sc.version)
    #
    # df_customers.show(truncate=False)
    # print(df_customers.count())

    # rcc_month = '201906'
    # df1 = spark.read.parquet(ROOT_PATH + f"pre_features/three_customers_sampled/customers_{int(rcc_month)}_sampled.parquet")
    # df1.show(truncate=False)
    # print(df1.select("CODSBS").distinct().count())






