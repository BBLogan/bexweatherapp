import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# READ THE DOC STRINGS - THE FORMULA IS THE ONE YOU'RE USING AT THE TOP OF EACH PROBLEM

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

    pass

# this one done
def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    try:
        # moving the ISO string into a datetime object
        date_object = datetime.fromisoformat(iso_string)

        # formatting the datetime object into the desired string format
        formatted_date = date_object.strftime('%A %d %B %Y')
        return formatted_date
    
    except ValueError:
        # handles the invalid ISO strings
        return "Invalid date format"
    
    #strftime = string format time funtion 
    #date_object has the following parts: %A - full weekday name; %d - day of the month as a zero-padded decimal number (01, 0); %B - full month name; %Y - year with century as a decimal number (four digit year - 2023)
    pass

# this one done
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celcius = round((float(temp_in_farenheit) - 32) * (5/9), 1)
    return celcius
    
    pass

# this one done
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # # Filter out non-numeric values from the list
    # numeric_data = [value for value in weather_data if isinstance(value, (int, float))]

    # Check if the list is empty to avoid division by zero
    if not weather_data:
        return None

    # starting the sum and count
    total = 0
    count = 0

    # move through the data
    for value in weather_data:
        try:
            # attempting to convert the value to a float
            numeric_value = float(value)
            total += numeric_value
            count += 1
        except ValueError:
            # ignoring non-numerica values
            pass
    
    # check if all values are non-numeric
    if count == 0:
        return None
    
    # calculate the mean by dividing the total by the count
    mean_value = total / count
    return mean_value

    # # Calculate the mean by summing up the numeric values and dividing by the number of elements
    # mean_value = sum(numeric_data) / len(numeric_data)
    # return mean_value
    pass

# do this one NEXT - just open a CSV file  - REMEMBER TO CHANGE WHICH TEST FILES ARE ACTIVE AND WHICH AREN'T run_tests.py
def load_data_from_csv(csv_file):  
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
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
