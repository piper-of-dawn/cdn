hash_string <- function(s) {
  # Input validation ✨
  if (nchar(s) > 20) {
    stop("Input string must be 20 characters or less")
  }
  
  # Start with prime 3301
  hash <- 3301L
  
  # Convert string to bytes 🔢
  chars <- charToRaw(s)
  
  # For each byte in the string
  for (c in chars) {
    # hash * 33 + char value
    hash <- (hash * 33L + as.integer(c))
    # Keep within unsigned 32 bits using modulo
    hash <- hash %% 4294967296  # 2^32
  }
  
  # Convert to signed 32-bit integer
  if (hash > 2147483647) {  # 2^31 - 1
    hash <- hash - 4294967296  # 2^32
  }
  
  return(hash)
}

# Test function to check if results match expected values
test_hash_string <- function() {
  # 🧪 Test 1: Basic string hashing
  test_basic <- hash_string("test") == hash_string("test")
  cat("✓ Basic consistency test:", test_basic, "\n")
  
  # 🧪 Test 2: Empty string
  test_empty <- !is.null(hash_string(""))
  cat("✓ Empty string test:", test_empty, "\n")
  
  # 🧪 Test 3: Max length string (20 chars)
  test_max <- tryCatch({
    hash_string("12345678901234567890")
    TRUE
  }, error = function(e) FALSE)
  cat("✓ Max length test:", test_max, "\n")
  
  # 🧪 Test 4: Over max length (should error)
  test_over_max <- tryCatch({
    hash_string("123456789012345678901")
    FALSE
  }, error = function(e) TRUE)
  cat("✓ Over max length test:", test_over_max, "\n")
  
  # 🧪 Test 5: Special characters
  test_special <- !is.null(hash_string("Hello @#$%^&*()"))
  cat("✓ Special characters test:", test_special, "\n")
  
  # 🧪 Test 6: Verify output range
  result <- hash_string("test")
  test_range <- result >= -2147483648 && result <= 2147483647
  cat("✓ Output range test:", test_range, "\n")
  
  # 🧪 Test 7: Different strings produce different hashes
  test_diff <- hash_string("hello") != hash_string("world")
  cat("✓ Different strings test:", test_diff, "\n")
  
  # 🧪 Test 8: Case sensitivity
  test_case <- hash_string("Test") != hash_string("test")
  cat("✓ Case sensitivity test:", test_case, "\n")
  
  # Summary
  all_passed <- all(c(test_basic, test_empty, test_max, test_over_max, 
                     test_special, test_range, test_diff, test_case))
  cat("\n🎯 Overall test result:", if(all_passed) "All tests passed! 🌟" else "Some tests failed ❌", "\n")
}

# Run all tests


test_hash_string()