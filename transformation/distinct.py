# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize([1, 1, 1, 1, ])

rdd = rdd.distinct()

print rdd.collect()

# distinct()操作的开销很大，因为它需要将所有数据通过网络进行混洗(shuffle)，以确保每个元素都只有一份
