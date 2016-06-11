from pyspark import SparkContext

logFile = "~/projects/spark/histogram/README.md"  # Should be some file on your system
sc = SparkContext("local", "Histogram")
logData = sc.textFile(logFile).cache()

nums = sc.parallelize(range(0,10))
oversample = nums.sample(True, 1000)
#oversample.count()
f = open('histogram.txt', 'w')
f.write(str(oversample.histogram(range(0,11))))
f.close()
