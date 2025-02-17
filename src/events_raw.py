"""Ingest my_stream via Delta Live Table"""

import dlt
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

HOST = spark.conf.get("spark.databricks.workspaceUrl")
DBX_HOST_TO_ENV = {
    "{{ dev_host }}": "dev",
    "{{ stage_host }}": "stage",
    "{{ prod_host }}": "prod",
}
ENV = DBX_HOST_TO_ENV.get(HOST, "dev")


def set_kafka_urls() -> str:
    if ENV == "stage":
        bootstrap_urls = [
            "b-5.stage.123abc.a3.kafka.us-east-2.amazonaws.com:9092",
            "b-4.stage.123abc.a3.kafka.us-east-2.amazonaws.com:9092",
            "b-1.stage.123abc.a3.kafka.us-east-2.amazonaws.com:9092",
        ]
    elif ENV == "prod":
        bootstrap_urls = [
            "b-3.prod.456def.a10.kafka.us-east-2.amazonaws.com:9092",
            "b-6.prod.456def.a10.kafka.us-east-2.amazonaws.com:9092",
            "b-1.prod.456def.a10.kafka.us-east-2.amazonaws.com:9092",
        ]
    else:
        bootstrap_urls = ["b-5.devel.789ghi.a3.kafka.us-east-2.amazonaws.com:9092"]
    return ",".join(bootstrap_urls)


KAFKA_URLS = set_kafka_urls()


@dlt.table
def my_stream():
    return (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_URLS)
        .option("subscribe", KAFKA_TOPIC)
        .option("startingOffsets", "latest")
        .option("failOnDataLoss", "false")
        .load()
    )
