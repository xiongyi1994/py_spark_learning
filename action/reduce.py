from pyspark import SparkContext

sc = SparkContext()

a = [1, 2, 3, 4, 5]

rdd = sc.parallelize(a)

print rdd.reduce(lambda x, y: x + y)
