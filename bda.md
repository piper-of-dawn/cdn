# Add total_loss_with_liquidity and total_loss_without_liquidity to each element of the list
simulation_list <- lapply(simulation_list, function(df) {
  df$total_loss_with_liquidity <- df$market_loss + df$liquidity_loss + df$default_loss
  df$total_loss_without_liquidity <- df$market_loss + df$default_loss
  return(df)
})
