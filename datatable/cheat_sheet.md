Here's a concise cheatsheet for using `data.table` in R. `data.table` is a high-performance package for data manipulation, offering fast aggregation, joins, and more. 

### Basics
```R
library(data.table)

# Creating a data.table
DT <- data.table(x = 1:5, y = letters[1:5])

# Viewing the first rows
head(DT, n)  # Show first n rows
```

### Syntax Overview
```R
DT[i, j, by]  # Primary syntax for data manipulation
```
- `i`: Subsetting rows (similar to `subset`)
- `j`: Selecting or computing on columns
- `by`: Grouping by columns

### Subsetting Rows (`i`)
```R
# Select rows where x > 3
DT[x > 3]

# Select the first two rows
DT[1:2]

# Conditional subsetting
DT[y == "a" | y == "b"]
```

### Selecting and Modifying Columns (`j`)
```R
# Select columns 'x' and 'y'
DT[, .(x, y)]

# Create a new column 'z'
DT[, z := x * 2]

# Multiple operations at once (without creating a new data.table)
DT[, `:=`(z = x * 2, w = y)]

# Remove a column
DT[, z := NULL]
```

### Grouping (`by`)
```R
# Calculate mean of 'x' by 'y'
DT[, .(mean_x = mean(x)), by = y]

# Multiple groupings
DT[, .(sum_x = sum(x)), by = .(y1, y2)]

# Order by group
DT[order(y), .(sum_x = sum(x)), by = y]
```

### Aggregation
```R
# Count occurrences of each group
DT[, .N, by = y]  # .N is a special symbol for the count of rows

# Aggregate multiple functions
DT[, .(mean_x = mean(x), sum_x = sum(x)), by = y]
```

### Chaining
```R
# Perform multiple operations in a sequence
DT[, .(mean_x = mean(x)), by = y][order(-mean_x)]

# Add a column and immediately group
DT[, z := x * 2][, .(sum_z = sum(z)), by = y]
```

### Joins
```R
# Create two data.tables
DT1 <- data.table(id = 1:3, x = c(10, 20, 30))
DT2 <- data.table(id = c(2, 3, 4), y = c("a", "b", "c"))

# Inner join (merge on common columns)
DT1[DT2, on = "id"]

# Left join (keeps all rows in DT1)
DT1[DT2, on = "id", nomatch = 0]

# Right join (keeps all rows in DT2)
DT2[DT1, on = "id"]

# Update join
DT1[DT2, x := i.x, on = "id"]  # i. refers to columns from DT2
```

### Keys and Fast Subsetting
```R
# Set key on a column (for fast joins and ordering)
setkey(DT, y)

# Fast subsetting based on key
DT["a"]
```

### Reshaping Data
```R
# Wide to long (melt)
melt(DT, id.vars = "id", measure.vars = c("x", "y"))

# Long to wide (dcast)
dcast(DT, id ~ variable, value.var = "value")
```

### Other Useful Functions
```R
# Unique rows
unique(DT)

# Summary of data.table
summary(DT)

# Copy a data.table (to avoid modifying by reference)
DT_copy <- copy(DT)

# Set column order
setcolorder(DT, c("y", "x"))

# Sample rows
DT[sample(.N, 3)]  # Randomly sample 3 rows
```

### Count NAs in data.table
To check for the number of `NULL` or `NA` values in a `data.table`, you can use the following methods:

### Checking for `NA` values in a single column
```R
# Count NA values in column 'x'
DT[, sum(is.na(x))]
```

### Checking for `NA` values in all columns
```R
# Count NA values for each column
DT[, lapply(.SD, function(col) sum(is.na(col)))]
```
- `.SD`: Stands for “Subset of Data,” which refers to all columns within the scope of the current operation.
- `lapply()`: Applies the function to each column in `.SD`.

### Checking for `NA` values in specific columns
```R
# Count NA values in columns 'x' and 'y'
DT[, lapply(.SD, function(col) sum(is.na(col))), .SDcols = c("x", "y")]
```

### Counting total `NA` values across the entire data.table
```R
# Total NA count in the entire data.table
DT[, sum(is.na(.SD))]
```
This computes the total number of missing values across all columns of the `data.table`.

### Example: Display NA counts for all columns
```R
# Display NA counts with column names
DT[, sapply(.SD, function(col) sum(is.na(col)))]
```

This will give a named vector showing the number of `NA`s for each column in the `data.table`.

### Fast File Reading/Writing
```R
# Fast reading/writing using fread() and fwrite()
DT <- fread("file.csv")      # Read CSV
fwrite(DT, "file.csv")       # Write CSV
```

This cheatsheet covers common operations in `data.table`. It’s a highly efficient package, especially useful for large datasets in R.
