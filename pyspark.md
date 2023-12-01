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
