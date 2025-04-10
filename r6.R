library(R6)

# Define the URLHandler class
mptHandler <- R6Class(
  "MPT",
  
  # Public members
  public = list(
    # Constructor (initialize method)
    initialize = function(url) {
      private$validate_url(url)
      private$url <- url
      private$domain <- private$extract_domain(url)
    },
    
    # Method to print URL information
    print_info = function() {
      cat("URL Information:\n")
      cat("  Full URL:", private$url, "\n")
      cat("  Domain:", private$domain, "\n")
      cat("  Protocol:", private$extract_protocol(), "\n")
      cat("  Last accessed:", as.character(private$last_accessed), "\n")
      
      # Update last accessed time
      private$update_access_time()
    }
  ),
  
  # Private members
  private = list(
    url = NULL,
    domain = NULL,
    last_accessed = NULL,
    
    # Helper method to validate URL format
    validate_url = function(url) {
      if (!grepl("^https?://", url)) {
        stop("Invalid URL format. Must start with http:// or https://")
      }
    },
    
    # Helper method to extract domain
    extract_domain = function(url) {
      domain <- gsub("^https?://([^/]+).*", "\\1", url)
      return(domain)
    },
    
    # Helper method to extract protocol
    extract_protocol = function() {
      if (grepl("^https://", private$url)) {
        return("HTTPS")
      } else {
        return("HTTP")
      }
    },
    
    # Helper method to update access time
    update_access_time = function() {
      private$last_accessed <- Sys.time()
    }
  )
)

# Example usage:
# Create an instance of the URLHandler
url_obj <- URLHandler$new("https://www.example.com/path/to/page")

# Call the print_info method
url_obj$print_info()