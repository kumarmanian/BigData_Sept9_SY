# Week 5 Instructions

# Create kiosk device hive table
* Based on the csv data sent in your email create DDL for hive external table table. Name it kiosk_device.hql and upload it to your week5 folder
# Ingest kiosk device data
* Use hdfs dfs -put to ingest this data into /user/ubunut/kiosk_device/
# Create kiosk unit hive table
* Based on the csv data sent in your email create DDL for hive table. Name it kiosk_unit.hql and upload it to your week5 folder
# Ingest kisosk unit data
* Use hdfs dfs -put to ingest this data into /user/ubunut/kiosk_unit/
# Create HBase table
* Create a HBase table "kiosk_details" with one column family "cf1"
# Create a hive table that can query data from HBase
* Use the DDL attached in the email to create Hive table.
# Ingest data into HBase by joining the two hive tables.
* Use the DML attached in email
