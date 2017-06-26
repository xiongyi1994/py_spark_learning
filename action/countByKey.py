# coding=<coding=utf-8>

# 对每个键对应的元素分别计数 countByKey

from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize([1,2,3,4,5,6,6,6,6])

pairRDD = rdd.map(lambda x:(x,'xiongyi'+str(x)))

print pairRDD.countByKey()





