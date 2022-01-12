import json, requests, copy


# Problem 01
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


# Problem 02
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
            response = requests.get(url, params, timeout=timeout)
    else:
        response = requests.get(url, timeout=timeout)

    return response.json()



# Problem 03
def delete_items(dictionary, key_list):
    dict_copy = copy.deepcopy(dictionary)
    for keys in key_list:
        if keys in dict_copy.keys():
            del(dict_copy)[keys]
    return(dict_copy)


# Problem 04
def get_homeworld(person, key_list = None):
    person_homeworld_link = person['homeworld']
    person_homeworld = get_swapi_resource(person_homeworld_link)
    new_dict = {}
    if key_list is None:
        return(person_homeworld)
    else:
        for key in key_list:
            for keys in person_homeworld.keys():
                if key in keys:
                    new_dict[keys] = person_homeworld[keys]
        return(new_dict)

def get_species(person, key_list = None):
    new_dict = {}
    if person['species']:
        person_species_link = person['species'][0]
        person_species = get_swapi_resource(person_species_link)
        if key_list is None:
            return(person_species)
        else:
            for key in key_list:
                for keys in person_species.keys():
                    if key in keys:
                        new_dict[keys] = person_species[keys]
            return(new_dict)
    else:
        return(new_dict)


# Problem 05
def clean_person_dictionary(person, delete_list, home_list = None, species_list = None):
    dict_copy = copy.deepcopy(person)
    a = delete_items(dict_copy, delete_list)
    a['homeworld'] = get_homeworld(a, home_list)
    a['species'] = get_species(a, species_list)
    return(a)




# Problem 06
def board_ship(ship, passengers):
    passengers_list = []
    ship_copy = copy.deepcopy(ship)
    for x in range(1,7):
        for a in passengers:
            if a['boarding_order'] == x:
                passengers_list.append(a)
    ship_copy['passengers'] = passengers_list
    return(ship_copy)




    ordered_board = []

# Problem 07
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

def main():
    """Program entry point."""

    # Problem 01
    passengers = read_json('passengers.json')


    #print(f'\nProblem 01:\n{passengers}')

    # Problem 02
    base_url = 'https://swapi.py4e.com/api/'
    falcon_params = {'search': 'falcon'}
    falcon = get_swapi_resource(base_url + '/starships', falcon_params)['results'][0]
    #print(f'\nProblem 02:\n{falcon}')

    # Problem 03
    falcon_updated = delete_items(falcon, list(falcon.keys())[-5:])
    #print(falcon_updated)

    # Problem 04
    bail_params = {'search': 'bail'}
    bail = get_swapi_resource(base_url + '/people', bail_params)['results'][0]
    bail_home = get_homeworld(bail)
    bail_species = get_species(bail)
    #print(bail)
    #print(bail_home)
    #print(bail_species)


    # Problem 05
    home_keys_keep = ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population']
    species_keys_keep = ['name']
    new_passengers = []
    for i in passengers.values():
        for a in i:
            passengers_params = {'search': a['name']}
            b = get_swapi_resource(base_url + '/people', passengers_params)['results'][0]
            c = clean_person_dictionary(b, ['films', 'vehicles', 'starships', 'created', 'edited', 'url'], home_keys_keep, species_keys_keep)
            a.update(c)
            new_passengers.append(a)
    #print(new_passengers)



    # Problem 06
    all_aboard = board_ship(falcon_updated, new_passengers)
    # Problem 07
    leaving_tatooine = 'hyperspace_jump.json'
    write_json(data=all_aboard, filepath=leaving_tatooine)



if __name__ == '__main__':
    main()
