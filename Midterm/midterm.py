# SI 506 Midterm

from copy import deepcopy
import csv
from os import get_terminal_size


def calculate_points(club):
    """Computes club's total points after converting string values to integers
    based on the following equation:

    3 points per win + 1 point per draw. A loss nets zero points.

    Parameters:
        club (list): representation of a club

    Returns
        int: league points earned
    """
    sum_points = (club[2] * 3) + club[3] 
    return(sum_points)


def calculate_shot_conversation_rate(club, shot_category='shots'):
    """Calculates a club's goal scoring efficiency by dividing goals scored
    by either all shots attempted (< shots >) OR shots considered on target,
    i.e., shots on goal (< shots_on_goal >).

    Dividing a club's < goals_for > by < shots_on_goal > will result in a higher
    shot conversion rate than dividing by < shots >.

    The caller must pass in the string 'shots_on_goal' as an optional second
    argument in order to instruct the function to switch the divisor. Otherwise,
    the calculation is performed using the < shots > value as the divisor.

    Either way, the resulting conversion rate value is rounded to the third
    (3rd) decimal place before it is returned to the caller.

    Parameters:
        club (list): representation of a club
        shot_category (str): indicates the divisor to use when performing the
                             calculation (e.g., shots or shots on goal)

    Returns
        float: conversion rate rounded to the 3rd decimal place
    """
    shot_calc = 0
    if shot_category == 'shots_on_goal':
        shot_calc = round(club[5] / club[8], 3)
    elif shot_category == 'shots':
        shot_calc = round(club[5] / club[7], 3)
    return(shot_calc)



def calculate_goals_by_top_scorers_pct(club, top_scorers):
    """Calculates the percentage of club goals scored by league-recognized top
    scorers. The function delegates to < get_club_top_scorers > the task of
    retrieving the club's league-recognized top scorers. It then divides the
    number of goals scored by the top scorers by the club's < goals_for > (GF)
    multipled by 100 to obtain the percentage value. The percentage value is
    then rounded to the second (2nd) decimal place.

    The return value is a three-item tuple comprising a club's goals for,
    the top scorers goal count, and the computed percentage value of club
    goals scored by its league-recognized top scorers:

    (< goals for >, < top scorers goals >, < top scorers goals percent >)

    Parameters:
        club (list): representation of a club
        top_scorers (list): League-recognized top scorers

    Returns:
        tuple: comprising the club's goals for, top scorers goal count, and the
               percentage of club goals scored the club's top scorers rounded
               to the second (2nd) decimal place
     """
    club_top_scorers = get_club_top_scorers(top_scorers, club[0])
    goals_for = club[5]
    top_scorers_goals = 0
    top_scorers_goals_pct = 0
    for i in club_top_scorers:
        i[3] = int(i[3])
        top_scorers_goals = top_scorers_goals + i[3]
    top_scorers_goals_pct = top_scorers_goals / goals_for
    top_scorers_goals_pct = round(top_scorers_goals_pct * 100, 2)
    club_result = (goals_for, top_scorers_goals, top_scorers_goals_pct)
    return(club_result)


def classify_club(club):
    """Classifies a club according to a three-tiered ranking system: 'top_tier',
    'middle_tier', 'bottom_tier'. Classifying a club is based on points earned
    during a particular season. The function delegates to < calculate_points >
    the task of calculating the club's points.

    Assigning a club to a tier is based on the following points scheme.

    Tiers:
        top_tier: > 35 points
        middle_tier: between 32 and 35 points (inclusive)
        bottom_tier: < 32 points

    Once the club is classified the function returns to the caller one of
    three labels: 'top_tier', 'middle_tier', or 'bottom_tier'.

    Parameters:
        club (list): representation of a club

    Returns:
        str: classification label
    """
    club_points = calculate_points(club)
    club_type = None
    if club_points > 35:
        club_type = 'top_tier'
    elif 32 <= club_points <= 35:
        club_type = 'middle_tier'
    elif club_points <32:
        club_type = 'bottom_tier'
    return(club_type)




def clean_club(club):
    """Converts number values read in as strings from the CSV file to integers.
    The club name string is ignored.

    Parameters:
        club (list): representation of a club

    Returns:
        list: mutated club list with "number" strings converted to integers
    """
    club_copy = club
    for i in range(len(club_copy)):
        if i == 0:
            continue
        club_copy[i] = int(club_copy[i])
    return(club_copy)


