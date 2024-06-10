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

