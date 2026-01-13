from pyspark.sql import SparkSession


def get_spark_session(app_name: str):
    """
    Creates and returns a SparkSession.
    Reused across batch and streaming jobs.
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "2") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")
    return spark
