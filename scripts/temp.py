from databricks.connect import DatabricksSession

# spark = DatabricksSession.builder.remote(cluster_id = '0413-015834-ammsxcbc').getOrCreate()
spark = DatabricksSession.builder.serverless().getOrCreate()
spark.sql("SELECT 1").show()
