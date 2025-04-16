save_as_rds <- function(object, file_path) {
  tryCatch({
    saveRDS(object, file = file_path)
    cat("Object saved successfully as", file_path, "\n")
  }, error = function(e) {
    cat("Error occurred while saving the object:", e$message, "\n")
  })
}
read_json_as_character <- function(file_path) {
  # Read the JSON file
  json_data <- fromJSON(file_path, simplifyVector = FALSE)
  
  # Convert the JSON object to a character vector
  json_string <- toJSON(json_data, pretty = TRUE)
  
  return(json_string)
}
read_json_as_character <- function(file_path) {
  # Read the JSON file content as a raw character string
  json_string <- readLines(file_path, warn = FALSE)
  
  # Combine the lines into a single character string
  json_character <- paste(json_string, collapse = "\n")
  
  return(json_character)
}

library(data.table)
library(knitr)

pretty_print_info <- function(data) {
  # Check if input is a named list or a data.table
  if (is.list(data) && !is.data.table(data)) {
    # Convert named list to data.table
    data <- as.data.table(data)
  } else if (!is.data.table(data)) {
    stop("Input must be a named list or data.table")
  }
  
  # Print dimensions of the dataframe
  cat("Dimensions of the data frame:\n")
  cat(paste("Rows:", nrow(data), "Columns:", ncol(data), "\n\n"))
  
  # Initialize a data.table to store column information
  info <- data.table(
    "Column Name" = character(),
    "Data Type" = character(),
    "Number of Missing Values" = integer()
  )
  
  # Loop through each column and collect required information
  for (col in names(data)) {
    col_name <- col
    col_type <- class(data[[col]])
    col_missing <- sum(is.na(data[[col]]))
    
    info <- rbind(info, list(col_name, col_type, col_missing))
  }
  
  # Print the information table
  cat("Column Information:\n")
  print(kable(info, format = "pipe", align = c("l", "l", "r")))
  
  # Print the last 5 rows of the dataframe
  cat("\nLast 5 Rows of the Data Frame:\n")
  last_rows <- tail(data, 5)
  print(kable(last_rows, format = "pipe"))
}

# Example usage with a named list
named_list <- list(
  A = c(1, 2, NA, 4, 5, 6),
  B = c("a", "b", "c", "d", "e", "f"),
  C = c(TRUE, FALSE, TRUE, NA, TRUE, FALSE)
)

pretty_print_info(named_list)

# Example usage with a data.table
dt <- data.table(
  A = c(1, 2, NA, 4, 5, 6),
  B = c("a", "b", "c", "d", "e", "f"),
  C = c(TRUE, FALSE, TRUE, NA, TRUE, FALSE)
)

pretty_print_info(dt)



read_config <- function(config_file) {
  config_lines <- readLines(config_file) 

  config_list <- list()  

  for (line in config_lines) {

    parts <- strsplit(line, ":\\s*")[[1]]
    
    if (length(parts) == 2) {
      # Trim whitespaces and add to the list
      attribute <- trimws(parts[1])
      path <- trimws(parts[2])
      
      config_list[[attribute]] <- path
    }
  }
  
  # Return the configuration list with FALSE if an attribute is not found
  return(function(attribute) {
    if (!is.null(config_list[[attribute]])) {
      return(config_list[[attribute]])
    } else {
      return(FALSE)
    }
  })
}


#  Configurtion looks like this
# ATTRIBUTE_1: /path/to/file1.csv
# ATTRIBUTE_2: /path/to/file2.csv
# ATTRIBUTE_3: /path/to/file3.csv

# Example Usage
config <- read_config("config.yaml")
attribute_value <- config("ATTRIBUTE_5")  # Gets the path for ATTRIBUTE_1 or FALSE if not found
print(attribute_value) # THIS RETURNS FALSE

attribute_value <- config("ATTRIBUTE_1")  # Gets the path for ATTRIBUTE_1 or FALSE if not found
print(attribute_value) # THIS RETURNS "/path/to/file1.csv"

filter_and_replace <- function(dt, column_name, filter_string, replace_list) {
    # Input validation
    if (!is.data.table(dt)) {
        stop("Input must be a data.table")
    }
    if (!column_name %in% names(dt)) {
        stop("Column name not found in data.table")
    }
    if (!all(names(replace_list) %in% names(dt))) {
        stop("Some columns in replace_list not found in data.table")
    }
    
    # Create a copy to avoid modifying the original data.table
    result_dt <- copy(dt)
    
    # Use .SD to update multiple columns at once
    result_dt[get(column_name) == filter_string, 
             (names(replace_list)) := replace_list]
    
    return(result_dt)
}

remove_special_characters <- function(name) {
  # Replace all non-alphanumeric characters (except space) with an underscore
  sanitized_name <- gsub("[^[:alnum:] ]", "_", name)
  return(sanitized_name)
}

# Example usage
name <- "my@csv#file$name.csv"
sanitized_name <- remove_special_characters(name)
cat("Sanitized name:", sanitized_name)

import re

def remove_special_characters(name):
    # Replace all non-alphanumeric characters (except spaces) with an underscore
    sanitized_name = re.sub(r'[^A-Za-z0-9 ]', '_', name)
    return sanitized_name

# Example usage
name = "my@csv#file$name.csv"
sanitized_name = remove_special_characters(name)
print("Sanitized name:", sanitized_name)




library(data.table)

check_and_read_csv <- function(i, path) {
  file_path <- file.path(path, paste0("P", i, ".csv"))
  
  if (file.exists(file_path)) {
    dt <- fread(file_path, nrows = 500001) # Read one extra row to check count
    
    if (nrow(dt) == 500000) {
      return(dt)
    } else {
      message("File exists but does not have exactly 500,000 rows.")
    }
  } else {
    message("File does not exist: ", file_path)
  }
  
  return(NULL)
}


library(dplyr)

mutate_volatility_factor <- function(df) {
  df %>%
    mutate(volatility_factor = if_else(
      volatility_factor == "NA",
      sqrt(1.8^2 - 1 + as.numeric(beta_factor)^2),
      as.numeric(volatility_factor)
    ))
}

