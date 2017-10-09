CREATE EXTERNAL TABLE stage_complaints ( product STRING,
sub_product STRING,
issue STRING,
sub_issue STRING,
company STRING,
state STRING,
zip_code STRING,
submitted_via STRING,
date_sent_to_company DATE,
timely_response STRING,
consumer_disputed STRING,
complaint_id STRING) 
PARTITIONED BY (year INT,month INT, day INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS ORC
LOCATION '/data/stage/consumer_data_stage'; 