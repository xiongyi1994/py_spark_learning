# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([3, 4, 5])

rdd = rdd1.subtract(rdd2)

print rdd.collect()

# subtract() 和 intersection() 一样，它也需要数据混洗。
