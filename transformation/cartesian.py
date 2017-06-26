# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([3, 4, 5])

rdd = rdd1.cartesian(rdd2)

print rdd.collect()

# 求大规模 RDD 的笛卡儿积开销巨大。
