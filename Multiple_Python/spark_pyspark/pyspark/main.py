# %%
from pyspark import SparkConf, SparkContext 

# %%
# connect to remote server
# sc = SparkContext.getOrCreate() 

master = '1636bb3ff163'
conf = SparkConf().setAppName("mytest").setMaster(f'spark://{master}:7077')
sc = SparkContext(conf=conf)

# %%
# check that it really works by running a job
# example from http://spark.apache.org/docs/latest/rdd-programming-guide.html#parallelized-collections
data = range(10000) 
distData = sc.parallelize(data)
distData.filter(lambda x: not x&1).take(10)
# Out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# %%
