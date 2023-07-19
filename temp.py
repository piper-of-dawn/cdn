from datetime import datetime, timedelta

def convert_date_format(input_date):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(input_date, '%Y%m')

    # Find the last day of the month
    last_day_of_month = (date_obj.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Convert the date to the desired format "DDMMYYYY"
    output_date = last_day_of_month.strftime('%d%m%Y')

    return output_date
