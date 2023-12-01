# Get unique values from the "ID" column after dropping null values

```python
unique_quarters = df2.select("ID").filter(col("ID").isNotNull()).distinct().rdd.flatMap(lambda x: x).collect()
```

# Create New Column in PySpark

```python
from pyspark.sql.functions import lit
df = df.withColumn('new_col', lit(0))
```


# Find minimum of a column:

```python
# Find the minimum value of the "Age" column
min_age = df.agg(F.min("Age")).first()[0]
```
# ISIN Operation
```python
filtered_df3 = df3.filter(col("col3").isin(df2.select("col3").rdd.flatMap(lambda x: x).collect())) \
                 .select("col3", "col8", "col9", "col1", "col2")
```

# Join with Duplicate columns
```python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample DataFrames with a common column "id"
data1 = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
data2 = [(2, 100), (3, 200), (4, 300)]

columns = ["id", "name"]

df1 = spark.createDataFrame(data1, columns)
df2 = spark.createDataFrame(data2, columns)

# Inner join on the common column "id"
result_df = df1.select("id", "name").alias('left').join(df2.select("id", "name").alias('right'), ["id"], how="inner")

# Show the resulting DataFrame
result_df.show()
```

# To Date
```python
from pyspark.sql.functions import to_date
df = df.withColumn('start_date', to_date(df['start_date'], 'yyyy-MM-dd'))
```

# Sort by multiple columns
```python
df = df.sort(F.col('col1'), F.col('col2'), F.col('col3'))
```


