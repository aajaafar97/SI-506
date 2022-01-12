import json
import requests
import swapi_utils as utl

# LAB EXERCISE 10

# SETUP CODE


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.
    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        max_atmosphering_speed (int): max sub-orbital speed
        consumables (str): max period in months before on-board provisions must be replenished
        hyperdrive_rating (float): lightspeed propulsion system rating

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.max_atmosphering_speed = None
        self.consumables = None
        self.hyperdrive_rating = None

    def __str__(self):
        """String representation of the object."""

        return self.model # not name (which is usually too generic)

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'consumables': self.consumables,
            'hyperdrive_rating': self.hyperdrive_rating,
        }

# END SETUP

# PROBLEM 02 (9 Points)

def create_starship(data):
    """Creates a < Starship > instance from dictionary data, converting string values to the
    appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.
    Type conversions:
        max_atmosphering_speed (str->int)
        consumables (str->dict)
        hyperdrive_rating (str->float)
    Parameters:
        data (dict): source data
    Returns:
        starship: a new < Starship > instance
    """

    starship = Starship(data['url'], data['name'], data['model'], data['starship_class'])
    #check if this value exists in the dictionary
    if data.get('max_atmosphering_speed'):
        #check if value for max_atmosphering_speed is n/a
        if data['max_atmosphering_speed'].lower() == 'n/a':
            data['max_atmosphering_speed'] = None
        #check if value for max_atmosphering_speed has km
        elif 'km' in data['max_atmosphering_speed']:
            new_data = data['max_atmosphering_speed'].replace('km', '')
            data['max_atmosphering_speed'] = int(new_data)
        else:
            data['max_atmosphering_speed'] = int(data['max_atmosphering_speed'])
        starship.max_atmosphering_speed = data['max_atmosphering_speed']

    #Check if consumbales exists
    if data.get('consumables'):
        if data['consumables'][-1] == 's':
            data['consumables'] = data['consumables'].replace('s', '')
        consumable_list = data['consumables'].split()
        consumables_dict ={}
        consumables_dict['interval'] = consumable_list[1]
        consumables_dict['value'] = int(consumable_list[0])
        starship.consumables = consumables_dict

    #check if hyperdrive rating exists in dictioanry
    if data.get('hyperdrive_rating'):
        starship.hyperdrive_rating = float(data['hyperdrive_rating'])

    #return starship
    return starship

# END PROBLEM 02



def main():
    """ This function calls <get_swapi_resource> function to retrieve SWAPI starships data.
    Create starship instances and clean these SWAPI starships data.
    Then it calls <write_json> function to store data to a json file.

    Parameters:
        None

    Return:
        None
    """

    # PROBLEM 01 (9 Points)
    starships_data = utl.get_swapi_resource(utl.ENDPOINT + '/starships/')['results'][:10]


    # END PROBLEM 01


    # PROBLEM 03 (5 Points)
    starships = []
    for data in starships_data:
        starships.append(create_starship(data))

    # END PROBLEM 03


    # PROBLEM 04 (2 Points)
    writable = []
    for data in starships:
        writable.append(data.jsonable())

    utl.write_json('starships.json', writable)
    # END PROBLEM 04


if __name__ == '__main__':
    main()
