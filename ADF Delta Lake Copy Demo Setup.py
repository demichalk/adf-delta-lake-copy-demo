# Databricks notebook source
# MAGIC %md 
# MAGIC #### Put in a Blob Storage name 
# MAGIC the cluster has spark.conf configuration with a key
# MAGIC The Blob storage account needs an adfdemo container created in it

# COMMAND ----------

blob_name = "fieldengdeveastus2sa"

# COMMAND ----------

# MAGIC %md
# MAGIC #### Clean up the folders 
# MAGIC  clear out Blob storage adfdemo container

# COMMAND ----------

dbutils.fs.rm(f"wasbs://adfdemo@{blob_name}.blob.core.windows.net/input", True)
dbutils.fs.rm(f"wasbs://adfdemo@{blob_name}.blob.core.windows.net/output", True)
dbutils.fs.rm(f"wasbs://adfdemo@{blob_name}.blob.core.windows.net/table", True)


# COMMAND ----------

# MAGIC %md
# MAGIC #### load taxi data into Blob storage 

# COMMAND ----------

dbutils.fs.cp(
  "dbfs:/databricks-datasets/nyctaxi/tripdata/yellow/yellow_tripdata_2019-12.csv.gz",  
  f"wasbs://adfdemo@{blob_name}.blob.core.windows.net/input/taxi.csv.gz"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### create Delta Lake database and table in Blob storage

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP DATABASE IF EXISTS adf_taxi_demo CASCADE

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE adf_taxi_demo

# COMMAND ----------

create_table_sql = f"""
CREATE TABLE adf_taxi_demo.tripdata 
(
  VendorID integer,
  tpep_pickup_datetime string,
  tpep_dropoff_datetime string,
  store_and_fwd_flag string,
  RatecodeID integer,
  PULocationID integer,
  DOLocationID integer,
  passenger_count integer,
  trip_distance double,
  fare_amount double,
  extra double,
  mta_tax double,
  tip_amount double,
  tolls_amount double,
  improvement_surcharge double,
  total_amount double,
  payment_type integer,
  congestion_surcharge double
)
USING delta
LOCATION 'wasbs://adfdemo@{blob_name}.blob.core.windows.net/table/tripdata'
TBLPROPERTIES (delta.autoOptimize.optimizeWrite = true, delta.autoOptimize.autoCompact = false)
"""
spark.sql(create_table_sql)
