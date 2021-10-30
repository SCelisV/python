from pprint import pprint as pp

def printRDD( rdd, message = "RDD" ):
  print( message )
  pp( rdd.collect() )
  print()

orderfile = "orderskus.txt"

ordersRDD = ( sc.textFile( orderfile ).
  map(lambda s: s.split(' ')).
  map(lambda fields: (fields[0],fields[1])).
  flatMapValues(lambda skus:skus.split(':')) )
printRDD( ordersRDD, "ordersRDD" )


idSkuRDD = (ordersRDD.
  groupByKey().
  mapValues( lambda s: ":".join(s) ).
  sortByKey().
  map( lambda t: t[0] + " " + t[1] ) )
printRDD( idSkuRDD, "idSkuRDD" )


skuIdRDD = ( ordersRDD.
  map( lambda t: (t[1], t[0]) ).
  groupByKey().
  mapValues( lambda r: ":".join(r) ).
  sortByKey().
  map( lambda t: t[0] + " " + t[1] ) )
printRDD( skuIdRDD, "skuIdRDD" )
