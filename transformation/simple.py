# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize([1, 2, 3])

rdd = rdd.sample()

# 对 RDD 采样，以及是否替换，结果是非确定的
