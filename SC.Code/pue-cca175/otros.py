"""
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPAT

en mi ubuntu: spark/spark-3.0.0-preview2-bin-hadoop3.2/python/lib/py4j-0.10.8.1-src.zip
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.8.1-src.zip:$PYTHONPAT

export PYSPARK_DRIVER_PYTHON=ipython
PYSPARK_DRIVER_PYTHON_OPTS=ipython
pyspark
"""
# add todo el fichero al final de scelisexercises.txt
#TODAS LAS SALIDAS LAS HE DEJADO EN EL MISMO SITIO: "dataset/solutions/sce/"
#
#--------------------------------------Scenario 1.--------------------------------------
"""
Data description
All the customer records are stored in the HDFS directory dataset/retail_db/customers-tab-delimited
Data is in text format
Data is tab delimited
Schema is: 
customer_id int,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
Requerimientos de salida
Output all the customers who live in California
Use text format for the output files
Result should only contain records that have state value as "CA"
Output should only contain customer's full name. Example: Robert Hudson
"""
"""

ls -l /tmp/dataset/retail_db/customers-tab-delimited

hdfs dfs -put /tmp/dataset/retail_db/customers-tab-delimited dataset/retail_db/customers-tab-delimited

hdfs dfs -ls dataset/retail_db/customers-tab-delimited

hdfs dfs -rm -R dataset/solutions/sce01/
"""
#--------------------------------------pyspark

in_dir = "dataset/retail_db/customers-tab-delimited"
out_dir = "dataset/solutions/sce01/"

from pyspark.sql.types import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
from pyspark.sql.functions import split

dfColumns = [
StructField ("customer_id", LongType()),
StructField ("customer_fname", StringType()),
StructField ("customer_lname", StringType()),
StructField ("customer_email", StringType()),
StructField ("customer_password", StringType()),
StructField ("customer_street", StringType()),
StructField ("customer_city", StringType()),
StructField ("customer_state", StringType()),
StructField ("customer_zipcode", StringType())
]
 
dfSchema = StructType( dfColumns )

DFIn = ( spark. read. schema( dfSchema ). option( "sep", "\t" ). csv( in_dir ) )
DFIn.printSchema()

DFOut = ( DFIn. 
filter( col( "customer_state" ) == "CA" ).
select( concat_ws ( " ", col ( "customer_fname" ) , col( "customer_lname" ) ) ) )

DFOut. show()
DFOut.printSchema()

DFOut. write. mode( "overwrite" ). text( out_dir )

#------------------

DFIn = ( spark. read. option( "inferSchema", "true" ). option( "sep", "\t" ).csv( in_dir ) )
DFIn.printSchema()

DFOut = ( DFIn. 
select( col ( "_c1" ) , col( "_c2" ), col( "_c7" ) ).
filter( col( "_c7" ) == "CA" ).
select( concat_ws ( " ", col ( "_c1" ) , col( "_c2" ) ) ) )

DFOut. show()
DFOut.printSchema()

DFOut. write. mode( "overwrite" ). text( out_dir )

#------------------

DFIn = ( spark. read. option( "inferSchema", "true" ). option( "sep", "\t" ). format ( "csv" ). load( in_dir ) )
DFIn.printSchema()

DFOut = ( DFIn. 
select( col ( "_c1" ) , col( "_c2" ), col( "_c7" ) ).
filter( col( "_c7" ) == "CA" ).
select( concat_ws ( " ", col ( "_c1" ) , col( "_c2" ) ) ) )

DFOut. show()
DFOut.printSchema()

DFOut. write. mode( "overwrite" ). text( out_dir )

#------------------

#------------------

( spark. read. option( "inferSchema", "true" ). option( "sep", "\t" ). format ( "csv" ). load( in_dir ).
select( col ( "_c1" ) , col( "_c2" ), col( "_c7" ) ).
filter( col( "_c7" ) == "CA" ).
select( concat_ws ( " ", col ( "_c1" ) , col( "_c2" ) ) ). 
write. 
mode( "overwrite" ). 
text( out_dir ) )

#------------------

#------------------

( spark.read.
option("sep", "\t").
csv( in_dir ).
select( "_c1", "_c2", "_c7").
filter( col("_c7") == "CA" ).
select( concat_ws( " ", col("_c1"), col("_c2") ) ).
write.
mode( "overwrite" ).
text( out_dir ) )

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""

( spark.read. option( "inferSchema", True ). option( "delimiter", "\t"). csv( in_dir ). toDF(
"customer_id",
"customer_fname",
"customer_lname",
"customer_email",
"customer_password",
"customer_street",
"customer_city",
"customer_state",
"customer_zipcode").
createOrReplaceTempView( "customer_view") )

(spark.sql (
"""
SELECT concat_ws( " ", customer_fname, customer_lname)
FROM customer_view
WHERE customer_state = 'CA'
""").
write.
mode( "overwrite" ).
text( out_dir ) )

#------------------ Comprobación

( spark.read. text( out_dir ).  orderBy( "value" ).  show( 10 ) )

#OJO esta comprobación no me funciono
( spark. read. text( out_dir ).
select( split( col("i"), " ")[0]. alias( "first_name"), split( col("i"), " ")[1]. alias( "last_name" ) ).
show( 5 ) )

#--------------------------------------EndScenario 1.--------------------------------------

#--------------------------------------StartScenario 2.--------------------------------------
"""
Data description
All the order records are stored in HDFS directory dataset/retail_db/orders_parquet.
Data is in parquet format.
Output requirements
Output all the completed orders (where order_status is 'COMPLETE')
Use json format for the output files
order_date should be in format yyyy-MM-dd
Compress the output using gzip compression
Output should only contain order_id, order_date, order_status.
fechas : https://sparkbyexamples.com/spark/spark-sql-unix-timestamp/
"""
"""

ls /tmp/dataset/retail_db/orders_parquet

hdfs dfs -put /tmp/dataset/retail_db/orders_parquet dataset/retail_db/orders_parquet 

hdfs dfs -ls dataset/retail_db/orders_parquet

hdfs dfs -rm -R dataset/solutions/sce02/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col

in_dir = "dataset/retail_db/orders_parquet"
out_dir = "dataset/solutions/sce02/"

DFIn = ( spark. read. parquet ( in_dir ) )
DFIn.printSchema()

Out = ( DFIn. filter ( col( "order_status" ) == 'COMPLETE' ).
drop ( col( "order_customer_id" ) ).
withColumn( "order_date", from_unixtime( col("order_date")/1000, "yyyy-MM-dd" ) ).
select ( col( "order_date" ), col( "order_id" ), col( "order_status" ) ).
write.
option( "compression", "gzip" ).
mode( "overwrite" ).
json( out_dir )
)

#------------------

#------------------

DFIn = ( spark. read. parquet ( in_dir ) )
DFIn.printSchema()

DFOut = ( DFIn. filter ( col( "order_status" ) == 'COMPLETE' ).
drop ( col( "order_customer_id" ) ).
withColumn( "order_date", from_unixtime( col("order_date")/1000, "yyyy-MM-dd" ) ).
select ( col( "order_date" ), col( "order_id" ), col( "order_status" ) )
)

DFOut.printSchema()
DFOut. show()

DFOut. write. mode( "overwrite" ). option( "compression", "gzip" ). json( out_dir )

#------------------

(spark.read.  load( in_dir ).
filter( "order_status = 'COMPLETE'" ).
drop( "order_customer_id" ).  withColumn( "order_date", from_unixtime( "order_date"/1000, "yyyy-MM-dd" ) ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
json( out_dir )
)

#------------------ Comprobación

( spark.read.  json( out_dir ). orderBy( "order_id" ). show( 10, truncate=False ) )

#--------------------------------------EndScenario 2.--------------------------------------

#--------------------------------------StartScenario 3.--------------------------------------
"""
Data description
All the customer records are stored in the HDFS directory dataset/retail_db/customers-tab-delimited
Data is in text format
Data is tab delimited
Schema is:
customer_customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
Output requirements
Place the result data in HDFS directory dataset/result/scenario3/solution
Result should only contain records that have customer_city as "Caguas"
Compress the output using snappy compression
The orc column names in the orc schema should have the names indicated above.
Save the output using orc format.
"""
"""
https://sparkbyexamples.com/spark/spark-read-orc-file-into-dataframe/
"""
"""
ls /tmp/dataset/retail_db/customers-tab-delimited

hdfs dfs -put /tmp/dataset/retail_db/customers-tab-delimited 

hdfs dfs -ls dataset/retail_db/customers-tab-delimited dataset/retail_db/customers-tab-delimited

hdfs dfs -rm -R dataset/solutions/sce03/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dir = "dataset/retail_db/customers-tab-delimited"
out_dir = "dataset/solutions/sce03/"

DFIn = ( spark. read. option( "inferSchema", "true" ). option ( "sep", "\t" ). csv ( in_dir ). toDF( ( "customer_customer_id" ), ( "customer_fname" ), ( "customer_lname" ), ( "customer_email" ), ( "customer_password" ), ( "customer_street" ), ( "customer_city" ), ( "customer_state" ), ( "customer_zipcode" ) ) )
DFIn.printSchema()

DFOut = (
DFIn. filter( col ( "customer_city" ) == "Caguas" ).
withColumn ( "customer_customer_id" , DFIn.customer_customer_id. cast( "int" ) )
)

