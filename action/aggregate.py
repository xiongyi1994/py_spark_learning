# coding=<coding=utf-8>
from pyspark import SparkContext

# 利用aggregate计算平均值

sc = SparkContext()

nums = [1, 2, 3, 4]

numsRDD = sc.parallelize(nums)

sumCount = numsRDD.aggregate((0, 0),
                             (lambda acc, value: (acc[0] + value, acc[1] + 1)),
                             (lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])))
print sumCount
print sumCount[0] / float(sumCount[1])
