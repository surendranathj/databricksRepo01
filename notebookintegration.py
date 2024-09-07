# Databricks notebook source
df_01=spark.read.csv('/Volumes/workdatanbricks78/default/vol8/cars_seaborn_dataset.csv')

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC show catalogs
