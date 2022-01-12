# SI 506 Problem Set 05

import csv
import copy

print("Problem 01\n\n")

# Problem 01: Implement read_csv and load the election data.

def read_csv(filepath, delimiter=','):
     with open(filepath, 'r', newline='', encoding='utf-8-sig') as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter = delimiter)
        for row in reader:
            data.append(row)
        return data


print("\n\nProblem 02\n\n")

raw_election_data_2021 = read_csv('election_data_2021.csv')
raw_election_data_2017 = read_csv('election_data_2017.csv')

print(raw_election_data_2021)

# Problem 02: Implement clean and clean the election data.

def clean(data):
    data_1 = copy.deepcopy(data)
    for item in data_1[1:]:
        item[1] = int(item[1])
        item[2] = item[2].lower()
        item[0] = item[0].strip()
        item[2] = item[2].strip()
    return data_1

clean_election_data_2021 = clean(raw_election_data_2021)
clean_election_data_2017 = clean(raw_election_data_2017)
print(clean_election_data_2021)

print("\n\nProblem 03\n\n")


# Problem 03: Implement get_party_seat_differences and get the party seat differences for the 2021 election.


def get_seat_differences(current_election, previous_election):
    party_diff = []
    for i in current_election[1:]:
        for a in previous_election[1:]:
            if a[0] == i[0]:
                party_diff.append((i[0],i[1] - a[1]))
    return party_diff

party_seat_differences = get_seat_differences(clean_election_data_2021,clean_election_data_2017)

print(party_seat_differences)
print("\n\nProblem 04\n\n")


# Problem 04: Implement get_leaders and get the leaders for the 2021 election data.
party_leaders_2021 = [
                        ('AfD', 'Joerg Meuthen and Tino Chrupalla'),
                        ('FDP', 'Christian Lindner'),
                        ('CDU/CSU', 'Armin Laschet'),
                        ('SPD', 'Olaf Scholz'),
                        ('Greens', 'Annalena Baerbock and Robert Habeck'),
                        ('Left', 'Janine Wissler and Susanne Hennig-Wellsow')
                    ]

def get_leaders(election_data, party_leaders):
    data_1 = copy.deepcopy(election_data)
    data_1[0].append('Party Leader(s)')
    for i in data_1[1:]:
     for party_tuple in party_leaders:
         party = party_tuple[0]
         canidate = party_tuple[1]
         if party == i[0]:
             i.append(canidate)
    return(data_1)




election_data_2021_with_leaders = get_leaders(clean_election_data_2021,party_leaders_2021)

print(election_data_2021_with_leaders)

print("\n\nProblem 05\n\n")

# Problem 05: Implement get_affiliation_percents and get affiliation percents for the 2021 election data.


def get_seats_percent(election_data):
    total_seats = 0
    left_seats = 0
    right_seats = 0
    center_seats = 0
    extreme_seats = 0
    for i in election_data[1:]:
        total_seats = total_seats + i[1]
        if 'left' in i[2]:
            left_seats = left_seats + i[1]
        elif 'right' in i[2]:
            right_seats = right_seats + i[1]
        if 'far' not in i[2]:
            center_seats = center_seats + i[1]
        if 'far' in i[2]:
            extreme_seats = extreme_seats + i[1]    
    percent_left_seats = round(left_seats/total_seats * 100,2)
    percent_right_seats = round(right_seats/total_seats * 100,2)
    percent_center_seats = round(center_seats/total_seats * 100,2)
    percent_extreme_seats = round(extreme_seats/total_seats * 100,2)
    seats_tuple = (percent_left_seats, percent_right_seats, percent_extreme_seats, percent_center_seats)
    print(seats_tuple)
    return  seats_tuple

get_seats_percent(election_data_2021_with_leaders)

print(get_seats_percent)

print("\n\nProblem 06\n\n")


# Problem 06: Implement write_csv and write election_data_2021_with_leaders to a file called revised_election_data_2021.csv.

def write_csv(filepath, data):
    with open(filepath, 'w', newline='', encoding = 'utf-8-sig') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(data)
        return data

write_csv('revised_election_data_2021.csv',election_data_2021_with_leaders)