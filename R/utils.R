save_as_rds <- function(object, file_path) {
  tryCatch({
    saveRDS(object, file = file_path)
    cat("Object saved successfully as", file_path, "\n")
  }, error = function(e) {
    cat("Error occurred while saving the object:", e$message, "\n")
  })
}

