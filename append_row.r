library(data.table)

append_row_with_default <- function(dt, new_row_data, n) {
    
  # Check if 'dt' is a data.table
  if (!is.data.table(dt)) {
    stop("The 'dt' parameter should be a data.table.")
  }
  
  # Check if 'new_row_data' is a named list
  if (!is.list(new_row_data) || is.null(names(new_row_data))) {
    stop("The 'new_row_data' parameter should be a named list with column names as keys.")
  }
  
  # Check if 'n' is within the bounds of the number of columns
  if (n < 1 || n > ncol(dt)) {
    stop("The 'n' parameter is out of bounds of the number of columns in the data.table.")
  }
  
  # Create an empty list to store the new row
  new_row <- vector("list", ncol(dt))
  names(new_row) <- names(dt)
  
  # Fill the new row with values from new_row_data or default from n-th column
  for (col in names(dt)) {
    if (col %in% names(new_row_data)) {
      new_row[[col]] <- new_row_data[[col]]
      cat(sprintf("Column '%s' found in new_row_data, using value: %s\n", col, new_row_data[[col]]))
    } else {
      new_row[[col]] <- dt[[col]][n]
      cat(sprintf("Column '%s' not found in new_row_data, using default value from column %d: %s\n", col, n, dt[[col]][n]))
    }
  }
  
  # Append the new row to the data.table
  dt <- rbind(dt, new_row, use.names = TRUE, fill = TRUE)
  cat("New row appended successfully.\n")
  
  return(dt)
}

# Example usage
dt <- data.table(a = 1:5, b = 6:10, c = 11:15)
new_row_data <- list(a = 99, c = 77)
n <- 3

# Append the row
dt <- append_row_with_default(dt, new_row_data, n)
print(dt)