DFOut.write .option( "compression", "snappy" ) .mode( "overwrite" ) .orc( out_dir )

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
(spark.read.
option( "delimiter", "\t").
csv( in_dir ).
toDF(
"customer_customer_id", "customer_fname",
"customer_lname",
"customer_email",
"customer_password", "customer_street",
"customer_city",
"customer_state",
"customer_zipcode").
filter( "customer_city = 'Caguas'" ).
withColumn( "customer_customer_id", col("customer_customer_id").cast("int") ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
orc( out_dir ) )

#------------------ Comprobación

( spark.read.  orc( out_dir ).  select( "customer_customer_id", "customer_fname", "customer_lname", "customer_street" ).
orderBy( "customer_customer_id" ).  show( 10, truncate=False ) )

#--------------------------------------EndScenario 3.--------------------------------------

#--------------------------------------StartScenario 4.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories.
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Output requirements
Convert data into tab delimited file
Use text format for the output files
Place de result data in HDFS directory dataset/result/scenario4/solution
Compress the output using lz4 compression
"""
"""

ls /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories
hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/sce04/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/categories/"
out_dir = "dataset/solutions/sce04/"

DFIn = (spark. read. option( "inferSchema", "true" ). csv( in_dir ))
DFIn.printSchema()


Out = (DFIn.
withColumn ( "value", concat_ws( '\t', "_c0", "_c1", "_c2") ).
drop ( "_c0", "_c1", "_c2" ).
write.
mode( "overwrite" ).
option ( "compression", "lz4" ).
csv( out_dir )
)

#------------------

DFIn = (spark. read. csv( in_dir ))
DFIn.printSchema()

from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

Out = (DFIn.
withColumn ( "_c0", col( "_c0" ). cast ( "int" ) ).
withColumn ( "_c1", col( "_c1" ). cast ( "int" ) ).
withColumn ( "value", concat_ws( '\t', "_c0", "_c1", "_c2" ) ).
drop ( "_c0", "_c1", "_c2" ).
write.
mode( "overwrite" ).
option ( "compression", "lz4" ).
csv( out_dir )
)

#------------------

#------------------

(spark. read. csv( in_dir ).
withColumn ( "_c0", col( "_c0" ). cast ( "int" ) ).
withColumn ( "_c1", col( "_c1" ). cast ( "int" ) ).
withColumn ( "value", concat_ws( '\t', "_c0", "_c1", "_c2" ) ).
drop ( "_c0", "_c1", "_c2" ).
write.
mode( "overwrite" ).
option ( "compression", "lz4" ).
csv( out_dir ) )

#------------------

#------------------

(spark.read.
csv( in_dir ).
selectExpr( "concat_ws('\t', * ) value" ).
write.
mode( "overwrite" ).
option( "compression", "lz4" ).
csv( out_dir ) )

#------------------ Comprobación

(spark.read.  text( out_dir ).  orderBy( "value" ).  show( 10 , truncate=False ) )

#--------------------------------------EndScenario 4.--------------------------------------

#--------------------------------------StartScenario 5.--------------------------------------
"""
Data description
All the products records are stored at dataset/retail_db/products_avro
Data is in avro format
Data is compressed with snappy compression
Output requirements
Outuput should only contain the products with price greater than 1000.0
Use parquet format for the outuput files
Compress the output using snappy compression
No se puede leer directamente con el método avro; no existe. Hay que usar format("avro") y luego load.
save escribe directamente en formato parquet con compresión snappy.
"""
"""
ls /tmp/dataset/retail_db/products_avro

hdfs dfs -put /tmp/dataset/retail_db/products_avro dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro

hdfs dfs -rm -R dataset/solutions/sce05/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/products_avro/"
out_dir = "dataset/solutions/sce05/"

DFIn = ( spark. read. format( 'avro' ). option( "compression", "snappy" ). load( in_dir ) )
DFIn.printSchema()

Out = (
DFIn.
filter ( col( "product_price" ) > 1000.0 ).
select ( col( "product_id" ), col( "product_name" ), col ( "product_price" ) ).
orderBy( col ( "product_id" ), col ( "product_price" ). desc() ).
write.
mode( "overwrite" ).
save( out_dir )
)

#------------------

#------------------

( spark. read. format( 'avro' ). option( "compression", "snappy" ). load( in_dir ).

filter ( col( "product_price" ) > 1000.0 ).
select ( col( "product_id" ), col( "product_name" ), col ( "product_price" ) ).
orderBy( col ( "product_id" ), col ( "product_price" ). desc() ).
write.
mode( "overwrite" ).
save( out_dir )
)

#------------------

#------------------

(spark.read.
format( "avro" ).
load( in_dir ).
filter( "product_price > 1000" ).
write.
mode( "overwrite" ).
save( out_dir ) )

#------------------ Comprobación

( spark.read.
load( out_dir ).
select( "product_id", "product_name", "product_price" ).
orderBy( "product_id" ).
show( 10, truncate=False ) )

#--------------------------------------EndScenario 5.--------------------------------------

#--------------------------------------StartScenario 6.--------------------------------------
"""
Data description
Get data from metastore table named orders.
Table is present in the database default.
Output requirements
Fetch orders from Jan-2013 to Dec-2013.
Use parquet format for the output files.
Compress the output using gzip compression.
"""
"""
hdfs dfs -rm -R dataset/solutions/sce06/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "orders"
out_dir = "dataset/solutions/sce06/orders"

DFIn = ( spark.read.table( in_dir ) )
DFIn.printSchema()

Out = ( DFIn.
filter( "year(order_date ) = 2013" ).
select ( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
save( out_dir ))

"""
withColumn( "order_date", to_timestamp ( col( "order_date" ), "yyyy-MM-dd hh:mm:ss" ) )
withColumn( "order_date", to_date( col( "order_date" ), "yyyy-MM-dd hh:mm:ss" ) )
"""

#------------------

#------------------

( spark.read.table( in_dir ).
filter( "year(order_date ) = 2013" ).
select ( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
save( out_dir ) )
#------------------

#------------------

(spark.read.
table( in_dir ).
filter( "year(order_date ) = 2013" ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
save( out_dir ) )

#------------------

(spark.sql(
"""
SELECT * FROM orders
WHERE year( order_date ) = '2013'
""").
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
save( out_dir ) )

#------------------ Comprobación

(spark.read.  load( out_dir ).  orderBy( "order_id" ).  show( 10 ) )

#--------------------------------------EndScenario 6.--------------------------------------

#--------------------------------------StartScenario 7.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories.
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Output requirements
Save all categories in metastore table categories_replica in scenario7_db database
Use no compression
Si se pone format( "hive" ), la tabla se crea con formato texto. Si no se pone format( "hive" ) se crea en formato parquet.
"""
"""
ls /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/sce07/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/sce07/"
out_table = "scenario7db.categories_replica"

DFIn = ( spark. read. csv( in_dir ). toDF( "category_id", "category_department_id", "category_name") )
DFIn.printSchema()

spark.sql( "CREATE database if not exists scenario7db" )

Out = ( DFIn.
withColumn ( ("category_id"), col ( "category_id" ). cast( "int" ) ).
withColumn ( ("category_department_id"), col ( "category_department_id" ). cast( "int" ) ).
withColumn ( ("category_name"), col ( "category_name" ) ).
write.
mode( "overwrite" ).
format ( "hive" ).
option( "compression", "none" ).
option( "path", out_dir ).
saveAsTable( out_table )
)

#------------------

spark.sql( "CREATE database if not exists scenario7db" )

Out = ( DFIn.
withColumn ( ("category_id"), col ( "category_id" ). cast( "int" ) ).
withColumn ( ("category_department_id"), col ( "category_department_id" ). cast( "int" ) ).
withColumn ( ("category_name"), col ( "category_name" ) ).
write.
mode( "overwrite" ).
format ( "hive" ).
option( "compression", "none" ).
option( "path", out_dir ).
saveAsTable( out_table )
)
#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
spark.sql( "CREATE database if not exists scenario7_db" )

(spark.read.
option( "inferSchema", True).
csv( in_dir ).
toDF( "category_id", "category_department_id", "category_name" ).
write.
format( "hive" ).
mode( "overwrite" ).
option( "compression", "uncompressed" ).
saveAsTable( out_dir ) )


#------------------ Comprobación

in_dir = out_dir

df = ( spark.read.table( in_dir ) )
df.printSchema( )  
df.orderBy( "category_id" )
df.show( 10 )
#--------------------------------------EndScenario 7.--------------------------------------

#--------------------------------------StartScenario 8.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories.
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Output requirements
Create a metastore table named categories_parquet.
Table should only contain category_id, category_name.
Use parquet format for the output files.
Si no se pone format( "hive" ) se crea en formato parquet.
save table escribe directamente en formato parquet con compresión snappy.
"""
"""
ls /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/sce08/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/categories"
out_table = "default.categories_parquet"
out_dir = "dataset/solutions/sce08/"

DFIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dir ) )
DFIn.printSchema()

Out = ( 
DFIn.
withColumn( col( "_c0" ), col( "category_id" ). cast( "int" ) ).
withColumn( col( "_c1" ), col( "category_name" ) ).
select( col( "category_id" ), col( "category_name" ) ).
write.
mode( "overwrite" ).
saveAsTable( out_table )
)


#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
(spark.read.
option( "inferSchema", True).
csv( in_dir ).
drop( "_c1" ).
toDF( "category_id", "category_name" ).
write.
mode( "overwrite" ).
saveAsTable( out_table ) )

#------------------ Comprobación

(spark.read.table( out_table ).  orderBy( "category_id" ).  show( 10 ) )

#--------------------------------------EndScenario 8.--------------------------------------

#--------------------------------------StartScenario 9.--------------------------------------
"""
Data description
All the products records are stored at dataset/retail_db/products_avro
Data is in avro format
Data is compressed with snappy compression
Output requirements
Output should contain columns product_id, product_price.
Save output as json file
Use no compression
json no se comprime por omisión. Por lo tanto no hace falta poner nada. 
Para indicar que no hay compresión, hay dos posibilidades:
option( "compression", "uncompressed")
option( "compression", "none")
read avro, snappy Hay que usar format("avro") y luego load.
"""
"""
ls /tmp/dataset/retail_db/products_avro

hdfs dfs -put /tmp/dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro dataset/retail_db/products_avro

hdfs dfs rm -R dataset/solutions/sce09/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/products_avro"
out_dir = "dataset/solutions/sce09/"

DFIn = ( spark.  read.  format( "avro" ).  load( in_dir ) )
DFIn.printSchema()

Out = ( DFIn.
select ( col( "product_id" ), col( "product_price" ) ).
write.
mode( "overwrite" ).
json( out_dir ).
option( "compression", "none" ) )

#------------------

(spark.read.
format( "avro" ).
load( "dataset/retail_db/products_avro" ).
select( "product_id", "product_price" ).
write.
mode( "overwrite" ).
json( out_dir ) )

#------------------ Comprobación

(spark.read.  json( out_dir ). orderBy( "product_id" ).  show( 10 ) )

#--------------------------------------EndScenario 9.--------------------------------------

#--------------------------------------StartScenario 10.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories.
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Output requirements
Create a metastore table named categories_partitioned. The format of the data must be parquet.
Table must be partitioned by category_department_id.
Save all categories in metastore table categories_partitioned.
save table escribe directamente en formato parquet con compresión snappy.
Si no se pone format( "hive" ) se crea en formato parquet.
"""
"""

ls /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/sce10/

"""

#--------------------------------------pyspark

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/sce10/"

DFIn = ( spark.  read.  option ( "inferSchema", "true" ). csv ( in_dir ) )

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
Out = ( DFIn.
toDF( "category_id", "category_department_id", "category_name" ).
partitionBy( "category_department_id" ).
write.
mode( "overwrite" ).
saveAsTable( out_dir )
)

"""
esto es para probrar en lugar del toDF
select( withColumn( col( "_c0" ), col( "category_id" ) ).  withColumn( col( "_c1" ), col( "category_department_id" ) ). withColumn( col( "_c2" ), col( "category_name" ) ))
ó
select( ( "_c0" ).alias( "category_id" ), ( "_c1" ).alias( "category_department_id" ), ( "_c2" ).alias( "category_name" ) )
"""

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
from pyspark.sql import HiveContext
sqlContext = HiveContext( sc )
sqlContext.setConf( "hive.exec.dynamic.partition", "true" )
sqlContext.setConf( "hive.exec.dynamic.partition.mode", "nonstrict" )

(spark.read.
option( "inferSchema", True).
csv( in_dir ).
toDF( "category_id", "category_department_id", "category_name" ).
write.
format( "parquet" ).
mode( "overwrite" ).
partitionBy( "category_department_id" ).
saveAsTable( "categories_partitioned" ) )

#------------------ Comprobación

(spark.read. table( "categories_partitioned" ). orderBy( "category_id" ).  show( 10 ) )

#--------------------------------------EndScenario 10.--------------------------------------

#--------------------------------------StartScenario 11.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers-avro
Data is in avro format - read Hay que usar format("avro") y luego load.
Output requirements
Convert all data into tab delimited file
Use text format for the outupt files
Use bzip2 compression
Ouput should only contain customer_id, customer_name
customer_name is first caracter of first name and complete last name separated by space.
A la hora de leer, no es necesario indicar que los datos están comprimidos. Spark se da cuenta y los descomprime. 
Es más, si se indica un formato incorrecto, por ejemplo, gzip en vez de bzip2, Spark lee correctamente.
"""
"""
ls /tmp/dataset/retail_db/customers-avro

hdfs dfs -put /tmp/dataset/retail_db/customers-avro dataset/retail_db/customers-avro

hdfs dfs -ls dataset/retail_db/customers-avro

hdfs dfs -rm -R dataset/solutions/sce11/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
from pyspark.sql.functions import substring

in_dir = "dataset/retail_db/customers-avro"
out_dir = "dataset/solutions/sce11/"

DFIn = ( spark.read.  format( "avro" ). load( in_dir ) )

Out = (DFIn.
select ( col ( "customer_id" ), col( "customer_fname" ), col( "customer_lname" ), col( "customer_email" ) ).
withColumn ( "customer_fname", substring( col( "customer_fname" ), 1, 1 ) ).
withColumn ( "customer_name", concat_ws(" ", col( "customer_fname" ), col( "customer_lname" ) ) ).
drop ( "customer_fname", "customer_lname", "customer_email" ).
selectExpr ( "concat_ws( '\t', customer_id, customer_name )" ).
write.
mode( "overwrite" ).
option ( "compression", "bzip2" ).
text( out_dir_dir )
)

#------------------
(spark.read.
format( "avro" ).
load( in_dir ).
select( "customer_id", "customer_fname", "customer_lname").
withColumn( "customer_fname", substring( col("customer_fname"), 1, 1 ) ).
withColumn( "customer_name", concat_ws( " ", col("customer_fname"), col("customer_lname" ) ) ).
select( "customer_id", "customer_name" ).
select( concat_ws( "\t", col("customer_id"), col("customer_name" ) ) ).
write.
mode( "overwrite" ).
option( "compression", "bzip2" ).
text( out_dir ) )

#------------------

(spark.read.
format( "avro" ).
load( in_dir ).
select( "customer_id", "customer_fname", "customer_lname").
createOrReplaceTempView( "customers" ) )
(spark.sql(
"""
SELECT customer_id,
concat_ws( ' ',
substring( customer_fname, 1, 1 ), customer_lname) customer_name
FROM customers
""").
selectExpr( "concat_ws( '\t', customer_id, customer_name )" ).
write.
mode( "overwrite" ).
option( "compression", "bzip2").
text( out_dir ) )

#------------------

#------------------ Comprobación

(spark. read.  option( "sep", "\t" ).  csv( out_dir ).  show( 10 ) )

#--------------------------------------EndScenario 11.--------------------------------------

#--------------------------------------StartScenario 12.--------------------------------------
"""
Data description
All the order records are stored in HDFS directory dataset/retail_db/orders_parquet.
Data is in parquet format.
Output requirements
Output all the PENDING orders in July 2013
Use json format for the output files
order_date should be in format yyyy-MM-dd.
Compress the output using snappy compression and output should only contain order_date, order_status.
"""
"""
??? json no se comprime por omisión. Por lo tanto no hace falta poner nada. 
"""
"""

ls /tmp/dataset/retail_db/orders_parquet

hdfs dfs -put /tmp/dataset/retail_db/orders_parquet dataset/retail_db/orders_parquet

hdfs dfs -ls dataset/retail_db/orders_parquet

hdfs dfs -rm -R dataset/solutions/sce12/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/orders_parquet"
out_dir = "dataset/solutions/sce12/"

DFIn = (spark. read. parquet( in_dir ))
DFIn.printSchema()

Out = (DFIn.
filter ( col ( "order_status" ) == 'PENDING' ).
withColumn( "order_date", from_unixtime( col( "order_date" )/1000, "yyyy-MM-dd" ) ).
select ( col ( "order_date" ), col( "order_status" ) ).
filter ( "order_date BETWEEN '2013-07-01' AND '2013-07-31' " ).
write.
mode( "overwrite" ).
option ( "compression", "snappy" ).
json( out_dir ) )

#------------------

DFIn = (spark. read. parquet( in_dir ))
DFIn.printSchema()

from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

Out = (DFIn.
filter ( col ( "order_status" ) == 'PENDING' ).
withColumn( "order_date", from_unixtime( col( "order_date" )/1000, "yyyy-MM-dd" ) ).
select ( col ( "order_date" ), col( "order_status" ) ).
filter ( "year(order_date) = '2013' AND month(order_date) = '07'" ).
write.
mode( "overwrite" ).
option ( "compression", "snappy" ).
json( out_dir )
)

#------------------

#------------------

DFIn = (spark. read. parquet( in_dir ))
DFIn.printSchema()

Out = (DFIn.
filter ( col ( "order_status" ) == 'PENDING' ).
withColumn( "order_date", from_unixtime( col( "order_date" )/1000, "yyyy-MM-dd" ) ).
select ( col ( "order_date" ), col( "order_status" ) ).
filter ( "year(order_date) = '2013' AND month(order_date) = '07'" ).
write.
mode( "overwrite" ).
option ( "compression", "snappy" ).
json( out_dir )
)

#------------------

(spark.read.
load( in_dir ).
select( "order_date", "order_status" ).
filter( col( "order_status") == "PENDING" ).
withColumn(
"order_date",
to_date( from_unixtime( col("order_date") / 1000 ) ) ).
filter( col("order_date").like("2013-07%") ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
json( out_dir ) )

#------------------

#------------------ Comprobación

(spark. read. json( out_dir ). orderBy ( "order_date" ). show( 10 ) )

#--------------------------------------EndScenario 12.--------------------------------------

#--------------------------------------StartScenario 13.--------------------------------------
"""
Data description
Get data from metastore table named customers.
Table is present in the database default.
Output requirements
Get records from the metastore table named customers whose customer_fname is like Rich.
Use parquet file for the outuput files.
Compress the output using snappy compression.
Con poner save es suficiente. Spark usa format parquet y snappy compression por omisión.
"""
"""
hdfs dfs -rm -R dataset/solutions/sce13/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col

in_dir = "default.customers"
out_dir = "dataset/solutions/sce13/customers"

DFIn = ( spark. read. table ( in_dir ) ) 
DFIn.printSchema()

Out = ( DFIn.
select ( ( "customer_fname" ) ).
filter ( ( "customer_fname == %Rich " ) ).
select ( ( "customer_id" ), ( "customer_fname" ), col( "customer_lname" ) ).
write.
mode( "overwrite" ).
save( out_dir )
)


#------------------

(spark.sql(
"""
SELECT * FROM customers
WHERE customer_fname LIKE 'Rich%'
""").
write.
mode( "overwrite" ).
save( out_dir ) )

#------------------

#------------------ Comprobación

in_dir = out_dir

(spark.read.  load( "dataset/result/scenario13/solution" ).  orderBy( "customer_id" ).  show( 10, truncate=False ) )

#--------------------------------------EndScenario 13.--------------------------------------

#--------------------------------------StartScenario 14.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers-tab-delimited.
Data is in text format
Data is tab delimited
Schema is:
customer_customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
Output requirements
Get total number of customers in each state whose first name starts with M.
Use parquet format for the ouput files
Use gzip compression
Output should only contain the columns customer_state, count.
"""
"""
ls /tmp/dataset/retail_db/customers-tab-delimited

hdfs dfs -put /tmp/dataset/retail_db/customers-tab-delimited dataset/retail_db/customers-tab-delimited

hdfs dfs -ls dataset/retail_db/customers-tab-delimited

hdfs dfs -rm -R dataset/solutions/sce14/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/customers-tab-delimited"
out_dir = "dataset/solutions/sce14/"

DFIn = ( spark. read. option( "inferSchema", "true" ). option ( "sep", "\t" ). csv ( in_dir ) )
DFIn.printSchema()


Out = (DFIn.
select ( "_c7", "_c1" ).
withColumn( "customer_fname", substring( col( "_c1" ), 1, 1 ) == 'M' ).
withColumn( "customer_state", col( "_c7" ) ).
drop( "_c7", "_c1" ).
groupBy( col( "customer_state" ) ).count().
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
save( out_dir )
)

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
from pyspark.sql.functions import col
(spark.read.
option("sep", "\t").
csv( in_dir ).
select( "_c1", "_c7").
toDF( "customer_name", "customer_state" ).
filter( "customer_name like 'M%'" ).
groupBy( col("customer_state" ) ).
count( ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
parquet( out_dir ) )

#------------------

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
(spark.read.
option("sep", "\t").
csv( in_dir ).
select( "_c1", "_c7").
toDF( "customer_name", "customer_state" ).
createOrReplaceTempView( "customers" ) )
(spark.sql(
"""
SELECT customer_state, COUNT(*) count
FROM customers
WHERE customer_name LIKE 'M%'
GROUP BY customer_state
""").
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
parquet( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  load( out_dir ).  orderBy( "customer_state" ).  show( 10 ) ) 

#--------------------------------------EndScenario 14.--------------------------------------

#--------------------------------------StartScenario 15.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers.
Format is csv with no header.
The schema of the customers record is:
customer_customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
All the order records are stored at dataset/retail_db/orders. Format is csv.
Format is csv with no header.
The schema of the orders records is:
order_id int,
order_date string,
order_customer_id int,
order_status string
Output requirements
Find out customers who have made more than 5 orders.
Customer name must start with M.
Use text format for the output files.
Use " | " as field separator.
Use gzip compression.
Place the result data in HDFS directory dataset/result/scenario15/solution
There should be only 1 file in the output
Output should only contain customer_fname, customer_lname, count
Output should be sorted by count in descending order.
"""
"""
ls -l dataset/retail_db/customers
ls -l dataset/retail_db/orders

hdfs dfs -put dataset/retail_db/customers dataset/retail_db/customers
hdfs dfs -put dataset/retail_db/orders dataset/retail_db/orders

hdfs dfs -ls dataset/retail_db/

hdfs dfs -rm -R dataset/solutions/sce15/
"""

#--------------------------------------pyspark
"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dirOne = "dataset/retail_db/customers"
in_dirTwo = "dataset/retail_db/orders"
out_dir = "dataset/solutions/sce15/"

DFCusIn = ( spark.  read.  option( "inferSchema", "true" ). csv( in_dirOne ). toDF ( "customer_customer_id", "customer_fname", "customer_lname", "customer_email", "customer_password", "customer_street", "customer_city", "customer_state", "customer_zipcode") )
DFCusIn.printSchema()

DFOrdIn = ( spark.  read.  option( "inferSchema", "true" ). csv( in_dirTwo). toDF ( "order_id", "order_date", "order_customer_id", "order_status") )

DFOrdIn.printSchema()

DFIn = DFCusIn. join( DFOrdIn, DFOrdIn.order_customer_id == DFCusIn.customer_customer_id )
DFIn. printSchema()

Out = (DFIn.
filter( substring( col( "customer_fname" ), 1, 1 ) == 'M' ).
groupBy ( col( "customer_customer_id" ), col( "customer_fname" ), col( "customer_lname" ) ). count(). alias ( "count" ).
filter ( col( "count" ) > 5 ).
sort( col( "count" ).desc()).
selectExpr ( "concat_ws( '|', customer_fname, customer_lname, count )" ).
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
text( out_dir )
)

#------------------

DFCusIn = ( spark.  read.  option( "inferSchema", "true" ). csv( in_dirOne ). toDF ( "customer_customer_id", "customer_fname", "customer_lname", "customer_email", "customer_password", "customer_street", "customer_city", "customer_state", "customer_zipcode")
)
DFCusIn.printSchema()

DFOrdIn = ( spark.  read.  option( "inferSchema", "true" ). csv( in_dirTwo). toDF ( "order_id", "order_date", "order_customer_id", "order_status")
)
DFOrdIn.printSchema()

DFIn = DFCusIn. join( DFOrdIn, DFOrdIn.order_customer_id == DFCusIn.customer_customer_id )
DFIn. printSchema()

Out = (DFIn.
filter( substring( col( "customer_fname" ), 1, 1 ) == 'M' ).
groupBy ( col( "customer_customer_id" ), col( "customer_fname" ), col( "customer_lname" ) ). count(). alias ( "count" ).
filter ( col( "count" ) > 5 ).
sort( col( "count" ).desc()).
selectExpr ( "concat_ws( '|', customer_fname, customer_lname, count )" ).
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
text( out_dir )
)

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
(spark.read.
csv( "dataset/retail_db/customers" ).
filter( "_c1 like 'M%'" ).
select( "_c0", "_c1", "_c2").
toDF( "customer_id", "customer_fname", "customer_lname").
createOrReplaceTempView( "customers" ) )
(spark.read.
csv( "dataset/retail_db/orders" ).
select( col("_c2").alias( "customer_id" ) ).
createOrReplaceTempView( "orders_view" ) )
(spark.sql(
"""
SELECT customer_fname, customer_lname, COUNT(*) count
FROM CUSTOMERS c
JOIN orders_view o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_fname, c.customer_lname
HAVING COUNT(*) > 5
ORDER BY count DESC
""").
coalesce( 1 ).
selectExpr( "concat_ws('|', *) value" ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
text( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  text( out_dir ).  orderBy( "value" ).  show( 20, truncate=False ) )

#--------------------------------------EndScenario 15.--------------------------------------

#--------------------------------------StartScenario 16.--------------------------------------
"""
Data description
All the order records are stored at dataset/retail_db/orders.
Format of files is csv with no header
The schema of the orders records is:
order_id int,
order_date string,
order_customer_id int,
order_status string
Output requirements
Find all fraud transactions per month
Order status must be equal to SUSPECTED_FRAUD
Use parquet format for the ouput files
Use snappy compression
Output should only contain order_date, count
Use yyyy-MM format for order_date
Output should be sorted by order_date in descending order.
save escribe directamente en formato parquet con compresión snappy.
"""
"""

ls /tmp/dataset/retail_db/orders

hdfs dfs -put /tmp/dataset/retail_db/orders dataset/retail_db/orders
hdfs dfs -ls dataset/retail_db/orders

hdfs dfs -rm -R dataset/solutions/sce16/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dir = "dataset/retail_db/orders"
out_dir = "dataset/solutions/sce16/"

DFIn = ( spark.  read.  option ( "inferSchema", "true" ).  csv ( in_dir) )
DFIn.printSchema()

Out = ( 
DFIn.
select( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
filter( col( "order_status" ) == "SUSPECTED_FRAUD" ).
drop( col( "order_date" ) ).
withColumn ( col( "order_date" ), from_unixtime( col( "order_date" ), "yyyy-MM" ) ).
groupBy( col( "order_date" ) ).count(). alias( "count" ).
orderBy( col( "order_date" ).desc() ).
select( col( "order_date" ), col( "count" ) ).
write.
mode( "overwrite").
save ( out_dir )
)

#------------------
"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""

DFIn = ( spark.  read.  option ( "inferSchema", "true" ).  csv ( in_dir) )
Out = ( DFIn.
select( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
filter( col( "order_status" ) == "SUSPECTED_FRAUD" ).
drop( col( "order_date" ) ).
withColumn ( col( "order_date" ), from_unixtime( col( "order_date" ), "yyyy-MM" ) ).
toDF( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
createOrReplaceTempView( "orders_view" ) )

(spark.sql(
"""
SELECT order_date, COUNT(*) count
FROM orders_view
GROUP BY order_date
ORDER BY order_date DESC
""").
write.
mode( "overwrite").
save( out_dir ) )

#------------------

#------------------

(spark.read.
csv( "dataset/retail_db/orders" ).
filter( col("_c3") == "SUSPECTED_FRAUD" ).
filter( "_c3 = 'SUSPECTED_FRAUD'" ).
select( date_format( col("_c1"), "yyyy-MM").alias( "order_date" ) ).
groupBy( "order_date" ).
count( ).
orderBy( desc("order_date" ) ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
parquet( "dataset/result/scenario16/solution" ) )

#------------------

#------------------ Comprobación

spark.read.  load( out_dir ).  show

#--------------------------------------EndScenario 16.--------------------------------------

#--------------------------------------StartScenario 17.--------------------------------------
"""
Data description
All the product records are stored at dataset/retail_db/products
All the category records are stored at dataset/retail_db/categories
Data is in text format
The schema of the products records is:
product_id int,
product_category_id int,
product_name, string,
product_description string,
product_price double,
product_image string
The schema of the categories records is:
category_id int,
category_department_id int,
category_name string
Output requirements
Get maximum product_price in each product_category
Get minimum product_price in each product_category
Get average product_price in each product_category
Round values to 2 decimal places
Save the output as JSON file
Compress the output using deflate compression
Output data should contain columns category_name, max_price, min_price, avg_price.
A la hora de leer products se puede poner option( "inferSchema", true ); 
de este modo no es necesario hacer el cast de las columnas max_price, min_price, y avg_price a double. 
Con lo cual, se pondría select( $"category_name", format_number( $"max_price", 2 ) alias "max_price", format_number( $"min_price", 2 ) alias "min_price", format_number( $"avg_price", 2 ) alias "avg_price")
format_number se puede evitar con ROUND 
ROUND( MAX( price ), 2) max_price,
ROUND( MIN( price ), 2) min_price,
ROUND( AVG( price ) ,2) avg_price
La función format_number se puede evitar usando el ROUND en la sentencia SQL:
"""
"""

ls -l /tmp/dataset/retail_db/products
ls -l /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/products dataset/retail_db/products
hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/

hdfs dfs -rm -R dataset/solutions/sce17/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dirOne = "dataset/retail_db/products"
in_dirTwo = "dataset/retail_db/categories"

DFPrdIn = ( spark.  read.  option( "inferSchema", "true" ).  text( in_dirOne ) )
DFCatIn = ( spark.  read.  option( "inferSchema", "true" ).  text( in_dirTwo ) )

DFIn = ( DFCatIn. join( DFPrdIn, DFPrdIn.product_category_id == DFCatIn.category_id ) )

out_dir = "dataset/solutions/sce17/"

Out = ( DFIn.
select ( col( "product_category_id" ), col( "product_price" ), col( "category_id" ), col( "category_name" ) ).
groupBy ( col( "product_category_id" ) ).
max( col( "product_price" ) ). round( col( "product_price" ), 2). alias ( "max_price" ).
min( col( "product_price" ) ). round( col( "product_price" ), 2). alias ( "min_price" ).
avg( col( "product_price" ) ). round( col( "product_price" ), 2). alias ( "avg_price" ).
select( col( "category_name" ), col( "max_price" ), col( "min_price" ), col( "avg_price" ) ).
write.
mode( "overwrite" ).
option( "compression", "deflate" ).
json( out_dir )
)

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
DFIn = ( DFCatIn. join( DFPrdIn, DFPrdIn.product_category_id == DFCatIn.category_id ) )

Out = ( 
DFIn.  select ( col( "product_category_id" ), col( "product_price" ), col( "category_id" ), col( "category_name" ) ).
toDF( col( "product_category_id" ), col( "product_price" ), col( "category_id" ), col( "category_name" ) ).
createOrReplaceTempView( "prdcat_view" ) )

(spark.sql(
"""
SELECT product_category_id, category_name, round(max(product_price), 2) as max_price, round(min(product_price), 2) as min_price, round(avg(product_price), 2) as avg_price
FROM prdcat_view
GROUP BY product_category_id, category_name
ORDER BY product_category_id
""").
write.
mode( "overwrite" ).
option( "compression", "deflate" ).
json( out_dir ) )

#------------------

#------------------

from pyspark.sql.functions import *
(spark.read.
option( "inferSchema", True).
csv( in_dirOne ).
select(
col("_c1").alias( "category_id"),
col("_c4").alias( "price" ).cast( "double" ) ).
createOrReplaceTempView( "products" ) )
(spark.read.
option( "inferSchema", True).
csv( in_dirTwo ).
select(
col("_c0").alias( "category_id"),
col("_c2").alias( "category_name" ) ).
createOrReplaceTempView( "categories" ) )
(spark.sql(
"""
SELECT category_name,
round( MAX(price), 2 ) max_price,
round( MIN( price ), 2 ) min_price,
round( AVG( price ), 2 ) avg_price
FROM products p
JOIN categories c
ON p.category_id = c.category_id
GROUP BY c.category_id, category_name
""").
write.
mode( "overwrite" ).
option( "compression", "deflate" ).
json( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  json( out_dir ).  orderBy( "avg_price" ).  show( 10 ) )

#--------------------------------------EndScenario 17.--------------------------------------

#--------------------------------------StartScenario 18.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers.
Format is csv with no header.
The schema of the customers record is:
customer_customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
All the order records are stored at dataset/retail_db/orders. Format is csv.
Format is csv with no header.
The schema of the orders records is:
order_id int,
order_date string,
order_customer_id int,
order_status string
Output requirements
Find out total number of orders placed by each customer in the year 2014
Order status should be COMPLETE
There must be only one output file
Output file must not be compressed and the format should be orc.
Output should only contain customer_fname, customer_lname, orders_count
Output should be sorted by orders_count in descending order.
Aunque se ordene el DataFrame antes de escribirlo a HDFS, a la hora de leer puede que el resultado no esté en orden. 
Cuando se escribe el DataFrame los ficheros resultantes están ordenados de acuerdo al nombre. 
Sin embargo, cuando se leen los ficheros para meterlos en el DataFrame, no se puede predecir, qué ficheros se leerán primero.
one output file coalesce( 1 )
Aunque se ordene el DataFrame antes de escribirlo a HDFS, a la hora de leer puede que el resultado no esté en orden. 
Cuando se escribe el DataFrame los ficheros resultantes están ordenados de acuerdo al nombre. 
Sin embargo, cuando se leen los ficheros para meterlos en el DataFrame, no se puede predecir, qué ficheros se leerán primero.
"""
"""
ls /tmp/dataset/retail_db/customers
ls /tmp/dataset/retail_db/orders

hdfs dfs -put /tmp/dataset/retail_db/customers dataset/retail_db/customers
hdfs dfs -put /tmp/dataset/retail_db/orders dataset/retail_db/orders

hdfs dfs -ls dataset/retail_db/
hdfs dfs -rm -R /dataset/solutions/sce18/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dirOne = "dataset/retail_db/customers"
in_dirTwo = "dataset/retail_db/orders"

out_dir = "dataset/solutions/sce18/ordcus"

DFCusIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dirOne ). toDF ( "customer_customer_id", "customer_fname", "customer_lname", "customer_email", "customer_password", "customer_street", "customer_city", "customer_state", "customer_zipcode") )
DFCusIn.printSchema()

DFOrdIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dirTwo ). toDF ( "order_id", "order_date", "order_customer_id", "order_status") )
DFOrdIn.printSchema()

DFIn = DFCusIn. join( DFOrdIn, DFOrdIn.order_customer_id == DFCusIn.customer_customer_id )
DFIn. printSchema()

Out = (DFIn.
filter ( ( year( col( "order_date" ) ) == 2014 ) & ( col( "order_status" ) == "COMPLETE" ) ).
groupBy ( col( "customer_customer_id" ), col( "customer_fname" ), col( "customer_lname" ) ). count().
withColumnRenamed( "count", "orders_count" ).
select( col( "customer_fname" ), col( "customer_lname" ), col( "orders_count" ) ).
orderBy( desc( col( "orders_count" ) ) ).
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "none" ).
orc( out_dir )
)
 
#------------------

#------------------

#------------------

#------------------

from pyspark.sql.functions import *
(spark.read.
csv( in_dirOne ).
select( "_c0", "_c1", "_c2").
toDF( "customer_id", "customer_fname", "customer_lname").
createOrReplaceTempView( "customers" ) )
(spark.read.
csv( in_dirTwo ).
filter( year(col("_c1")) == 2014 ).
filter( col("_c3") == "COMPLETE" ).
select( col("_c2").alias( "customer_id" ) ).
groupBy( "customer_id" ).
count( ).
withColumnRenamed( "count", "orders_count" ).
createOrReplaceTempView( "orders_view" ) )
(spark.sql(
"""
SELECT customer_fname, customer_lname, orders_count
FROM customers c
JOIN orders_view o
WHERE c.customer_id = o.customer_id
ORDER BY orders_count DESC
"""
).
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "uncompressed" ).
orc( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  orc( out_dir ).  show( 6 ) )

#--------------------------------------EndScenario 18.--------------------------------------

#--------------------------------------StartScenario 19.--------------------------------------
"""
Data description
All the product records are stored at dataset/retail_db/products
All the category records are stored at dataset/retail_db/categories
All the order items records are stored at dataset/retail_db/order_items
Data is in text format
The schema of the products records is:
product_id int,
product_category_id int,
product_name string, 
product_description string,
product_price double,
product_image string,
The schema of the categories records is:
category_id int,
category_department_id int,
category_name string
The schema of the order_items records is:
order_item_id int,
order_item_order_id int,
order_item_product_id int,
order_item_quantity tinyint,
order_item_subtotal double,
order_item_product_price double
Output requirements
Get top five selling products in "Accessories" category
Save the output as text file
Use "|" as field separator
Ouput data should contain columns category_name, product_name, and product_revenue.
product_revenue should be rounded to 2 decimals.
"""
"""
ls /tmp/dataset/retail_db/products
ls /tmp/dataset/retail_db/categories
ls /tmp/dataset/retail_db/order_items

hdfs dfs -put /tmp/dataset/retail_db/products dataset/retail_db/products
hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories
hdfs dfs -put /tmp/dataset/retail_db/order_items dataset/retail_db/order_items

hdfs dfs -rm -R /dataset/solutions/sce19/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dirOne = "dataset/retail_db/order_items"
in_dirTwo = "dataset/retail_db/products"
in_dirThree = "dataset/retail_db/categories"

out_dir = "dataset/solutions/sce19/"

( spark. read. option( "inferSchema", "true" ).  csv( in_dirOne ). 
select( col( "order_item_id" ), col( "order_item_order_id" ), col( "order_item_product_id" ), col( "order_item_quantity" ), col( "order_item_subtotal" ), col( "order_item_product_price" ) ).  createOrReplaceTempView( "order_items_view" ) )

( spark. read. option( "inferSchema", "true" ). csv( in_dirTwo ).
select( col( "product_id" ), col( "product_category_id" ), col( "product_name" ), col( "product_description" ), col( "product_price" ), col( "product_image" ) ). createOrReplaceTempView( "products_view" ) )

( spark. read. option( "inferSchema", "true" ). csv( in_dirThree ). 
select( col( "category_id" ), col( "category_department_id" ), col( "category_name" ) ). createOrReplaceTempView( "categories_view" ) )

( spark.sql (
"""
SELECT c.category_name, p.product_name, ROUND( ( o.order_item_subtotal - ( o.order_item_quantity * o.order_item_product_price ) ) , 2) as product_revenue
LIMIT (5) 
FROM categories_view c
JOIN products_view p ON c.category_id == p.product_category_id
JOIN order_items o ON product_id == order_item_product_id
WHERE c.category_name = "Accessories"
ORDER BY product_revenue DESC
"""
).
selectExpr( "concat_ws('|', * ) value" ).
write.
mode( "overwrite" ).
text( out_dir )
)

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""
DFOrdIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dirOne ). toDF( col( "order_item_id" ), col( "order_item_order_id" ), col( "order_item_product_id" ), col( "order_item_quantity" ), col( "order_item_subtotal" ), col( "order_item_product_price" ) ) )
DFOrdIn.printSchema()

DFPrdIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dirTwo ). toDF( col( "product_id" ), col( "product_category_id" ), col( "product_name" ), col( "product_description" ), col( "product_price" ), col( "product_image" ) ) )
DFPrdIn.printSchema()

DFCatIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dirThree ). toDF( col( "category_id" ), col( "category_department_id" ), col( "category_name" ) ) )
DFCatIn.printSchema()


DFIn = ( DFCatIn.join ( DFPrdIn, DFPrdIn.product_category_id == DFCatIn.category_id ).join ( DFOrdIn, DFOrdIn.order_item_product_id == DFPrdIn.order_items ) )
DFIn.printSchema()

Out = ( DFIn.
filter ( col( "category_name" ) == "Accessories" ).
select( col( "category_name" ), col( "product_name" ), ( col( "order_item_subtotal" ) - ( col( "order_item_quantity" ) * col( "order_item_product_price" ) ) ).  format_number( col( "product_revenue" ), 2 ). alias( "product_revenue" ) ).
orderBy( desc( col( "product_revenue" ) ) ).
selectExpr( "concat_ws('|', * ) value" ).
write.
mode( "overwrite" ).
text( out_dir )
)


#------------------

#------------------

from pyspark.sql.functions import *
(spark.read.
csv( in_dirTwo ).
select(
col("_c0").alias( "product_id"),
col("_c1").alias( "category_id"),
col("_c2").alias( "product_name") ).
createOrReplaceTempView( "products" ) )
(spark.read.
csv( in_dirThree ).
select(
col("_c0").alias( "category_id"),
col("_c2").alias( "category_name") ).
filter( "category_name = 'Accessories'" ).
createOrReplaceTempView( "categories" ) )
(spark.read.
csv( in_dirOne ).
select(
col("_c2").alias( "product_id"),
col("_c4").alias( "subtotal") ).
createOrReplaceTempView( "order_items" ) )
(spark.sql(
"""
SELECT
c.category_name,
p.product_name,
ROUND( SUM(subtotal), 2 ) product_revenue
FROM products p
JOIN categories c ON p.category_id = c.category_id
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, c.category_name, p.product_name
ORDER BY product_revenue DESC
LIMIT 5
""").
selectExpr( "concat_ws('|', *) value" ).
write.
mode( "overwrite" ).
text( dir_out ) )

#------------------

#------------------ Comprobación

(spark.read.  text( dir_out ).  orderBy( "value" ).  show( 10, truncate=False ) )

#--------------------------------------EndScenario 19.--------------------------------------

#--------------------------------------StartScenario 20.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers.
Format is csv with no header.
The schema of the customers record is:
customer_customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
All the order records are stored at dataset/retail_db/orders.
Format is csv with no header.
The schema of the orders records is:
order_id int,
order_date string,
order_customer_id int,
order_status string
All the order items records are stored at dataset/retail_db/order_items
Format is csv with no header.
The schema of the order_items records is:
order_item_id int,
order_item_order_id int,
order_item_product_id int,
order_item_quantity tinyint,
order_item_subtotal double,
order_item_product_price double
Output requirements
Get customers who have placed succesuful (COMPLETE) orders of revenue more than 500
Use parquet files for the output files
Use snappy compression
Output should only contain customer_fname, customer_lname, order_revenue
save escribe directamente en formato parquet con compresión snappy.
"""
"""
ls /tmp/dataset/retail_db/customers
ls /tmp/dataset/retail_db/orders
ls /tmp/dataset/retail_db/order_items

hdfs dfs -put 
/tmp/dataset/retail_db/customers dataset/retail_db/customers
/tmp/dataset/retail_db/orders dataset/retail_db/orders
/tmp/dataset/retail_db/order_items dataset/retail_db/order_items

hdfs dfs -ls dataset/retail_db/

hdfs dfs -rm -R dataset/solutions/sce20/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dirOne = "dataset/retail_db/customers"
in_dirTwo = "dataset/retail_db/orders"
in_dirThree = "dataset/retail_db/order_items"

out_dir = "dataset/solutions/sce20/"

DFCusIn = ( spark. read.  option( "inferShema", "true" ).  csv( in_dirOne ).  select( col( "customer_customer_id" ), col( "customer_fname" ), col( "customer_lname" ), col( "customer_email" ), col( "customer_password" ), col( "customer_street" ), col( "customer_city" ), col( "customer_state" ), col( "customer_zipcode" ) ).  createOrReplaceTempView( "customers_view" ) )

DFOrdIn = ( spark. read.  option( "inferShema", "true" ).  csv( in_dirTwo ).  select( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).  createOrReplaceTempView( "orders_view" ) )

DFItemsIn = ( spark. read.  option( "inferShema", "true" ).  csv( in_dirThree ).  select( col( "order_item_id" ), col( "order_item_order_id" ), col( "order_item_product_id" ), col( "order_item_quantity" ), col( "order_item_subtotal" ), col( "order_item_product_price" ) ).  createOrReplaceTempView( "order_items_view" ) )

DFIn = ( 
DFCusIn. join(DFOrdIn, DFOrdIn.order_customer_id == DFCusIn.customer_customer_id ).
DFOrdIn. join(DFItemsIn, DFItemsIn.order_item_order_id == DFOrd.order_id ) )
DFIn.printSchema()

Out = ( DFIn.
filter( col( "order_status" ) == "COMPLETE" & ( col( "order_revenue" ) > 500 ) ).
select( col ("customer_fname" ).  col ("customer_lname" ).  col ("order_revenue" ) ).
write.
mode( "overwrite" ).
option( "inferSchema", "true" ).
save( out_dir )
)

#------------------

#------------------

"""
 toDF(*cols) Returns a new class:DataFrame that with new specified column names
"""

( spark. read.  option( "inferShema", "true" ).  csv( in_dirOne ).  toDF( col( "customer_customer_id" ), col( "customer_fname" ), col( "customer_lname" ), col( "customer_email" ), col( "customer_password" ), col( "customer_street" ), col( "customer_city" ), col( "customer_state" ), col( "customer_zipcode" ) ) )

( spark. read.  option( "inferShema", "true" ).  csv( in_dirTwo ).  toDF( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ) )

( spark. read.  option( "inferShema", "true" ).  csv( in_dirThree ).  toDF( col( "order_item_id" ), col( "order_item_order_id" ), col( "order_item_product_id" ), col( "order_item_quantity" ), col( "order_item_subtotal" ), col( "order_item_product_price" ) ) )

(spark.sql(
"""
SELECT "customer_fname", "customer_lname", "order_revenue"
FROM customers_view c
JOIN orders_view o ON o.order_customer_id == c.customer_customer_id
JOIN order_items_view oi ON oi.order_item_order_id == o.order_id
WHERE "order_status" == "COMPLETE" AND "order_revenue" > 500
"""
).
write.
mode( "overwrite" ).
option( "inferSchema", "true" ).
save( out_dir )
)

#------------------

from pyspark.sql.functions import *
(spark.read.
csv( in_dirTwo ).
filter( col("_c3") == "COMPLETE" ).
select(
col("_c0").alias( "order_id"),
col("_c2").alias( "customer_id") ).
createOrReplaceTempView( "orders_view" ) )
(spark.read.
option( "inferSchema", True ).
csv( in_dirThree ).
select(
col("_c1").alias( "order_id"),
col("_c4").alias( "subtotal") ).
createOrReplaceTempView( "order_items" ) )
(spark.read.
csv( in_dirOne ).
select(
col("_c0").alias( "customer_id"),
col("_c1").alias( "customer_fname"),
col("_c2").alias( "customer_lname" ) ).
createOrReplaceTempView( "customers" ) )
(spark.sql(
"""
SELECT
customer_fname,
customer_lname,
ROUND( SUM(subtotal), 2 ) order_revenue
FROM orders_view
NATURAL JOIN order_items
NATURAL JOIN customers
GROUP BY order_id, customer_id, customer_fname, customer_lname
HAVING SUM(subtotal) > 500
""").
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
save( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  load( out_dir ).  orderBy( "customer_lname", "customer_fname" ).  show( 10 ) )

#--------------------------------------EndScenario 20.--------------------------------------

#--------------------------------------StartScenario 21.--------------------------------------
"""
Data description
All the products records are stored at dataset/retail_db/products_avro
Data is in avro format
Data is compressed with snappy compression
Output requirements
Output should contain columns product_id, product_name, product_price.
Save output as text file
product_id and product_name should be separated by ':'; product_name and product_price should be separated by '+'
"""
"""
ls /tmp/dataset/retail_db/products_avro
hdfs dfs -put /tmp/dataset/retail_db/products_avro dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro

hdfs dfs -rm -R dataset/solutions/sce21/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/products_avro"
out_dir = "dataset/solutions/sce21/"

DFIn = ( spark.  read.  format( "avro" ).  option( "compression", "snappy" ).  load( in_dir ) )
DFIn.printSchema()

Out = ( DFIn.
select( col( "product_id" ), col( "product_name" ), col( "product_price" ) ).
select( concat_ws( ':', "product_id", concat_ws( '+', "product_name", "product_price" ) ) ).
write.
mode( "overwrite" ).
option( "compression", None ).
text( out_dir )
)

#------------------

#------------------

(spark.read.
format( "avro" ).
load( in_dir ).
select( "product_id", "product_name", "product_price" ).
selectExpr(
"""
concat_ws( ':', product_id, concat_ws( '+', product_name, product_price) )
""" ).
write.
mode( "overwrite" ).
option( "compression", "uncompressed" ).
text( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  text( out_dir ).  orderBy ( "value" ).  show( 10, False ) )

#--------------------------------------EndScenario 21.--------------------------------------

#--------------------------------------StartScenario 22.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories
Data is in text format
Data is comma separated
The schema is
category_id int
category_department_id int
category_name string
Output requirements
Convert data into pipe delimited file
Filter the records where category_name is Soccer
Use text format for the output files
Place the result data at dataset/result/scenario22/solution
Compress the output using lz4 compression
"""
"""
ls /tmp/dataset/retail_db/categories
hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/sce22/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/sce22/categories"

DFIn = ( spark.  read.  option( "inferSchema", "true").  csv( in_dir ).  toDF( "category_id", "category_department_id", "category_name") )
DFIn.printSchema()

Out = (DFIn.
filter ( col( "category_name" ) == "Soccer" ).
selectExpr( "concat_ws( '|' , * ) value" ).
write.
mode( "overwrite" ).
option( "compression", "lz4" ).
text ( out_dir )
)

# or

DFIn = ( spark.  read.  option( "inferSchema", "true").  csv( in_dir ) )
DFIn.printSchema()

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

Out = (DFIn.
filter( col("_c2") == "Soccer" ).
select( "_c0", "_c1", "_c2").
withColumn ( "value", concat_ws( '|', "_c0", "_c1", "_c2") ).
drop( "_c0", "_c1", "_c2").
write.
mode( "overwrite" ).
option( "compression", "lz4" ).
text (out_dir)
)

#------------------

#------------------

from pyspark.sql.functions import *
(spark.read.
csv( in_dir ).
filter( col("_c2") == "Soccer" ).
selectExpr( "concat_ws('|', *)" ).
write.
mode( "overwrite" ).
option( "compression", "lz4" ).
text( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  text( out_dir ).  show( 5 ) )

#--------------------------------------EndScenario 22.--------------------------------------

#--------------------------------------StartScenario 23.--------------------------------------
"""
Data description
Customer records are stored at dataset/retail_db/customers-tab-delimited
Data is in text format
Data is tab delimited
Schema is:
customer_id int
customer_fname string
customer_lname string
customer_email string
customer_password string
customer_street string
customer_city string
customer_state string
customer_zipcode string
Output requirements
Output all the customers who live in California
Use text format for the output files
Result should only contain records that have state value as CA
Output should only contain customer's full name; i.e. customer_fname and customer_lname separated by a space.
"""
"""
ls /tmp/dataset/retail_db/customers-tab-delimited
hdfs dfs -put /tmp/dataset/retail_db/customers-tab-delimited dataset/retail_db/customers-tab-delimited

hdfs dfs -ls dataset/retail_db/customers-tab-delimited

hdfs dfs -ls dataset/retail_db/customers-tab-delimited

hdfs dfs -rm -R dataset/solutions/sce22/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dir = "dataset/retail_db/customers-tab-delimited"
out_dir = "dataset/solutions/sce/"

DFIn = ( spark. read. option( "inferSchema", "true" ). option ( "sep", "\t" ). csv ( in_dir ). toDF( ( "customer_customer_id" ), ( "customer_fname" ), ( "customer_lname" ), ( "customer_email" ), ( "customer_password" ), ( "customer_street" ), ( "customer_city" ), ( "customer_state" ), ( "customer_zipcode" ) ) )
DFIn.printSchema()

Out = ( DFIn.
filter( col( "customer_state" ) == 'CA' ).
select( col( "customer_fname" ), col( "customer_lname" ) ).
selectExpr ( "concat_ws( ' ', customer_fname, customer_lname ) value" ).
write. 
mode ( "overwrite" ).
text ( out_dir )
)

#------------------

#------------------

(spark.read.
option("sep", "\t" ).
csv( in_dir ).
filter( col("_c7") == "CA" ).
select( concat_ws( " ", col("_c1"), col("_c2") ) ).
write.
mode( "overwrite" ).
text( out_dir ) )

#------------------

#------------------ Comprobación

(spark.read.  text( out_dir ).  orderBy( "value" ).  show( 10 ) )

#--------------------------------------EndScenario 23.--------------------------------------

#--------------------------------------StartScenario 24.--------------------------------------
"""
Data description
"""
"""
ls /tmp/

hdfs dfs -put /tmp/

hdfs dfs -ls 

hdfs dfs -rm -R dataset/solutions/sce24/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col

in_dir = ""
out_dir = "dataset/solutions/sce24/"


#------------------

#------------------ Comprobación


#--------------------------------------EndScenario 24.--------------------------------------

#--------------------------------------StartScenario 32.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories.
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Output Requirements
Create a metastore table named categories_parquet in the database named q2_db.
CREATE DB "q2_db.categories_parquet"
Table should should contain all 3 columns.
Use parquet format for the output files.
The data for the table should be in dataset/categories_parquet.
"""
"""
ls /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/sce32/

"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/sce32/"
out_table = "q2_db.categories_parquet"

DFIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dir ).
select( col("_c0").alias( "category_id" ), col("_c1").alias( "category_department_id" ), col("_c2").alias( "category_name" ) ) )

DFIn. printSchema()
DFIn. show()


spark.sql( "CREATE database if not exists q2_db" )

Out = (DFIn.
select( "category_id", "category_department_id", "category_name" ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
option( "path", "dataset/result/scenario33/solution" ).
saveAsTable( out_dir )
)
#------------------
#------------------
spark.sql( "CREATE database if not exists q2_db" )
(spark.read.
option( "inferSchema", True).
csv( in_dir ).
toDF( "category_id", "category_department_id", "category_name" ).
write.
mode( "overwrite" ).
option( "path", out_dir ).
saveAsTable( out_table ) )
#------------------

#------------------ Comprobación
(spark.read.  table( out_table ).  orderBy( "category_id" ).  show( 10 ) )
(spark.read.  load( out_dir ).  orderBy( col("category_id").desc() ).  show( 10 ) )

(spark.read.  table( out_dir ).  orderBy( "category_id" ).  show( 10 ) )
#--------------------------------------EndScenario 32.--------------------------------------

#--------------------------------------StartScenario 33.--------------------------------------
"""
Data description
Get data from metastore table named customers.
Table is present in the database default.
Output requirements
Get records from the metastore table named customers such that the four first letters from the first name are equal to the first four letters of the last name.
Use parquet file for the outuput files.
Compress the output using snappy compression.
"""
"""
hdfs dfs -rm -R dataset/solutions/sce33/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
from pyspark.sql.functions import substring

in_dir = "default.customers"
out_dir = "dataset/solutions/sce33/"

DFIn = ( spark.read.table( in_dir ) )
DFIn. printSchema()
DFIn. show()

DFOut = ( DFIn.
select( "customer_id", "customer_fname", "customer_lname" ).
filter( "substr( customer_fname, 1, 4) = substr( customer_lname, 1, 4 )" )
)

DFOut.printSchema()
DFOut.show()

Out = (DFIn.
filter( "substr( customer_fname, 1, 4) = substr( customer_lname, 1, 4 )" ).
select( "customer_id", "customer_fname", "customer_lname" ).
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
parquet( out_dir )
)
#------------------

#------------------
(spark.sql(
"""
SELECT *
FROM customers
WHERE substr( customer_fname, 1, 4) = substr( customer_lname, 1, 4 )
""").
write.
mode( "overwrite" ).
save( out_dir ) )
#------------------

#------------------ Comprobación

(spark.read. load( out_dir ). select( "customer_id", "customer_fname", "customer_lname" ).  orderBy( "customer_id" ).  show( 10, False ) )
(spark. read. parquet ( out_dir ). show( 10 ) )

#--------------------------------------EndScenario 33.--------------------------------------

#--------------------------------------StartScenario 34.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers.
Format is csv with no header.
The schema of the customers record is:
customer_id int, customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode string
All the order records are stored at dataset/retail_db/orders.
Format is csv with no header.
The schema of the orders records is:
order_id int,
order_date string,
order_customer_id int,
order_status string
Output requirements
For each customer output all the dates he made an order
Output should only contain customer_fname, customer_lname, order_date
The order_date should be in the following format: yyyy-mm-dd
There should be only one output file
Use parquet files for the: output files
Use snappy compression
"""
"""
ls /tmp/dataset/retail_db/customers
ls /tmp/dataset/retail_db/orders
hdfs dfs -put /tmp/dataset/retail_db/customers dataset/retail_db/customers
hdfs dfs -put /tmp/dataset/retail_db/orders dataset/retail_db/orders

hdfs dfs -ls dataset/retail_db/

hdfs dfs -rm -R dataset/solutions/sce34/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dirOne = "dataset/retail_db/customers"
in_dirTwo = "dataset/retail_db/orders"
out_dir = "dataset/solutions/sce34/"

DFCusIn = ( spark.  read.  csv( in_dirOne ). select ( "_c0", "_c1", "_c2" ). toDF( "customer_id", "customer_fname", "customer_lname" ) )
DFCusIn.printSchema()
DFIn.show()

DFOrdIn = ( spark.  read.  csv( in_dirTwo). select( "_c1", "_c2" ). toDF( "order_date", "order_customer_id" ) )
DFOrdIn.printSchema()
DFOrdIn.show()

DFIn = DFCusIn. join( DFOrdIn, DFOrdIn.order_customer_id == DFCusIn.customer_id )
DFIn. printSchema()
DFIn. show()


DFOut = ( DFIn.
select( "customer_fname", "customer_lname", "order_date" ).
withColumn( "order_date", to_date( "order_date" ) ).
distinct()
)

DFOut.printSchema()
DFOut.show()

Out = (DFIn.
select( "customer_fname", "customer_lname", "order_date" ).
withColumn( "order_date", to_date( "order_date" ) ).
distinct().
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
parquet( out_dir )
)

#------------------

#------------------
in_dirTwo = "dataset/retail_db/orders/"
in_dirOne = "dataset/retail_db/customers/"
(spark.read.
csv( in_dirTwo ).
select(
col("_c1").alias("order_date"),
col("_c2").alias("customer_id") ).
createOrReplaceTempView( "orders_v" ) )
(spark.read.
csv( in_dirOne ).
select(
col("_c0").alias("customer_id"),
col("_c1").alias("customer_fname"),
col("_c2").alias("customer_lname") ).
createOrReplaceTempView( "customers_v" ) )
(spark.sql(
"""
SELECT DISTINCT
customer_fname,
customer_lname,
to_date( order_date ) order_date
FROM orders_v o
NATURAL JOIN customers_v
""").
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "snappy" ).
save( out_dir ) )
#------------------

#------------------ Comprobación

(spark.read.  load( out_dir ).  orderBy( "order_date", "customer_fname", "customer_lname" ).  show( 10 ) )
spark.sql( "DROP VIEW customers_v" )
spark.sql( "DROP VIEW orders_v" )

# or
(spark. read. parquet ( out_dir ). show( 10 ) )

#--------------------------------------EndScenario 34.--------------------------------------

#--------------------------------------StartScenario 35.--------------------------------------
"""
Data description
Scenario 35
Data description
All the products records are stored at dataset/retail_db/products_avro
Data is in avro fromat1G
Data is compressed with snappy compression
Output requirements
Output should contain columns product_id, product_name, product_price.
Save output as text file
product_id and product_name should be separated by ':'; product_name and product_price by '+'
"""
"""
ls /tmp/dataset/retail_db/products_avro
hdfs dfs -put /tmp/dataset/retail_db/products_avro dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro

hdfs dfs -rm -R dataset/solutions/sce35/

"""
#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
from pyspark.sql.functions import substring

in_dir = "dataset/retail_db/products_avro"
out_dir = "dataset/solutions/sce35/"

DFIn = ( spark. read. format("avro"). option( "compression", "snappy" ). load( in_dir ) )
DFIn.printSchema()
DFIn.show()

DFOut = ( DFIn.
whithColumn( "value", concat_ws( ':', "product_id", "product_name" ) ).
whithColumn( "value", concat_ws( '+', "product_name", "product_price" ) ).
selectExpr( concat_ws( ':', product_id, concat_ws( '+', product_name, product_price ) ) ).
select    ( concat_ws( ':', "product_id", concat_ws( '+', "product_name", "product_price" ) ) ).
select ( "product_id", "product_name", "product_price", "value")
)

DFOut.printSchema()
DFOut.show()

Out = ( DFIn.
write.
mode( "overwrite" ).
option( "compression", "none" ).
csv( out_dir )
)

#------------------
(spark.read.
format( "avro" ).
load( in_dir ).
select( "product_id", "product_name", "product_price" ).
selectExpr(
"""
concat_ws(
':',
product_id,
concat_ws( '+', product_name, product_price) )
""" ).
write.
mode( "overwrite" ).
option( "compression", "uncompressed" ).
text( out_dir ) )
#------------------ Comprobación

(spark.read.  text( out_dir ).  orderBy ( "value" ).  show( 10, False ) )

#--------------------------------------EndScenario 35.--------------------------------------

#--------------------------------------StartQuestion 01.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories.
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Requerimientos de salida
Output only contain category_id, category_name.
Data should be ordered by category_id in descending order.
Use csv format for the output file. Fields separated by ":".
There should be only 1 output file.
"""
"""
ls /tmp/dataset/retail_db/categories
hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/scq01/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/scq01"

DFIn = ( spark. read. option( "inferSchema", "true" ). csv( in_dir ). toDF( "category_id", "category_department_id", "category_name") )
DFIn.printSchema()
DFIn.show()


DFOut = ( DFIn.
coalesce( 1 ).
drop( "category_department_id" ).
select ( "category_id", "category_name" ).
orderBy( "category_id" ). desc()
)

DFOut.printSchema()
DFOut.show()

Out = ( DFOut.
write.
option("sep", ":" ).
mode( "overwrite" ).
csv( out_dir )
)

#------------------

#------------------

( spark. read. option( "inferSchema", "true" ). csv( in_dir ). toDF( "category_id", "category_department_id", "category_name").
drop( "category_department_id" ).
select ( "category_id", "category_name" ).
orderBy( "category_id" ). desc().
coalesce( 1 ).
write.
option("sep", ":" ).
mode( "overwrite" ).
csv( out_dir )
)
#------------------

#------------------ Comprobación

(spark. read.  option( "sep", ":" ).  csv( out_dir ).  show( 10 ) )

#--------------------------------------EndQuestion 01.--------------------------------------

#--------------------------------------StartQuestion 02.--------------------------------------
"""
Data description
All the customer records are stored at dataset/retail_db/customers-avro
Data is in avro format
Requerimientos de salida
Convert all data into tab delimited file
Use text format for the outupt files
Use bzip2 compression
Ouput should only contain customer_id, customer_name
customer_name is first caracter of first name and complete last name separated by space.
"""
"""
ls /tmp/dataset/retail_db/customers-avro
hdfs dfs -put /tmp/dataset/retail_db/customers-avro dataset/retail_db/customers-avro

hdfs dfs -ls dataset/retail_db/customers-avro
hdfs dfs -rm -R dataset/solutions/scq02/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
from pyspark.sql.functions import substring

in_dir = "dataset/retail_db/customers-avro"
out_dir = "dataset/solutions/scq02"

DFIn = ( spark. read. format("avro"). load( in_dir ) )

DFOut = ( DFIn.
#select ( "customer_id", "customer_fname", "customer_lname").
withColumn ( "customer_fname" , substring( ( "customer_fname" ), 1, 1) ).
#select ( "customer_id", "customer_fname", "customer_lname").
withColumn ( "customer_name" , concat_ws( " ", "customer_fname", "customer_lname" ) ).
select ( "customer_id", "customer_name")
)

Out = ( DFIn.
withColumn ( "customer_fname" , substring( ( "customer_fname" ), 1, 1) ).
withColumn ( "customer_name" , concat_ws( " ", "customer_fname", "customer_lname" ) ).
select ( "customer_id", "customer_name").
write.
mode( "overwrite" ).
option( "compression", "bzip2" ).
option( "sep", "\t" ).
csv( out_dir )
)

#------------------

#------------------
( spark. read. format("avro"). load( in_dir ).
withColumn ( "customer_fname" , substring( ( "customer_fname" ), 1, 1) ).
withColumn ( "customer_name" , concat_ws( " ", "customer_fname", "customer_lname" ) ).
select ( "customer_id", "customer_name").
write.
mode( "overwrite" ).
option( "compression", "bzip2" ).
option( "sep", "\t" ).
csv( out_dir )
)
#------------------

#------------------ Comprobación

(spark. read. option ( "sep", "\t" ). csv( out_dir ). show( 10 ) )

#--------------------------------------EndQuestion 02.--------------------------------------

#--------------------------------------StartQuestion 03.--------------------------------------
"""
Data description
Customer records are stored at dataset/retail_db/customers-tab-delimited
Data is in text format
Data is tab delimited
Customers schema:
customer_id, int
customer_fname string
customer_lname string
customer_email string
customer_password string
customer_street string
customer_city string
customer_state string
customer_zipcode string
Requerimientos de salida
Get total number of customers in each state whose first name starts with A
Filter records where total customer count is greater than 50
User parquet format for the output files
Place result data in metastore table customers_replica_parquet
Column names should be state and count.
Use gzip compression
"""
"""
ls /tmp/dataset/retail_db/customers-tab-delimited
hdfs dfs -put /tmp/dataset/retail_db/customers-tab-delimited dataset/retail_db/customers-tab-delimited
hdfs dfs -ls dataset/retail_db/customers-tab-delimited

hdfs dfs -rm -R dataset/solutions/scq03/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
from pyspark.sql.functions import substring

in_dir = "dataset/retail_db/customers-tab-delimited"
out_dir = "dataset/solutions/scq03/"
out_table = "default.customers_replica_parquet"

DFIn = ( spark. read. option( "sep", "\t" ). csv( in_dir ).
select( "_c0", "_c1", "_c2", "_c7").
toDF( "customer_id", "customer_fname", "customer_lname", "customer_state" )
)

Out = ( DFIn.
filter( "substring( ( customer_fname ), 1, 1) = 'A'" ).
groupBy( col( "customer_state" ) ).count(). alias( "count" ).
filter( col( "count" ) > 50 ).
withColumnRenamed("customer_state", "state").
write.
format( "parquet" ).
option( "compression", "gzip" ).
saveAsTable( out_table )
)

#------------------

#------------------
(spark.read.
option( "sep", "\t" ).
csv( in_dir ).
filter( col("_c1").like( "A%" ) ).
select( col("_c7").name( "state" ) ).
createOrReplaceTempView( "states" ) )
(spark.sql(
"""
SELECT state, COUNT(*) count
FROM states
GROUP BY state
HAVING COUNT(*) > 50
""").
write.
mode( "overwrite" ).
format( "parquet" ).
option( "compression", "gzip" ).
saveAsTable( out_table ) )
#------------------

#------------------ Comprobación

(spark.read. table ( out_dir ). show( 10 ) )

#--------------------------------------EndQuestion 03.--------------------------------------

#--------------------------------------StartQuestion 04.--------------------------------------
"""
Data description
All the product records are stored at dataset/retail_db/products_avro
Data is in avro format
Data is compressed with snappy compression
Requerimientos de salida
Output should only contains the products with price lower or equal than 23 and greater or equal than 20.
Filter only product where product_name starts with Nike
Use parquet format for the output files
Compress the output using gzip compression
"""
"""
ls /tmp/dataset/retail_db/products_avro
hdfs dfs -put /tmp/dataset/retail_db/products_avro dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro

hdfs dfs -rm -R dataset/solutions/scq04/
"""

#--------------------------------------pyspark

in_dir = "dataset/retail_db/products_avro"
out_dir = "dataset/solutions/scq04"

DFIn = ( spark. read. format("avro"). option( "compression", "snappy" ). load( in_dir ) )

Out = ( DFIn.
filter( " product_name like 'Nike%' " ).
filter( " product_price <= 23.0 AND product_price >= 20.0 " ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
parquet( out_dir )
)

#------------------

( spark. read. format("avro"). option( "compression", "snappy" ). load( in_dir ). 
filter( " product_name like 'Nike%' " ).
filter( " product_price <= 23.0 AND product_price >= 20.0 " ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
parquet( out_dir )
)

#------------------

#------------------ Comprobación

(spark. read. parquet ( out_dir ). orderBy( "product_price" ).show( 10 ) )

#--------------------------------------EndQuestion 04.--------------------------------------

#--------------------------------------StartQuestion 05.--------------------------------------
"""
Data description
All the order records are stored at dataset/retail_db/orders_parquet
Data is in parquet format
Requerimientos de salida
Output all completed orders
Use json format for the output files
Result should only contain records that have order_status value as COMPLETE
order_date should be in format dd-MM-yyyy
Only records for january 2014 or july 2014 will be in the output
Output should only contain order_id, order_date, order_status.
"""
"""
ls /tmp/dataset/retail_db/orders_parquet
hdfs dfs -put /tmp/dataset/retail_db/orders_parquet dataset/retail_db/orders_parquet

hdfs dfs -ls dataset/retail_db/orders_parquet

hdfs dfs -rm -R dataset/solutions/scq05/
"""

#--------------------------------------pyspark
from pyspark.sql.functions import col
from pyspark.sql.functions import from_unixtime

in_dir = "dataset/retail_db/orders_parquet"
out_dir = "dataset/solutions/scq05"

DFIn = (spark. read. parquet( in_dir ))

Out = ( DFIn.
filter( " order_status = 'COMPLETE' " ).
withColumn( "order_date", from_unixtime( col( "order_date" )/1000, "yyyy-MM-dd" ) ).
filter ( " year(order_date) = '2014' " ).
filter ( " month(order_date) = '07' OR month(order_date) = '01' ").
write.
option( "compression", "none" ).
json( out_dir )
)

#------------------

#------------------
(spark. read. parquet( in_dir ).
filter( " order_status = 'COMPLETE' " ).
withColumn( "order_date", from_unixtime( col( "order_date" )/1000, "yyyy-MM-dd" ) ).
filter ( " year(order_date) = '2014' " ).
filter ( " month(order_date) = '07' OR month(order_date) = '01' ").
write.
option( "compression", "none" ).
json( out_dir )
)
#------------------

#------------------

ordersDF = (spark.read.
load( in_dir ).
ordersDF2 = (ordersDF.
filter( col("order_status") == "COMPLETE" ).
withColumn(
"order_date",
from_unixtime( col("order_date")/1000, "dd-MM-yyyy") ).
filter(
"""
substring( order_date, 4, 2 ) = '01' OR
substring( order_date, 4, 2 ) = '07'
""").
filter( "substring( order_date, 7, 4 ) = '2014'" ).
drop( "order_customer_id" ) )
( ordersDF2.
write.
mode( "overwrite" ).
json( out_dir ) )
#------------------

#------------------ Comprobación

(spark. read. json( out_dir ). orderBy ( "order_date" ). show( 10 ) )

#--------------------------------------EndQuestion 05.--------------------------------------

#--------------------------------------StartQuestion 06.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories
Data is in text format
Data is comma separated
The schema is
category_id int
category_department_id int
category_name string
Requerimientos de salida
Convert data into pipe delimited file
Filter the records where category_name is Soccer
Use text format for the output files
"""
"""
ls /tmp/dataset/retail_db/categories
hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/scq06/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/scq06"

DFIn = ( spark.  read.  option( "inferSchema", "true").  csv( in_dir ) )

Out = (DFIn.
filter( col("_c2") == "Soccer" ).
selectExpr( "concat_ws('|', *) value" ).
write.
mode( "overwrite" ).
text (out_dir)
)

#------------------

( spark.  read.  option( "inferSchema", "true").  csv( in_dir ).
filter( col("_c2") == "Soccer" ).
selectExpr( "concat_ws('|', *) value" ).
write.
mode( "overwrite" ).
text ( out_dir )
)
#------------------

#------------------
(spark.read.
csv( in_dir ).
filter( "_c2 = 'Soccer'" ).
write.
mode( "overwrite" ).
option( "sep", "|" ).
csv( out_dir ) )
#------------------

#------------------ Comprobación

(spark.read.  csv( out_dir ).  show( 5 ) )

#--------------------------------------EndQuestion 06.--------------------------------------

#--------------------------------------StartQuestion 07.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories
Data is in text format
Data is comma separated
The schema is
category_id int
category_department_id int
category_name string
Requerimientos de salida
Convert data into tab delimited file
Use csv format for the output files
There should be a header line; the name of the columns should be category_id, category_department_id, category_name
Compress the output using lz4 compression
"""
"""
ls /tmp/dataset/retail_db/categories
hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/scq07/
"""

#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/scq07/"

DFIn = ( spark.  read.  csv( in_dir ).
select( col( "_c0" ).alias ( "category_id" ), col( "_c1" ).alias ( "category_department_id" ), col( "_c2" ).alias ( "category_name" ) )
)

Out = (DFIn.
write.
mode( "overwrite" ).
option( "sep", "\t" ).
option( "header", "true" ).
option( "compress", "lz4" ).
csv(out_dir)
)
#------------------

#------------------

( spark.  read.  csv( in_dir ).
select( col( "_c0" ).alias ( "category_id" ), col( "_c1" ).alias ( "category_department_id" ), col( "_c2" ).alias ( "category_name" ) ).
write.
mode( "overwrite" ).
option( "sep", "\t" ).
option( "header", "true" ).
option( "compress", "lz4" ).
csv( out_dir )

#------------------

#------------------
(spark.read.
csv( in_dir ).
select( col( "_c0" ).alias ( "category_id" ), 
col( "_c1" ).alias ( "category_department_id" ), 
col( "_c2" ).alias ( "category_name" ) ).
write.
mode( "overwrite" ).
option( "sep", "\t" ).
option( "header", "true" ).
option( "compress", "lz4" ).
csv( out_dir ) )
#------------------

#------------------ Comprobación

(spark.read.
  option( "sep", "\t" ).
  option( "header", True ).
  csv( out_dir ).
  withColumn( "category_id", col("category_id").cast("int" ) ).
  orderBy( col("category_id").desc() ).
  show( 10, False ) )

#--------------------------------------EndQuestion 07.--------------------------------------

#--------------------------------------StartQuestion 08.--------------------------------------
"""
Data description
Get data from metastore table named orders.
Table is present in the database default.
Output requirements
Fetch orders placed on February of any year.
Output order_customer_id, and year-month-day of order_date
the name of the columns should be order_customer_id, and date
Use parquet format for the output files.
Compress the output using gzip compression.
"""
"""
hdfs dfs -rm -R dataset/solutions/scq08/
"""
#--------------------------------------pyspark

in_dir = "default.orders"
out_dir = "dataset/solutions/scq08/"

#------------------
from pyspark.sql.functions import col

(
spark. read. table("default.orders").
filter( "month(order_date ) = 02" ).
withColumn( "order_date", to_date( col( "order_date" ), "yyyy-MM-dd" ) ).
select("order_customer_id", col("order_date").alias( "date" ) ).
write.
mode( "overwrite" ).
option( "compress", "gzip" ).
parquet().
)
#------------------

#------------------ Comprobación

(spark.read.
  load( out_dir ).
  orderBy( "order_customer_id" ).
  show( 10 ) )

#--------------------------------------EndQuestion 08.--------------------------------------

#--------------------------------------StartQuestion 09.--------------------------------------
"""
Data description

All the products records are stored at dataset/retail_db/products_avro
Data is in avro format
Data is compressed with snappy compression
Output requirements
Output should contain columns product_name, product_price.
Save output as json file
The output should not contain duplicate rows
There should be only 1 file in the output
Use no compression
"""
"""
ls /tmp/dataset/retail_db/products_avro

hdfs dfs -put /tmp/dataset/retail_db/products_avro dataset/retail_db/products_avro

hdfs dfs -ls dataset/retail_db/products_avro

hdfs dfs -rm -R dataset/solutions/scq09/
"""
#--------------------------------------pyspark

in_dir = "dataset/retail_db/products_avro"
out_dir = "dataset/solutions/scq09/"

from pyspark.sql.functions import *

( spark. read. format("avro"). option( "compression", "snappy" ). load( in_dir ).
select ( "product_name", "product_price" ).
distinct().
coalesce( 1 ).
write.
mode( "overwrite" ).
option( "compression", "uncompressed" ).
json( out_dir ) )
#------------------

#------------------ Comprobación

(spark.read.  json( out_dir ).  orderBy( col("product_name").desc() ).  show( 10, truncate=False ) )

#--------------------------------------EndQuestion 09.--------------------------------------

#--------------------------------------StartQuestion 10.--------------------------------------
"""
Data description
All the categories records are stored at dataset/retail_db/categories
Data is in text format
Data is comma separated
Schema is:
category_id int,
category_department_id int,
category_name string
Output requirements
Create a metastore table named default.retail_categories.
The format of the data must be parquet.
The table should contain two columns: category_id, category_name
Save all categories in metastore table default.retail_categories.
"""
"""
ls /tmp/dataset/retail_db/categories

hdfs dfs -put /tmp/dataset/retail_db/categories dataset/retail_db/categories

hdfs dfs -ls dataset/retail_db/categories

hdfs dfs -rm -R dataset/solutions/scq10/
"""
#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/categories"
out_dir = "dataset/solutions/scq10/"
out_table = "default.retail_categories"

DFIn = ( spark. read. csv( in_dir ). toDF( "category_id", "category_department_id", "category_name") )

DFOut = ( DFIn.
withColumn ( ("category_id"), col ( "category_id" ). cast( "int" ) ).
withColumn ( ("category_name"), col ( "category_name" ) ).
select("category_id", "category_name")
)

Out = ( DFIn.
withColumn ( ("category_id"), col ( "category_id" ). cast( "int" ) ).
withColumn ( ("category_name"), col ( "category_name" ) ).
select("category_id", "category_name").
write.
mode( "overwrite" ).
option( "path", "dataset/solutions/scq10/" ).
saveAsTable( out_table )
)

#------------------

#------------------

( spark. read. csv( in_dir ). toDF( "category_id", "category_department_id", "category_name").
withColumn ( ("category_id"), col ( "category_id" ). cast( "int" ) ).
withColumn ( ("category_name"), col ( "category_name" ) ).
select("category_id", "category_name").
write.
mode( "overwrite" ).
option( "path", "exam/question4" ).
saveAsTable( "default.retail_categories" )
)

#------------------

#------------------ Comprobación

(spark.read.  table( out_table ).  orderBy( "category_name" ).  show( 10 ) )

#--------------------------------------EndQuestion 10.--------------------------------------

#--------------------------------------StartQuestion 11.--------------------------------------
"""
Data description
All the order records are stored in HDFS directory dataset/retail_db/orders_parquet
Data is in parquet format
Output requirements
Output should contain 1 column with the different order_status without repeticion.
The name of the columns should be order_status
Compress the output using snappy compression
The format of the output should be orc
"""
"""
ls /tmp/dataset/retail_db/orders_parquet

hdfs dfs -put /tmp/dataset/retail_db/orders_parquet dataset/retail_db/orders_parquet

hdfs dfs -ls dataset/retail_db/orders_parquet

hdfs dfs -rm -R dataset/solutions/scq11/
"""
#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/orders_parquet"
out_dir = "dataset/solutions/scq11/"

DFIn = (spark. read. parquet( in_dir ))
DFOut = ( DFIn.
select ( "order_status" ).
distinct()
)

Out = ( DFIn.
select ( "order_status" ).
distinct().
write.
option( "compression", "snappy" ).
orc( out_dir )
)

#------------------

#------------------

from pyspark.sql.functions import *

(spark. read. parquet( in_dir ).
select ( "order_status" ).
distinct().
write.
option( "compression", "snappy" ).
orc( out_dir )
)
#------------------

#------------------ Comprobación

(spark.read.
  orc( out_dir ).
  orderBy( "order_status" ).
  show( 10 ) )

#--------------------------------------EndQuestion 11.--------------------------------------

#--------------------------------------StartQuestion 12.--------------------------------------
"""
Data description
All the order records are stored at dataset/retail_db/orders_parquet
Data is in parquet format
Output requirements
Output all the order status along with their count
Use CSV format for the output files
Compress the output using gzip compression
Output should only contain order_status, total_count
Output should be in descending order by total_count
Output should only contain one partition file
"""
"""
ls /tmp/dataset/retail_db/orders_parquet

hdfs dfs -put /tmp/dataset/retail_db/orders_parquet dataset/retail_db/orders_parquet

hdfs dfs -ls dataset/retail_db/orders_parquet

hdfs dfs -rm -R dataset/solutions/scq12/
"""
#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "dataset/retail_db/orders_parquet"
out_dir = "dataset/solutions/scq12/"

from pyspark.sql.functions import *

(spark.read.
  load( in_dir ).
  select( "order_status" ).
  createOrReplaceTempView( "orders_view" ) )

(spark.sql(
  """
  SELECT order_status, COUNT(order_status) total
  FROM orders_view
  GROUP BY order_status
  ORDER BY total DESC
  """).
  coalesce( 1 ).
  write.
  mode( "overwrite" ).
  option( "compression", "gzip" ).
  csv( out_dir )
)

#------------------


#------------------ Comprobación

(spark.read.  csv( "out_dir" ).  show() )

#--------------------------------------EndQuestion 12.--------------------------------------

#--------------------------------------StartQuestion 13.--------------------------------------
"""
Data description
Get data from metastore table named orders
Table is present in the default database
Output requirementes
Fetch orders greater than or equal to Dec-2013
Use parquet format for the output files
Compress the output using gzip compression
"""
"""
hdfs dfs -rm -R dataset/solutions/scq13/
"""
#--------------------------------------pyspark

from pyspark.sql.functions import *

in_dir = "orders"
out_dir = "dataset/solutions/scq13/"

DFIn = ( spark.read.table( in_dir ) )
DFIn.printSchema()

Out = ( DFIn.
filter( "year(order_date ) >= 2013" ).
select ( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
parquet( out_dir )
)

#------------------

#------------------

( spark.read.table( in_dir ).
filter( "year(order_date ) >= 2013" ).
select ( col( "order_id" ), col( "order_date" ), col( "order_customer_id" ), col( "order_status" ) ).
write.
mode( "overwrite" ).
option( "compression", "gzip" ).
parquet( out_dir )
)

#------------------

#------------------ Comprobación

(spark.read.  parquet( out_dir ).  orderBy( "order_customer_id", "order_id" ).  show( 10 ) )

#--------------------------------------EndQuestion 13.--------------------------------------

#--------------------------------------StartScenario .--------------------------------------
"""
Data description
"""
"""
ls /tmp/

hdfs dfs -put /tmp/

hdfs dfs -ls 

hdfs dfs -rm -R dataset/solutions/sce/

"""

#--------------------------------------pyspark


#------------------

#------------------ Comprobación


#--------------------------------------EndScenario .--------------------------------------