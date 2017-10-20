from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark.sql.functions import *

conf= (SparkConf())
# Create new context
sc= SparkContext(conf=conf)

sqlContext = SQLContext(sc)

#df = sqlContext.read.csv("file:/home/ubuntu/practice/chicago_2017_budget_salaries.csv",header=False)
#df.write.format("csv").save('/user/ubuntu/sparkingest/raw')
df1 = sqlContext.read.csv("/user/ubuntu/sparkingest/raw/",header=False)
df1.show(2)
dfFilter = df1.filter("_c0 != 'FUND TYPE'")
dfFilter.show(1)
dfTransform1 = dfFilter.withColumn('_c20',regexp_replace('_c20','[$]',''))
dfTransform2 = dfTransform1.withColumn('_c21',regexp_replace('_c21','[$]',''))
dfTransform2.show(1)
dfTransform2.write.format("ORC").save('/user/ubuntu/sparkingest/stage')
