import csv
import json
import requests


# Constants
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api/'
SWAPI_CATEGORES = f"{SWAPI_ENDPOINT}/"
SWAPI_FILMS = f"{SWAPI_ENDPOINT}/films/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"
SWAPI_VEHICLES = f"{SWAPI_ENDPOINT}/vehicles/"


def convert_gravity_value(value):
    """Convert a planet's "gravity" value to a float. Removes the "standard" unit of measure if
    it exists in the string. Delegates to the function < convert_to_float > the task of casting
    the < value > to a float.

    Parameters:
        value (obj): string to be converted

    Returns:
        float: if value successfully converted; otherwise returns value unchanged
    """
    try:

        if 'standard' in value:
            return convert_to_float(value.strip('standard'))
        else:
            return convert_to_float(value)
    except:
        return value


def convert_to_float(value):
    """Attempts to convert a string or a number < value > to a float. If unsuccessful or an
    exception is encountered returns the < value > unchanged. Note that this function will
    return True for boolean values, faux string boolean values (e.g., "true"), "NaN", exponential
    notation, etc.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        float: if value successfully converted; otherwise returns value unchanged
    """

    try:
        return float(value)
    except:
        return(value)


def convert_to_int(value):
    """Attempts to convert a string or a number < value > to an int. If unsuccessful or an
    exception is encountered returns the < value > unchanged. Note that this function will return
    True for boolean values, faux string boolean values (e.g., "true"), "NaN", exponential
    notation, etc.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        int: if value successfully converted; otherwise returns value unchanged
    """

    try:
        return int(value)
    except:
        return value


def convert_to_list(value, delimiter=None):
    """Attempts to convert a string < value > to a list using the provided < delimiter >. Removes
    leading/trailing spaces before converting < value > to a list. If unsuccessful or an exception
    is encountered returns the < value > unchanged.

    Parameters:
        value (str): string to be split.
        delimiter (str): optional delimiter provided for splitting the string

    Returns:
         list: string converted to a list.
    """

    try:
        if delimiter :
            return value.split(delimiter)
        else:
            return value.split()
    except:
        return value


def convert_to_none(value):
    """Attempts to convert the passed in < value > to < None > if it matches any of the following
    strings: "n/a", "N/A", "none", "None", "unknown" "Unknown" (i.e., a case-insensitive check).
    If no match is obtained or an exception is encountered the < value > is returned unchanged.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        int: if value successfully converted; otherwise returns value unchanged
    """
    try:
        if value.lower() == 'n/a':
            value = None
        elif value.lower() == 'none':
                value = None
        elif value.lower() == 'unknown':
            value = None
        elif value.lower() == "":
            value = None
        return value
    except:
        return value



def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: a list of nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of dictionaries that
    represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)
