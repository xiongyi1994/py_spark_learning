# coding=<coding=utf-8>
from pyspark import SparkContext

sc = SparkContext()

rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([3, 4, 5])

rdd = rdd1.intersection(rdd2)

print rdd.collect()

# intersection() 在运行时也会去掉所有重复的元素(单个 RDD 内的重复元素也会一起移除)。
# 尽管 intersection() 与 union() 的概念相似，intersection() 的性能却要差很多，因为它需要 通过网络混洗数据来发现共有的元素。
