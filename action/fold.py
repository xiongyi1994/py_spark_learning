from pyspark import SparkContext

sc = SparkContext()

a = [1, 2, 3, 4, 5]

rdd = sc.parallelize(a)

print rdd.fold(1, lambda x, y: x + y)

'''
    why the result is 24 ??????
'''
