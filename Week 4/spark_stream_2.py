from pyspark.streaming import StreamingContext
from pyspark import SparkConf,SparkContext
from pyspark import SQLContext
from pyspark.sql.functions import *
from pyspark.sql import SparkSession

conf=(SparkConf())
sc=SparkContext(conf=conf)
ssc=StreamingContext(sc,1)

sqlContext = SQLContext(sc)

spark = SparkSession.builder.appName("StructuredNetworkFilter").getOrCreate()

df = sqlContext.read.orc("/user/ubuntu/sparkingest/stage/")
df.cache()

#lines=ssc.socketTextStream("localhost",9999)
#words=lines.flatMap(lambda line:line.split(" "))
#words.pprint()
#ip=words.map(lambda word:(word,1))
#p0i#rint(ip)
#dfFilter=df[df._c1==lines]
#dfFilter.show(1)
socketDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

deptcodeDF = socketDF.select(
   explode(
       split(socketDF.value, " ")
   ).alias("dept_id")
)

dfFilter=df.join(deptcodeDF,df._c1==deptcodeDF.dept_id).select ('_c0','_c1','_c2','_c3','_c4','_c5','_c6','_c7','_c8','_c9','_c10','_c11','_c12','_c13','_c14','_c15','_c16','_c17','_c18','_c19','_c20','_c21')

query = dfFilter\
    .writeStream \
    .outputMode("append")\
    .format("console")\
    .start()


#ssc.start()
ssc.awaitTermination()

