from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark import SparkContext

spark = SparkSession.builder.appName("Prueba_Spark").getOrCreate()

inputfileDF = spark.read.text("hdfs://localhost/user/training/input.txt")

filteredDF = inputfileDF.filter(inputfileDF.value.contains("segunda"))

filteredDF.take(3)

# Mostrar un Dataframe de Spark
inputfileDF.show()

sc = SparkContext.getOrCreate(SparkConf())
entradaRDD = sc.wholeTextFiles(path="hdfs://localhost/user/training/input.txt")

print(entradaRDD.take(3))

spark.stop()