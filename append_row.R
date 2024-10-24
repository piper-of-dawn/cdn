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
move_row_to_end <- function(dt, n) {
  # Check if dt is a data.table
  if (!is.data.table(dt)) {
    stop("Input must be a data.table")
  }
  
  # Check if n is numeric
  if (!is.numeric(n)) {
    stop("Row number 'n' must be numeric")
  }
  
  # Check if n is an integer
  if (n != as.integer(n)) {
    stop("Row number 'n' must be an integer")
  }
  
  # Check if n is within the range of the number of rows
  if (n > nrow(dt) || n <= 0) {
    stop("Row number 'n' is out of range")
  }
  
  # Extract the nth row
  row_to_move <- dt[n]
  
  # Remove the nth row from the data.table
  dt <- dt[-n]
  
  # Add the extracted row to the end of the data.table
  dt <- rbind(dt, row_to_move)
  
  return(dt)
}
