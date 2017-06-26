# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize([1, 2, 3])

rdd = rdd.filter(lambda x: x != 2)

print rdd.collect()
