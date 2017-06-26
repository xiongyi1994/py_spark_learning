from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize(['a is b is c','a is b are cs'])

print rdd.flatMap(lambda x:x.split(" ")).collect()