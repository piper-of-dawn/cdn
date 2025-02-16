library(data.table)

get_data <- function(path = NULL, fun = NULL) {
  # If a valid path string is provided and the file exists, use fread.
  if (!is.null(path) && is.character(path) && file.exists(path)) {
    return(fread(path))
  }
  # Otherwise, if a valid function is provided, execute it.
  else if (!is.null(fun) && is.function(fun)) {
    dt <- fun()
    if (!"data.table" %in% class(dt)) {
      stop("The provided function did not return a data.table.")
    }
    return(dt)
  }
  # If neither a valid path nor function is provided, throw an error.
  stop("Invalid input: Provide either a valid file path or a function that returns a data.table.")
}
