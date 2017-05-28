import csv
from pip._vendor import requests

'''
Helper methods that parse the data from the Google Finance Website. These methods
parse data into the form of a list to allow easy plotting on the constructed graph

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 26 May 2017

'''


def parse_data(stock_code):
    '''
    Parses the data of the CSV file into a 2D list. (List within Lists). This allow
    easy data selects to be done

    Args:
        stock_code (str) : The stock data for which we are parsing data for
    Returns:
        (list)(list) : A 2D list that contains data parsed in from the downloaded CSV file
    '''
    url = 'http://www.google.com/finance/historical?output=csv&q={}'.format(stock_code)
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)


def collect_date_range(csv_data):
    '''
    Collects the list of dates included on the CSV data file. This data corresponds
    to the stock data given for each of the respective dates

    Args:
        csv_data (list)(list) : The parsed in CSV data from which we select a designated
            column from all rows. (The row that corresponds to the date field)

    Returns:
        (list) The list of dates in string format given on the CSV file
    '''
    date_range = []
    for item in csv_data:  # Iterate through all rows on the CSV file
        date_range.append(item[0])  # Column 1 contains the date values on each row
    del date_range[0]        # This row deletes the title string (first row parsed) which is first on the list
    return date_range


def collect_all_opening_values(csv_data):
    '''
    Collects the list of opening values included on the CSV data file. This data corresponds
    to the data on each row in the CSV file

    Args:
        csv_data (list)(list) : The parsed in CSV data from which we select a designated
            column from all rows. (The row that corresponds to the opening values field)

    Returns:
        (list) The list of opening values in float format given on the CSV file
    '''
    all_opening_values = []
    for item in csv_data:   # Iterate through all rows on the CSV file
        all_opening_values.append(item[1])    # Column 2 contains the date values on each row
    del all_opening_values[0]     # This row deletes the title string (first row parsed) which is first on the list
    return [float(i) for i in all_opening_values]


def collect_all_closing_values(list):
    '''
    Collects the list of closing values included on the CSV data file. This data corresponds
    to the data on each row in the CSV file

    Args:
        csv_data (list)(list) : The parsed in CSV data from which we select a designated
            column from all rows. (The row that corresponds to the closing values field)

    Returns:
        (list) The list of closing values in float format given on the CSV file
    '''
    all_closing_values = []
    for item in list:   # Iterate through all rows on the CSV file
        all_closing_values.append(item[4])    # Column 5 contains the date values on each row
    del all_closing_values[0]
    return [float(i) for i in all_closing_values]

