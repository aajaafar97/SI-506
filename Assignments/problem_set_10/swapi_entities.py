# Problem 2.0
class Planet:
    """Representation of a planet.
    Attributes:
        url (str): identifier/locator
        name (str): planet name
        rotation_period (int): rotation period
        orbital_period (int): orbital period
        diameter (int): diameter of the planet
        climate (list): climate type(s) found on planet
        gravity (dict): gravity level
        terrain (list): terrain type(s) found on planet
        surface_water (float): surface water
        population (int): population size
    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    # Problem 2.1
    def __init__(self, url, name):
        """Initialize a Planet instance."""
        self.url = url
        self.name = name
        self.rotation_period = None
        self.orbital_period = None
        self.diameter = None
        self.climate = None
        self.gravity = None
        self.terrain = None
        self.surface_water = None
        self.population = None

    # Problem 2.2
    def __str__(self):
        """Return a string representation of the object."""
        return self.name

    # Problem 2.3
    def has_surface_water(self):
        """Return a boolean representation of whether the planet has surface water."""
        if self.surface_water:
            return True
        else:
            return False

    # Problem 2.5
    def is_populated(self):
        """Return a boolean representation of whether the planet has population."""
        if self.population:
            return True
        else:
            return False

    # Problem 2.6
    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use the order specified in the Docstring above.
        Use a dictionary literal rather than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
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
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population
        }

# Problem 3.0
def convert_data(planet):
    """Convert string values of a dictionary to the appropriate type whenever possible.
    Remember to set the value to None when the string is "unknown".

    Type conversions:
        rotation_period (str->int)
        orbital_period (str->int)
        diameter (str->int)
        climate (str->list) e.g. ["hot", "humid"]
        gravity (str->dict) e.g. {"measure": 0.75, "unit"; "standard"}
        terrain (str->list) e.g. ["fungus", "forests"]
        surface_water (str->float)
        population (str->int)

    Parameters:
        dict: dictionary of a planet
    Returns:
        dict: dictionary of a planet with its values converted
    """

    if planet.get('rotation_period'):
        if planet['rotation_period'].lower() == 'unknown':
            planet['rotation_period'] = None
        else:
            planet['rotation_period'] = int(planet['rotation_period'])
    if planet.get('orbital_period'):
        if planet['orbital_period'].lower() == 'unknown':
            planet['orbital_period'] = None
        else:
            planet['orbital_period'] = int(planet['orbital_period'])
    if planet.get('diameter'):
        if planet['diameter'].lower() == 'unknown':
            planet['diameter'] = None
        else:
            planet['diameter'] = int(planet['diameter'])
    if planet.get('climate'):
        if planet['climate'].lower() == 'unknown':
            planet['climate'] = None
        else:
            planet['climate'] = planet['climate'].split(', ')
    if planet.get('gravity'):
        if planet['gravity'].lower() == 'unknown':
            planet['gravity'] = None
        else:
            planet_list = planet['gravity'].split()
            gravity_dict ={}
            gravity_dict['measure'] = float(planet_list[0])
            if len(planet_list) == 2:
                gravity_dict['unit'] = planet_list[1]
            else:
                gravity_dict['unit'] = 'standard'
            planet['gravity'] = gravity_dict
    if planet.get('terrain'):
        if planet['terrain'].lower() == 'unknown':
            planet['terrain'] = None
        else:
            planet['terrain'] = planet['terrain'].split(', ')
    if planet.get('surface_water'):
        if planet['surface_water'].lower() == 'unknown':
            planet['surface_water'] = None
        else:
            planet['surface_water'] = float(planet['surface_water'])
    if planet.get('population'):
        if planet['population'].lower() == 'unknown':
            planet['population'] = None
        else:
            planet['population'] = int(planet['population'])
    return planet


# Problem 4.0
def create_planet(planet):
    """Creates a < Planet > instance from dictionary data. You must call the convert_data() function
    to clean up the planet dictionary first, then assign the dictionary to the instance.

    Parameters:
        planet (dict): planet as a dictionary
    Returns:
        Planet: new < Planet > instance
    """
    converted_planet = convert_data(planet)
    converted_planet_instance = Planet(converted_planet['url'], converted_planet['name'])
    converted_planet_instance.orbital_period = converted_planet['orbital_period']
    converted_planet_instance.population = converted_planet['population']
    converted_planet_instance.surface_water = converted_planet['surface_water']
    converted_planet_instance.terrain = converted_planet['terrain']
    converted_planet_instance.climate = converted_planet['climate']
    converted_planet_instance.diameter = converted_planet['diameter']
    converted_planet_instance.gravity = converted_planet['gravity']
    converted_planet_instance.rotation_period = converted_planet['rotation_period']

    return converted_planet_instance