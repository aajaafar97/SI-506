import json
from os import write

from requests import NullHandler
import swapi_entities as ent

# Problem 1.0
def read_json(filepath, encoding='utf-8'):
    """
    Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.
    Parameters:
        filepath (string): path to file
        encoding (string): optional name of encoding used to decode the file. The default is 'utf-8'.
    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open (filepath , 'r', encoding = 'utf-8') as file_obj:
        return json.load(file_obj)


# Problem 1.0
def write_json(filepath, data):
    """
    This function dumps the JSON object in the dictionary `data` into a file on
    `filepath`.
    Parameters:
        filepath (string): The location and filename of the file to store the JSON
        data (dict): The dictionary that contains the JSON representation of the objects.
    Returns:
        None
    """
    with open(filepath, 'w') as file_obj:
        json.dump(data, file_obj)


def main():
    # Problem 1.0
    planet_data = read_json('swapi_planets.json')

    # Problem 2.0 - Problem 4.0

    # Complete in problem_set_10_utils.py

    # Problem 5.2
    global planets
    planets = {}
    for data in planet_data:
        planets[data['name']] = ent.create_planet(data)

    # Problem 6.0
    planets_with_surface_water = []
    for key, value in planets.items():
        if value.has_surface_water() == None:
            continue
        elif value.has_surface_water() == True:
            planets_with_surface_water.append(value.jsonable())
    write_json('stu_planets_with_surface_water.json', planets_with_surface_water)

    planets_inhabited = []
    planets_uninhabited = []
    for key, value in planets.items():
        if value.population == None:
            continue
        elif value.is_populated() == True:
            planets_inhabited.append(value.jsonable())
        elif value.is_populated() == False:
            planets_uninhabited.append(value.jsonable())


    write_json('stu_planets_inhabited.json', planets_inhabited)
    write_json('stu_planets_uninhabited.json', planets_uninhabited)

    planets_desert_only = []
    for key, value in planets.items():
        if value.terrain == None:
            continue
        if len(value.terrain) > 1:
            continue
        elif 'desert' in value.terrain :
            planets_desert_only.append(value.jsonable())

    write_json('stu_planets_desert_only.json', planets_desert_only)

    planets_biggest_smallest = {"biggest": [], "smallest": []}

    Max = 0
    for key, value in planets.items():
        if value.diameter == None:
            continue
        if value.diameter == 0:
            planets_biggest_smallest['smallest'].append(value.jsonable())
        if value.diameter > Max:
            planets_biggest_smallest['biggest'].clear()
            Max = value.diameter
            planets_biggest_smallest['biggest'].append(value.jsonable())
    print((planets_biggest_smallest['smallest']))
    print((planets_biggest_smallest['biggest']))
    write_json('stu_planets_biggest_smallest.json', planets_biggest_smallest )
if __name__ == '__main__':
    main()
