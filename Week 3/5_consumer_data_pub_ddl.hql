CREATE EXTERNAL TABLE top_complaint_states ( state STRING,
cnt INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS PARQUET
LOCATION '/data/stage/consumer_data_pub'; 