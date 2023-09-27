from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Save DataFrame as CSV") \
    .getOrCreate()

# Create a sample DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Specify the path where you want to save the CSV file
output_path = "path_to_save/my_dataframe.csv"

# Save the DataFrame as a CSV file
df.write \
    .format("csv") \
    .option("header", "true") \  # Include header row
    .mode("overwrite") \  # You can use "overwrite", "append", or "ignore"
    .save(output_path)

# Stop the Spark session
spark.stop()