def combine_data(club_info, standings, top_scorers):
    """Modifies the < club_info > list to include club records, top scorer-based
    statistics, shot conversion metrics, and club classifications. Delegates a
    number of tasks to other functions to retrieve the additional data.

    Additional data added to each of the nested club records in < club_info > includes:
        1. club record statistics (e.g., all values from matches played to points earned )
        2. count of a club's league-recognized top scorers, if any
        3. number of goals scored by a club's league-recognized top scorers, if any
        4. percentage of club's goals scored by league-recognized top scorers, if any
        5. shot conversion rate (all shots taken)
        6. shots on goal conversion rate
        7. club classification (e.g., 'top_tier', 'middle_tier', 'bottom_tier')

    Parameters:
        club_info (list): representation of a club
        standings (list): league standings
        top_scorers (list): League-recognized top scorers

    Returns:
       list: mutated < club_info > list containing additional data about each club
    """
    new_club_info = deepcopy(club_info)
    top_scorers_count = get_clubs_top_scorers_counts(standings,top_scorers)
    shot_conversion_rate = get_clubs_shot_conversion_rates(standings, shot_category = 'shots')
    shots_on_goal_conversion_rate = get_clubs_shot_conversion_rates(standings,shot_category = 'shots_on_goal')
    for x in new_club_info:
        for y in standings:
            if x[0] == y[0]:
                x.extend(y[1:])
        for a in top_scorers_count:
            if a[0] == x[0]:
                x.append(a[1])
        for y in standings:
             if x[0] == y[0]:
                    x.append(calculate_goals_by_top_scorers_pct(y, top_scorers)[1])
                    x.append(calculate_goals_by_top_scorers_pct(y, top_scorers)[2])
        for b in shot_conversion_rate:
            if x[0] == b[0]:
                x.append(b[1])
        for z in shots_on_goal_conversion_rate:
            if x[0] == z[0]:
                x.append(z[1])
        for y in standings:
            if x[0] == y[0]:
                x.append([y[0],classify_club(y)][1])
    return(new_club_info)


def get_club_record(standings, club_name):
    """Returns a club record by the club's name. The name check is case-insentive.
    If a match on the club name is not obtained None is returned.

    Parameters:
        standings (list): league standings
        club_name (str): club name

    Returns
        list: representation of a club if match obtained; otherwise returns None
    """
    club_record = None
    for x in standings:
        if x[0].lower() == club_name.lower():
            club_record = x
    return(club_record)




def get_club_top_scorers(top_scorers, club_name):
    """Filters league's top scorers by club affiliation. Performs a case
    insensitive comparison of the player's club name with the passed in
    < club_name >.

    Parameters:
        top_scorers (list): League-recognized top scorers
        club_name (str): club name to which the top scorer(s) are affiliated

    Returns:
        list: top scorer(s), if any, affiliated with the club
    """
    top_scorer = []
    for i in top_scorers:
        if i[2].lower() == club_name.lower():
            top_scorer.append(i)
    return(top_scorer)





def get_clubs_shot_conversion_rates(standings, shot_category='shots'):
    """Tabulates shot conversion rates for all clubs in < standings >. The
    function delegates to < calculate_shot_conversation_rate >
    the task of returning either its shot conversion rate or shots on goal
    conversion rate depending on the < shot_category > passed to the function
    < calculate_shot_conversation_rate >.

    The conversion rate returned by calling < calculate_shot_conversation_rate >
    is added to a tuple along with the club name, e.g.,

    (< club name >, < shot conversion rate >)

    The tuple is then appended to a local accumulator list. After all club
    conversion rates have been retrieved, the list of nested tuples is returned
    to the caller.

    Parameters:
        standings (list): league standings
        shot_category (str): indicates the divisor to use when performing the
                             calculation (e.g., shots or shots on goal)

    Returns:
        list: nested tuples of club shot conversion rates
    """
    club_calc = []
    club_name = []
    for x in standings:
        if shot_category == 'shots':
            club_calc.append(calculate_shot_conversation_rate(x))
        elif shot_category == 'shots_on_goal':
                club_calc.append(calculate_shot_conversation_rate(x, 'shots_on_goal'))
        club_name.append(x[0])
    clubs_with_calc = list(zip(club_name, club_calc))
    return(clubs_with_calc)


