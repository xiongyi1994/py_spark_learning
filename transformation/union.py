# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([3, 4, 5])

rdd = rdd1.union(rdd2)

print rdd.collect()

# union 输出结果包含重复的数据
