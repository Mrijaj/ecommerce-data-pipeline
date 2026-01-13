from pyspark.sql.functions import col, to_date, sum as _sum, count
from spark.utils.spark_session import get_spark_session

spark = get_spark_session("DailySalesAggregation")

# Read RAW orders
orders_df = spark.read.parquet("storage/raw/orders")

# Convert order_time to date
orders_df = orders_df.withColumn(
    "order_date",
    to_date(col("order_time"))
)

# Aggregate daily sales
daily_sales_df = orders_df.groupBy(
    "order_date", "city"
).agg(
    _sum("price").alias("total_revenue"),
    count("*").alias("total_orders")
)

# Write CURATED data
daily_sales_df.write \
    .mode("overwrite") \
    .partitionBy("order_date") \
    .parquet("storage/curated/daily_sales")

spark.stop()
