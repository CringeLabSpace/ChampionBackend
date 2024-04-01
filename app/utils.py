import datetime


def format_current_time():
    current_date = datetime.datetime.now()
    formatted_time = current_date.strftime("%d-%m-%Y %H:%M:%S")
    return formatted_time