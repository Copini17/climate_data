from pyspark.sql import SparkSession

def extract_data():
    spark = SparkSession.builder.appName("ExtractData").getOrCreate()
    data = spark.read.csv('/data/raw/sales_data.csv', header=True, inferSchema=True)
    data.write.parquet('/data/processed/sales_data.parquet')
    spark.stop()

if __name__ == '__main__':
    extract_data()