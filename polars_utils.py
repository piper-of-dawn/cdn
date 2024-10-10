import polars as pl
from collections import namedtuple
from typing import List

def compare_dataframes(first: pl.DataFrame, second: pl.DataFrame, key_column: str) -> namedtuple:
    # Create a named tuple for return type
    DiffResult = namedtuple('DiffResult', ['in_first_not_second', 'in_second_not_first'])
    
    # Validate that both dataframes have the same schema
    if first.schema != second.schema:
        raise ValueError("Dataframes have different schemas")
    
    # Validate that key_column exists in both dataframes
    if key_column not in first.columns or key_column not in second.columns:
        raise ValueError(f"Key column '{key_column}' not found in one or both dataframes")
    
    # Find rows in first that are not in second
    in_first_not_second = first.join(
        second,
        on=first.columns,
        how="anti"
    )
    
    # Find rows in second that are not in first
    in_second_not_first = second.join(
        first,
        on=second.columns,
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

