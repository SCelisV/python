# Python application 
"""
to execute:
scelisdev03@cluster-cca175-m:~$ vi app-accounts-by-state.py

si lo ejecutas sin argumentos te dará un error:
scelisdev03@cluster-cca175-m:~$ spark-submit app-accounts-by-state.py
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'> Usage: accounts-by-state.py <state-code>

scelisdev03@cluster-cca175-m:~$ spark-submit app-accounts-by-state.py CA
"""
"""
definition
The Spark application will take a single argument—a state code (such as CA). 
The program should read the data from the devsh.accounts Hive table and save the rows whose state column value matches the specified state code. 
Write the results to /devsh_loudacre/accounts_by_state/state-code (such as accounts_by_state/CA).
"""
import sys

from pyspark.sql import SparkSession

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print(sys.stderr, "Usage: accounts-by-state.py <state-code>")
    sys.exit()
    
  stateCode = sys.argv[1]

  # Create a SparkSession object
  spark = SparkSession.builder.getOrCreate()

  # Change the application log level from INFO (the default) to WARN

  spark.sparkContext.setLogLevel("WARN")

  # Leer la tabla Hive
  accountsDF = spark.read.table("devsh.accounts")

  # seleccionar los registros que coincidan con el argumento pasado
  # save el resultado
  accountsDF.where(accountsDF.state==stateCode).write.mode("overwrite").save("/devsh_loudacre/accounts_by_state" + stateCode)
  # Otra forma
  """
  stateAccountsDF = accountsDF.where(accountsDF.state == stateCode)
  stateAccountsDF.write.mode("overwrite").save("/devsh_loudacre/accounts_by_state/" + stateCode)
  """

  #stop the Spark session:
  spark.stop()

"""
Revisar los ficheros en:
"""
#hdfs dfs -ls /devsh_loudacre/
#hdfs dfs -ls /devsh_loudacre/accounts_by_state + stateCode
#hdfs dfs -ls /devsh_loudacre/accounts_by_stateCA/