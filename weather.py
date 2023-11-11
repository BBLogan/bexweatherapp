import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        date_object = datetime.fromisoformat(iso_string)
        formatted_date = date_object.strftime('%A %d %B %Y')
        return formatted_date
    except ValueError:
        return "Invalid date format"

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celcius = round((float(temp_in_farenheit) - 32) * (5/9), 1)
    return celcius

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if not weather_data:
        return None
    
    total = 0
    count = 0

    for value in weather_data:
        try:
            numeric_value = float(value)
            total += numeric_value
            count += 1
        except ValueError:
            pass
    
    if count == 0:
        return None

    mean_value = total / count
    return mean_value

def load_data_from_csv(csv_file):  
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, 'r', newline="", encoding="utf-8", ) as file:
        csv_reader = csv.reader(file)
        
        header = next(csv_reader, None)

        for row in csv_reader:
            if len(row) == 3:
                date, min_temp, max_temp = row
                data.append([date, int(min_temp), int(max_temp)])
    return data

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    min_value = None
    min_index = None

    for i, value in enumerate(weather_data):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                continue

        if min_value is None or value < min_value:
            min_value = value
            min_index = i
        elif value == min_value:
            min_index = i

    return min_value, min_index

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    max_value = None
    max_index = None

    for i, value in enumerate(weather_data):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                continue

        if max_value is None or value > max_value:
            max_value = value
            max_index = i
        elif value == max_value:
            max_index = i

    return max_value, max_index

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No weather data available."
    
    summary = []
    summary = f"{len(weather_data)} Day Overview\n"

    min_values = [day[1] for day in weather_data]
    min_temp_value, min_temp_index = find_min(min_values)
    min_temp_date = weather_data[min_temp_index][0]

    max_values = [day[2] for day in weather_data]
    max_temp_value, max_temp_index = find_max(max_values)
    max_temp_date = weather_data[max_temp_index][0]

    summary += f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp_value))}, and will occur on {convert_date(min_temp_date)}.\n"
    summary += f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp_value))}, and will occur on {convert_date(max_temp_date)}.\n"

    avg_min = format_temperature(convert_f_to_c(calculate_mean(min_values)))
    avg_max = format_temperature(convert_f_to_c(calculate_mean(max_values)))

    summary += f"  The average low this week is {avg_min}.\n"
    summary += f"  The average high this week is {avg_max}.\n"

    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No weather data available."
    
    summary = ""

    for day in weather_data:
        date = day[0]
        min_value = day[1]
        max_value = day[2]
    
        summary += f"---- {convert_date(date)} ----\n"
        summary += f"  Minimum Temperature: {format_temperature(convert_f_to_c(min_value))}\n"
        summary += f"  Maximum Temperature: {format_temperature(convert_f_to_c(max_value))}\n\n"

    return summary