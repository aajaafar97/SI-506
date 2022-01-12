# LAB EXERCISE 07
print('Lab Exercise 07 \n')

# SETUP
restaurants = [
    {'Name': 'Frita Batidos', 'Location': '117 W Washington St', 'Rating': 4.5, 'Reviews': 1871, 'Category': 'Burgers'},
    {'Name': "Zingerman's Delicatessen", 'Location': '422 Detroit St', 'Rating': 4.0, 'Reviews': 2224, 'Category': 'Delis'},
    {'Name': "Scorekeepers", 'Location': '310 Maynard St', 'Rating': 2.5, 'Reviews': 59, 'Category': 'Burgers'},
    {'Name': 'Rich Jc Korean Restaurant', 'Location': '1313 S University Ave', 'Rating': 4.0, 'Reviews': 183, 'Category': 'Korean'},
    {'Name': 'Tomukun Noodle Bar', 'Location': '505 E Liberty St Ste 200', 'Rating': 4.0, 'Reviews': 773, 'Category': 'Noodles'},
    {'Name': "Sava's", 'Location': '216 S State St', 'Rating': 4.0, 'Reviews': 1195, 'Category': 'American'},
    {'Name': "Krazy Jim's Blimpy Burger", 'Location': '304 S Ashley St', 'Rating': 3.5, 'Reviews': 231, 'Category': 'Burgers'},
    {'Name': "Joe's Pizza", 'Location': '1107 S University Ave', 'Rating': 4.5, 'Reviews': 107, 'Category': 'Pizza'},
    {'Name': 'Hola Seoul', 'Location': '715 N University Ave', 'Rating': 4.0, 'Reviews': 98, 'Category': 'Korean'},
    {'Name': 'The Chop House', 'Location': '322 S Main St', 'Rating': 4.0, 'Reviews': 448, 'Category': 'Steakhouses'},
    {'Name': 'TK Wu', 'Location': '510 E Liberty St', 'Rating': 3.5, 'Reviews': 236, 'Category': 'Chinese'},
    {'Name': 'HopCat', 'Location': '311 Maynard St', 'Rating': 3.5, 'Reviews': 397, 'Category': 'Burgers'},
    {'Name': 'Lan City Noodle Bar', 'Location': '1235 S University Ave', 'Rating': 4.0, 'Reviews': 5, 'Category': 'Chinese'},
    {'Name': 'First Bite', 'Location': '108 S Main St', 'Rating': 5.0, 'Reviews': 104, 'Category': 'Burgers'}
]

# END SETUP

# Problem 01 (3 points)
def get_restaurants(restaurants, category=None):
    """
    This function takes a list of dictionaries as an argument and returns a list of strings that includes restaurants' names

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant
        category (list): A list of strings containing different categories of restaurants

    Returns:
        restaurants_names (list): A list containing the restaurants' names
    """
    names = []
    for restaurant in restaurants:
        if category:
            if restaurant['Category'] in category:
                names.append(restaurant['Name'])
        else:
            names.append(restaurant['Name'])
    return names

# Problem 02 (4 points)
def get_most_reviewed_restaurant(restaurants):
    """
    This function takes a list of dictionaries as an argument and returns a dictionary with the restaurant's name as value to the key 'Name' and the number of reviews as value to the key 'Reviews'

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant

    Returns:
        most_reviewed_restaurant (dict): A dictionary containing the restaurant's name and the number of reviews
    """
    most_reviewed_restaurant = {}
    most_reviews = 0
    for restaurant in restaurants:
        if restaurant['Reviews'] > most_reviews:
            most_reviews = restaurant['Reviews']
            most_reviewed_restaurant['Name'] = restaurant['Name']
            most_reviewed_restaurant['Reviews'] = restaurant['Reviews']
    return most_reviewed_restaurant




# Problem 03 (4 points)
def get_high_rating_restaurants(restaurants, category):
    high_rated_restaurants = {}
    for restaurant in restaurants:
        if restaurant['Category'] in category and restaurant['Rating'] >= 3.5:
            high_rated_restaurants[restaurant['Name']] = restaurant['Rating']
    return high_rated_restaurants

# Problem 04 (4 points)
def get_avg_rating(high_rating_restaurants):
    ratings_total = 0
    for rating in high_rating_restaurants.values():
        ratings_total += rating
    return ratings_total / len(high_rating_restaurants.values())


# Problem 05 (5 points)
def write_txt(filepath, data):
    with open(filepath, 'w', encoding = 'utf-8') as file_obj:
        for item in data:
            item = list(item.items())
            file_obj.write(f'{item[:3]}\n')


# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01
    print("Problem 01:\n")
    korean_restaurants = get_restaurants(restaurants, ['Korean'])
    print(korean_restaurants)

    # Problem 02
    print("Problem 02:\n")
    most_reviewed_restaurant = get_most_reviewed_restaurant(restaurants)
    print(most_reviewed_restaurant)

    # Problem 03
    categories = ['Burgers', 'Chinese']
    high_rating_restaurants = get_high_rating_restaurants(restaurants, categories)
    print(high_rating_restaurants)

    # Problem 04
    avg_rating = get_avg_rating(high_rating_restaurants)
    print(avg_rating)

    # Problem 05
    write_txt('restaurants_info.txt', restaurants)

if __name__ == "__main__":
    main()