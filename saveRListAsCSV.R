# Load the data.table package
library(data.table)

# Create a sample named list of data tables
dt_list <- list(
  dt1 = data.table(x = c(1, 2, 3), y = c("a", "b", "c")),
  dt2 = data.table(x = c(4, 5, 6), y = c("d", "e", "f")),
  dt3 = data.table(x = c(7, 8, 9), y = c("g", "h", "i"))
)

# Define the file path where the CSV files will be saved
file_path <- "/path/to/directory/"

# Loop through the list and save each named data.table as a CSV file
for (name in names(dt_list)) {
  dt <- dt_list[[name]]
  file_name <- paste0(name, ".csv")
  fwrite(dt, file.path(file_path, file_name))
}
