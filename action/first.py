from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize([0, 1, 2, 3])

print rdd.first()