def get_clubs_top_scorers_counts(standings, top_scorers):
    """Tabulates counts of club affiliated league-recognized top scorers for
    all clubs in < standings>. The function delegates to < get_club_top_scorers >
    the task of retrieving each club's league-recognized top scorers. The number
    of elements in the list returned by < get_club_top_scorers > constitutes the
    count.

    The club's name along with the count is placed in a tuple, e.g.,
    (< club name >, < top scorers count> ) which is appended to a local
    accumulator list. After each club's top scorers, if any, are retrieved
    and counted the accumulator list is returned to the caller.

    Parameters:
        standings (list): league standings
        top_scorers (list): League-recognized top scorers

    Returns:
       list: nested tuples of top scorer counts for each passed in club
    """
    scorer_count = []
    scorer_name = []
    for x in standings:
     scorer_count.append(len(get_club_top_scorers(top_scorers,x[0])))
     scorer_name.append(x[0])
    the_count = list(zip(scorer_name,scorer_count))
    return(the_count)

def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line
    of decoded text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader.

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


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Challenge 01

    # TODO 01.1-2 (required)
    filepath = 'nwsl-top_scorers-2021.csv'
    scorers_data = read_csv('nwsl-top_scorers-2021.csv')
    top_scorers_seven_goals = scorers_data[6:9]

    # TODO 01.3-4 (required)
    filepath = 'nwsl-standings-2021.csv'
    standings_data = read_csv('nwsl-standings-2021.csv')
    standings_reversed = standings_data[::-1]


    # TODO 01.5-6 (required)
    filepath = 'nwsl-club_info-2021.csv'
    club_info_data = read_csv('nwsl-club_info-2021.csv')
    kc_stadium_name = club_info_data[3][5]


    # Challenge 02

    # TODO 02.1-4 (required)
    standings_headers = standings_data[0]
    standings = standings_data[1:]
    for x in standings:
        x = clean_club(x)
    get_club_record(standings, 'Orlando Pride')


    # Challenge 03
    calculate_points(get_club_record(standings,'Washington Spirit'))
    standings_headers.append('price')
    for x in standings:
        x.append(calculate_points(x))


    # Challenge 04
    clubs_classified = []
    for x in standings:
        clubs_classified.append([x[0],classify_club(x)])
    write_csv('stu-nswl_clubs_classified-2021.csv', clubs_classified, headers = ("club_name","tier"))



    # Challenge 05


    scorer_header = scorers_data[0]
    scorers = scorers_data[1:]
    ol_reign_scorers = get_club_top_scorers(scorers, 'Ol Reign')


    # Challenge 06
    clubs_top_scorers_counts = get_clubs_top_scorers_counts(standings, scorers)
    write_csv('stu-nwsl_clubs_top_scorers_counts.csv', clubs_top_scorers_counts, headers = ("club","top_scorers_count"))

    # Challenge 07
    thorns_record = get_club_record(standings,'Portland Thorns FC')
    thorns_shot_conversion_rate = calculate_shot_conversation_rate(thorns_record, 'shots_on_goal')


    # Challenge 08

    clubs_with_shots = get_clubs_shot_conversion_rates(standings, 'shots_on_goal')
    write_csv('stu-nwsl_shots_on_goal_conversion_rates-2021.csv', clubs_with_shots, headers = ("club","shots_on_goal_conversion_rate"))


    # Challenge 09

    club_goals_top_scorers_pct = []

    for i in standings:
        goals_for, top_scorers_goals, top_scorers_goals_pct = calculate_goals_by_top_scorers_pct(i, scorers)
        club_goals_top_scorers_pct.append([i[0], goals_for,top_scorers_goals, top_scorers_goals_pct])
    write_csv('stu-nwsl_club_goals_top_scorers_pct.csv', club_goals_top_scorers_pct, headers = ("club", "goals_for", "top_scorer_goals", "top_scorer_goals_pct"))


    # Challenge 10
    print(club_info_data)
    club_info = club_info_data[1:]
    print(club_info)
    combined_data = combine_data(top_scorers=scorers, standings=standings, club_info=club_info)
    write_csv('stu-nwsl_combined_data.csv', combined_data, headers = None)
    print(combined_data)


# WARN: Do not delete __name__ value check.
if __name__ == '__main__':
    main()
