from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

def filter_dataframe_by_date(input_df):
    # Assuming the date column is named 'date_column', change it accordingly
    date_column_name = 'date_column'
    
    # Convert the date column to a DateType
    formatted_date_column = to_date(col(date_column_name), 'dd/MM/yyyy')
    
    # Specify the target date for filtering
    target_date = '2023-02-28'
    
    # Filter the DataFrame
    filtered_df = input_df.filter(formatted_date_column == target_date)
    
    return filtered_df
