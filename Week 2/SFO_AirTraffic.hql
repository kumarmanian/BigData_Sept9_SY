CREATE EXTERNAL TABLE IF NOT EXISTS airtraffic
(
        period STRING,
        opairline STRING,
        opairlinecode STRING,
        pubairline STRING,
        pubairlinecode STRING,
        geosummary STRING,
        georegion STRING,
        activitytypecode STRING,
        pricecategorycode STRING,
        terminal STRING,
        boardingarea STRING,
        passengercnt INT
        
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/ubuntu/airtraffic';
