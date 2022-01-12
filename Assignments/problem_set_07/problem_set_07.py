import csv

def read_csv_to_dicts(filepath, encoding='utf-8-sig', newline='', delimiter=','):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

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

def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)

# PROBLEM 2


def clean_data(data):
    """
    This function takes in data and returns a mutated version that converts string versions of numbers
    to their integer or float form depending on the type of value.

    Parameters:
        data (list): A list of dictionaries.

    Returns:
        (list): A list of dictionaries with the numerical values appropriately converted.
    """
    for standing in data:
        if 'points' in standing.keys():
            for x in standing['points']:
                standing['points'] = float(standing['points'])
        if 'position' in standing.keys():
            for y in standing['position']:
                standing['position'] = int(standing['position'])
    return(data)


# PROBLEM 3
def convert_time_to_ms(driver_dict):
    splits = driver_dict['fastest_lap'].split(':')
    a = int(splits[0]) * 60000
    b = int(splits[1]) * 1000
    c = int(splits[2])
    d = a + b + c
    return(d)



# PROBLEM 4
def add_fastest_lap_point(race_result):
    for result in race_result:
        lap_time = 98486
        if lap_time > convert_time_to_ms(result) and result['position'] <= 10:
            lap_time = convert_time_to_ms(result)
            result['points'] += 1
    return(race_result)

# PROBLEM 5
def update_driver_standings(standings, race_result):
    for standing in standings:
        for result in race_result:
            if standing['driver'] == result['name']:
                standing['points'] += result['points']
    return(standings)



# PROBLEM 6


def compare_points_by_nation(standings, nationality1, nationality2):
    """
    This function calculates the average points for all drivers for two nations and returns
    a tuple with the name and average points for the nation with the higher average points.

    Parameters:
        standings (list): A list of dictionaries that contains the drivers' standings.
        nationality1 (str): A string signifying the first nationality to be checked for.
        nationality2 (str): A string signifying the second nationality to be checked for.

    Returns:
        (tuple): A tuple with the nationality and average points for the nation with
        the higher average points.
    """
    nationality_1_sum = 0
    nationality_1_count = 0
    nationality_1_average = 0
    nationality_2_sum = 0
    nationality_2_count = 0
    nationality_2_average = 0
    nationality_1_nationality = None
    nationality_2_nationality = None
    for standing in standings:
        if nationality1 in standing['nationality']:
            nationality_1_count += 1
            nationality_1_sum += standing['points']
            nationality_1_nationality = standing['nationality']
        if nationality2 in standing['nationality']:
            nationality_2_count += 1
            nationality_2_sum += standing['points']
            nationality_2_nationality = standing['nationality']

    nationality_1_average = round(nationality_1_sum / nationality_1_count,1)
    nationality_2_average = round(nationality_2_sum / nationality_2_count,1)
    result = ()
    for standing in standings:
        if nationality_1_average > nationality_2_average:
            result = (nationality_1_nationality, nationality_1_average)
        elif nationality_2_average > nationality_1_average:
            result = (nationality_2_nationality, nationality_2_average)

    return(result)


#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """

    # PROBLEM 1
    standings = read_csv_to_dicts('driver_standings_pre_USGP.csv')
    race_result = read_csv_to_dicts('usgp_results.csv')
    #print(f'\n{standings}')
    #print(f'\n{race_result}')

    last_standing_keys = standings[-1].keys()
    #print(f'\n{last_standing_keys}')

    third_standing_values = standings[2].values()
    #print(f'\n{third_standing_values}')

    tenth_race_result_kv = race_result[9].items()
    #print(f'\n{tenth_race_result_kv}')

    # PROBLEM 2
    cleaned_standings = clean_data(standings)
    #print(f'\nCleaned standings:\n{cleaned_standings}')

    cleaned_race_result = clean_data(race_result)
    #print(f'\nCleaned race results:\n{cleaned_race_result}')
    #print(cleaned_race_result[0])

    # PROBLEM 3 (Optional Check)
    #test_check = convert_time_to_ms(cleaned_race_result[0])
    #print(test_check)

    # PROBLEM 4
    updated_race_result = add_fastest_lap_point(cleaned_race_result)
    #print(updated_race_result)


    # PROBLEM 5
    updated_standings = update_driver_standings(cleaned_standings, updated_race_result)
    print(updated_standings)

    # PROBLEM 6
    ger_vs_gbr = compare_points_by_nation(updated_standings, 'British', 'German')
    fra_vs_spa = compare_points_by_nation(updated_standings, 'French', 'Spanish')
    print(ger_vs_gbr)
    print(fra_vs_spa)

    # PROBLEM 7
    write_filepath = 'driver_standings_post_USGP.csv'
    write_fieldnames = ['driver', 'team', 'nationality', 'points']
    write_dicts_to_csv(write_filepath, updated_standings, write_fieldnames)

#DO NOT EDIT
if __name__ == '__main__':
    main()
