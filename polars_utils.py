import polars as pl
from collections import namedtuple
from typing import List

def compare_dataframes(df1: pl.DataFrame, df2: pl.DataFrame, key_column: str) -> namedtuple:
    # Create a named tuple for return type
    DiffResult = namedtuple('DiffResult', ['in_first_not_second', 'in_second_not_first'])
    
    # Validate that both dataframes have the same schema
    if df1.schema != df2.schema:
        raise ValueError("Dataframes have different schemas")
    
    # Validate that key_column exists in both dataframes
    if key_column not in df1.columns or key_column not in df2.columns:
        raise ValueError(f"Key column '{key_column}' not found in one or both dataframes")
    
    # Find rows in df1 that are not in df2
    in_first_not_second = df1.join(
        df2,
        on=df1.columns,
        how="anti"
    )
    
    # Find rows in df2 that are not in df1
    in_second_not_first = df2.join(
        df1,
        on=df2.columns,
        how="anti"
    )
    
    return DiffResult(in_first_not_second, in_second_not_first)

# Example usage
def example_usage():
    # Create sample dataframes
    df1 = pl.DataFrame({
        "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, 40]
    })
    
    df2 = pl.DataFrame({
        "id": [1, 2, 5, 6],
        "name": ["Alice", "Bob", "Eve", "Frank"],
        "age": [25, 30, 45, 50]
    })
    
    # Compare dataframes
    result = compare_dataframes(df1, df2, "id")
    
    print("Rows in first but not in second:")
    print(result.in_first_not_second)
    
    print("\nRows in second but not in first:")
    print(result.in_second_not_first)

