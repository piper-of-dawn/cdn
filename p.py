import polars as pl
from functools import lru_cache


@lru_cache(maxsize=1)
def load_portfolio(path: str) -> pl.DataFrame:
    return pl.read_csv(path)

# Step 2: Fill UNIQUE_ID with INVESTMENT_NAME if null
def fill_unique_id(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col("UNIQUE_ID").is_null())
        .then(pl.col("INVESTMENT_NAME"))
        .otherwise(pl.col("UNIQUE_ID"))
        .alias("UNIQUE_ID")
    )

# Step 3: Copy UNIQUE_ID to LSDB_ID
def sync_lsdb_id(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(pl.col("UNIQUE_ID").alias("LSDB_ID"))

# Step 4: Enforce uniqueness on UNIQUE_ID
def assert_unique_ids(df: pl.DataFrame):
    assert df.select("UNIQUE_ID").n_unique() == df.height, "UNIQUE_IDs must be unique."

# Step 5: Map BUSINESS_AREA_CD and BUSINESS_AREA_DESC using BUSINESS_DIVISION_CD
def map_business_area(df: pl.DataFrame) -> pl.DataFrame:
    mapping = {
        "N20979": ("N25354", "Non-Core and Legacy"),
        "N14952": ("N26934", "Investment Bank"),
        "N14949": ("N18083", "Personal & Corporate Banking"),
        "N14951": ("N20607", "Global Wealth Management"),
        "N14954": ("N18522", "Group Functions"),
        "N14953": ("N24552", "Asset Management"),
    }
    return df.with_columns([
        pl.col("BUSINESS_DIVISION_CD").map_dict(
            {k: v[0] for k, v in mapping.items()}, default=None
        ).alias("BUSINESS_AREA_CD"),
        pl.col("BUSINESS_DIVISION_CD").map_dict(
            {k: v[1] for k, v in mapping.items()}, default=None
        ).alias("BUSINESS_AREA_DESC"),
    ])

# Step 6: CLO override
def apply_clo_override(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns([
        pl.when(pl.col("SOURCE_CODE") == "CLO")
        .then("N30244")
        .otherwise(pl.col("BUSINESS_AREA_CD"))
        .alias("BUSINESS_AREA_CD"),
        
        pl.when(pl.col("SOURCE_CODE") == "CLO")
        .then("Credit Investments Group")
        .otherwise(pl.col("BUSINESS_AREA_DESC"))
        .alias("BUSINESS_AREA_DESC"),
    ])

# Step 7: Set constant INTERNAL_INVESTMENT_CATEGORY
def set_internal_category(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(pl.lit("CS").alias("INTERNAL_INVESTMENT_CATEGORY"))

# Main routine with assertions
def main(path: str):
    original = load_portfolio(path)
    df = original.clone()
    
    df = fill_unique_id(df)
    df = sync_lsdb_id(df)
    assert_unique_ids(df)

    df = map_business_area(df)
    df = apply_clo_override(df)
    df = set_internal_category(df)
    
    # Assertions
    assert df["LSDB_ID"].to_list() == df["UNIQUE_ID"].to_list(), "LSDB_ID must match UNIQUE_ID"
    assert not df["UNIQUE_ID"].is_null().any(), "UNIQUE_ID must not be null"
    assert all(v == "CS" for v in df["INTERNAL_INVESTMENT_CATEGORY"]), "INTERNAL_INVESTMENT_CATEGORY must be 'CS'"
    assert df["FAIR_VALUE"].to_list() == original["FAIR_VALUE"].to_list(), "FAIR_VALUE must not change"
    
    print("All assertions passed.")

# Example usage
# main("path_to_portfolio.csv")
