from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize(["hello my name is xiongyi", "I'am learning spark"])

pairRDD = rdd.map(lambda x: (x.split(' ')[0], x))

print pairRDD.collect()
