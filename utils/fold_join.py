def fold_join_dataframes(dataframes: list[pl.DataFrame], on: list[str]) -> pl.DataFrame:
    return reduce(lambda left, right: left.join(right, on=on, how="inner"), dataframes)
