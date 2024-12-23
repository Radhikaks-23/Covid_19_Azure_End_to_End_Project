# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "c9fd8d25-5908-45fb-872a-01b097e49baf",
           "fs.azure.account.oauth2.client.secret": "De18Q~40Iv0Hn1DlAu4s-r588hGEzJ7KT1kK3b3E",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/87f050b0-4ec1-410d-81d7-97b2c1e92b04/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@coviddatalakegen.dfs.core.windows.net/",
  mount_point = "/mnt/coviddatalakegen/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@coviddatalakegen.dfs.core.windows.net/",
  mount_point = "/mnt/coviddatalakegen/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@coviddatalakegen.dfs.core.windows.net/",
  mount_point = "/mnt/coviddatalakegen/lookup",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/coviddatalakegen")