import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# READ THE DOC STRINGS - THE FORMULA IS THE ONE YOU'RE USING AT THE TOP OF EACH 


# this one done
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


# do this one 5th - google the words in the mulitple "" - docstrings - CSV examples
def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

# this one done
def convert_f_to_c(temp_in_farenheit):
    celcius = round((float(temp_in_farenheit) - 32) * (5/9), 1)
    return celcius

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

# do this one 4th - what's the mean forumla  - REMEMBER TO CHANGE WHICH TEST FILES ARE ACTIVE AND WHICH AREN'T run_tests.py - for this one to pass look at what the number types are in the test_calculate_mean.py file
def calculate_mean(weather_data):
    
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

# do this one 3rd - just open a CSV file  - REMEMBER TO CHANGE WHICH TEST FILES ARE ACTIVE AND WHICH AREN'T run_tests.py
def load_data_from_csv(csv_file):
    data = [] 
    # the above starts an empty list to store the CSV data

    try:
        with open(csv_file, mode='r', newline='', encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        
        return data
    except FileNotFoundError:
        # handle if file doesn't exist
        return None
    
    except Exception as e:
        # any other errors which may occur during file reading
        print("An error occurred: ", str(e))
        return None
    
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

# do this one 6th - and then follow on with the max (max = inverse of this one) - REMEMBER TO CHANGE WHICH TEST FILES ARE ACTIVE AND WHICH AREN'T run_tests.py
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass

# do this one 7th - after the find_min
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass

# need to do the ones above before attempting this one
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

# need to do the ones above before attempting this one
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
