from databricks.connect import DatabricksSession
#spark = DatabricksSession.builder.remote(cluster_id = '0409-234714-u6c4zbfc').getOrCreate()
spark =DatabricksSession.builder.getOrCreate()
spark.sql("SELECT 1").show()