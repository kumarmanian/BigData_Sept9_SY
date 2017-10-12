# Week 4 Instructions

# Spark Ingestion
* Download the following file on to your laptop
     https://catalog.data.gov/dataset/budget-2017-budget-recommendations-positions-and-salaries

* Write a pyspark script named 'spark_analysis.py' and write pyspark to load this data from local file system into a Data frame
* Write this data frame into a HDFS file under /user/ubuntu/sparkingest/raw/

# Spark Trasform and load
* Modify the 'spark_analysis.py' file to load the HDFS file from /user/ubuntu/sparkingest/ into a data frame
* Remove the header from the csv file using spark
* Write a transform to remove the dollar signs from the last two columns
* Save the resulting data frame as in ORC format into /user/ubuntu/sparkingest/stage/
* Upload spark_analysis.py to your /Week4/ folder.

# Spark Streaming

* Write a pyspark script 'spark_stream.py' to initialize a spark streaming context to listen on 9999 on the localhost of edge node
* Load the staging data from /user/ubuntu/sparkingest/stage/  into a data frame
* Cache the data frame
* Using a NetCat command on another putty window connect to the spark streaming context.
* In the pyspark script 'spark_stream.py' write code to take in a department code from the DStream (What user types in from netcat) and filter the cached data frame with that department code
* print the resulting data frame.
* Start the spark_stream.py and output the console to 'myspark_stream_result.log' and upload to your github /Week4/ folder
* Upload spark_stream.py code to /Week4/
