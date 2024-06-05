from pyspark.sql import SparkSession

def transform_data():
    spark = SparkSession.builder.appName("TransformData").getOrCreate()
    data = spark.read.parquet('/data/processed/sales_data.parquet')
    # Transformação de exemplo: limpeza de dados
    data = data.dropna()
    data.write.parquet('/data/processed/sales_data_clean.parquet')
    spark.stop()

if __name__ == '__main__':
    transform_data()