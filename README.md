# Ecommerce Data Pipeline

End-to-end real-time data engineering pipeline using Kafka, Spark Streaming, and Spark Batch.

## Architecture
Producer → Kafka → Spark Streaming → Raw Layer → Batch Aggregation → Curated Layer

## Tech Stack
- Python
- Apache Kafka
- Apache Spark (Structured Streaming)
- Docker & Docker Compose

## How to Run
1. docker-compose up -d
2. python -m kafka_client.producer_orders
3. python spark/streaming/process_orders_stream.py
4. python -m spark.batch.daily_sales_aggregation

## Output
- Raw orders stored as Parquet
- Daily sales aggregated by date, city, product
