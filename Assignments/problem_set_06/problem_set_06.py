import csv
import copy

#Problem 01
def read_csv(filepath, encoding='utf-8'):
    """
    This function reads in a csv and returns its contents as a list

    Parameters:
        filepath (str): A str representing the filepath for the file to be read
        encoding (str): A str representing the character encoding of the file

    Returns:
        (list): A list with the content of the file
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        data = []
        reader = csv.reader(file_obj)
        for row in reader:
            data.append(row)
        return data

#Problem 02
def add_ratings(shows, ratings):
    """
    This function makes a copy of a show list and adds the shows IMDb rating to it

    Parameters:
        shows (list): A list of shows
        ratings (list): A list of IMDb ratings for the shows

    Returns:
        (list): A list of shows with the ratings added
    """
    show_copy = copy.deepcopy(shows)
    show_copy[0].append('IMDb Rating')
    for show in show_copy[1:]:
        for rating in ratings[1:]:
            if show[0].lower() == rating[0].lower():
                show.append(rating[1])
    return show_copy


#Problem 03
def clean_show_data(shows):
    """
    This function cleans the data of a list of shows

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): The list of shows with clean data
    """
    shows_copy = copy.deepcopy(shows)
    for show in shows_copy[1:]:
        show[3] = float(show[3])
        show[1] = show[1].split('/')
        show[2] = show[2].split('/')
    return shows_copy

#Problem 04
def get_highest_rated_show(shows):
    highest_show_rank = 0
    show_name = None
    show_creators = None
    for show in shows[1:]:
        if show[3] > highest_show_rank:
            highest_show_rank = show[3]
            show_name = show[0]
            show_creators = show[1]
    highest_ranked_show = (show_name, show_creators)
    return highest_ranked_show



#Problem 05
def filter_by_genre(shows,genre):
    filtered_shows = []
    for show in shows[1:]:
        for genres in show[2]:
            if genre.lower() in genres.lower():
             filtered_shows.append(show)
    return filtered_shows



#Problem 06
def stringify(shows):
    shows_copy = copy.deepcopy(shows)
    for show in shows_copy[1:]:
        show[2] = '/'.join(show[2])
        show[1] = '/'.join(show[1])
    return shows_copy


#Problem 07
def write_csv(filepath, data):
    with open(filepath, 'w', newline='', encoding = 'utf-8') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(data)
        return data
#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """
    #Problem 01
    netflix_data = read_csv('netflix_data.csv')
    disney_data = read_csv('disney_data.csv')
    netflix_ratings = read_csv('netflix_ratings.csv')
    disney_ratings = read_csv('disney_ratings.csv')

    #Problem 02
    netflix_data_with_ratings = add_ratings(netflix_data, netflix_ratings) 
    disney_data_with_ratings = add_ratings(disney_data, disney_ratings)
   
    #Problem 03
    clean_netflix_data = clean_show_data(netflix_data_with_ratings)
    clean_disney_data = clean_show_data(disney_data_with_ratings)
    #print(clean_netflix_data)

    #Problem 04
    best_netflix_show = get_highest_rated_show(clean_netflix_data)
    best_disney_show = get_highest_rated_show(clean_disney_data)

    #Problem 05
    sci_fi_shows = [['Title', 'Creator(s)', 'Genre(s)', 'IMDb Rating']]
    disney_filter = filter_by_genre(clean_disney_data, 'Science Fiction')
    netflix_filter = filter_by_genre(clean_netflix_data ,'Science fiction')
    sci_fi_shows.extend(netflix_filter)
    sci_fi_shows.extend(disney_filter)
    #print(sci_fi_shows)
    #Problem 06
    stringified_sci_fi_shows = stringify(sci_fi_shows)
    print(stringified_sci_fi_shows)
    #Problem 07
    write_csv('sci_fi_shows.csv', stringified_sci_fi_shows)
    # WARN: if variables in the tuple below are not yet defined, initialize them to zero (0)
    return (netflix_data, disney_data, netflix_ratings, disney_ratings, netflix_data_with_ratings,
    disney_data_with_ratings, clean_netflix_data, clean_disney_data, best_netflix_show, best_disney_show,
    )

#Do not delete
if __name__ == '__main__':
    main()
