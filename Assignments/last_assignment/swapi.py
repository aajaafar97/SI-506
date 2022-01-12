import sw_utils as utl
from sw_utils import read_csv, read_csv_to_dicts


class Crew:
    """Represents a Starship or Vehicle crew.

    Attributes:
        Accepts a dictionary of Person and/or Droid crew members and assigns each key-value pair
        to the new `Crew` instance's `__dict__` dictionary of writable attributes.

        < role > (Person | Droid): Person or Droid instance identified by crew role (e.g., pilot)

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, crew_members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to create each instance variable and assign the value. The
        dictionary key (e.g., "pilot") serves as the instance variable name to which the
        accompanying < Person | Droid > instance is assigned as the value, e.g.,
        {< role >: < Person | Droid >, ...}

        Parameters:
            crew_members (dict): crew members dictionary

        Returns:
            None
        """

        for key, val in crew_members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person | Droid > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over a < Crew > instance's
        __dict__ items and assigns new key-value pairs to an empty dictionary using the existing
        key as the new key and a dictionary representation of the < Person > or < Droid > instance
        as the value. After the loop terminates the new dictionary is returned to the caller.
        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying
        and/or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person or droid object

        return crew


class Droid:
    """Represents a mechanical being that possesses artificial intelligence.

    Attributes:
       Required
            url (str): identifier/locator (required)
            name (str): droid name (required)
            model (str): droid model (required)
        Optional
            manufacturer (str): creator
            create_year (str): year of manufacture
            height_m (float): height in meters
            mass_kg (float): mass in kilograms
            equipment (list): equipment carried, if any

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model):
        """Initialize a Droid instance."""

        self.url = url
        self.name = name
        self.model = model
        self.manufacturer = None
        self.create_year = None
        self.height_m = None
        self.mass_kg = None
        self.equipment = None

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            model
            manufacturer
            create_year
            height_m
            mass_kg
            equipment
        """

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'create_year': self.create_year,
            'height_m': self.height_m,
            'mass_kg': self.mass_kg,
            'equipment': self.equipment
        }


class Passengers:
    """Represents passengers carried on a Starship or Vehicle.

    Attributes:
        Accepts a list of < Person > and/or < Droid > objects that are added as key-value pairs
        to the new Passengers instance's `__dict__` dictionary of writable attributes. The
        < Person > or < Droid > "name" value serves as the key and the instance itself as the
        value. Each key-value pair added to __dict__ represents a new instance variable and value.

        < "name" > (Person | Droid): Person or Droid instance identified by name

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid > instances and calls the built-in function < setattr() > to create the instance
        variable and assign the value. The < Droid > or < Person > instance's "name" value serves
        as the new instance variable name (see format below) while the < Person > or < Droid >
        instance is assigned as the value.

        Instance variable name formatting rules:
            1. Change name to lowercase
            2. Replace space (' ') with underscore ('_')
            3. Replace dash ('-') with underscore ('_')

            "Luke Skywalker" -> "luke_skywalker"
            self.luke_skywalker = < Person >

            "C-3PO" -> "c_3po"
            self.c_3po = < Droid >

        Parameters:
            passengers (list): list of < Person > and/or < Droid > objects

        Returns:
            None
        """

        for data in passengers:
            setattr(self, data.name, data.jsonable()) # call built-in function

    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > or < Droid > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}" # additional member
            else:
                passengers = f"Passengers: {val.name}" # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over the < Passengers >
        instance's __dict__ values and converts each < Person > or < Droid > object encountered
        to a dictionary. Accumulates dictionaries in a < list >.  After the loop terminates the
        new list is returned to the caller. Do not simply return self.__dict__. It can be
        intercepted and mutated, adding, modifying and/or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            list: nested person or droid dictionaries
        """

        passengers = []
        for val in self.__dict__.items():
            passengers = val.jsonable() # person or droid object

        return passengers


class Person:
    """Represents a person.

    Attributes:
        url (str): identifer/locator
        name (str): person name
        birth_year (str): person's birth_year
        height_m (float): person's height in centimeters
        mass_kg (float): person's weight in kilograms
        homeworld (Planet): person's home planet
        force_sensitive (bool): ability to harness the power of the Force.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, force_sensitive=False):
        """Initialize a Person instance."""
        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.height_m = None
        self.mass_kg = None
        self.homeworld = None
        self.force_sensitive = force_sensitive

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes
        as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
           url
           name
           birth_year
           height_m
           mass_kg
           homeworld
           force_sensitive
        """

        return {
            'url': self.url,
            'name': self.name,
            'birth_year': self.birth_year,
            'height_m': self.height_m,
            'mass_kg': self.mass_kg,
            'homeworld': self.homeworld,
            'force_sensitive': self.force_sensitive
        }



class Planet:
    """Represents a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in
                                     standard days
        diameter_km (int): diameter of planet measured in kilometers
        gravity_std (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        """Initialize a Planet instance."""
        self.url = url
        self.name = name
        self.region = None
        self. sector = None
        self.suns = None
        self.moons = None
        self.orbital_period_days = None
        self. diameter_km = None
        self.gravity_std = None
        self.climate = None
        self.terrain = None
        self.population = None

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes
        as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            region
            sector
            suns
            moons
            orbital_period_days
            diameter_km
            gravity_std
            climate
            terrain
            population
        """

        return {
            'url': self.url,
            'name': self.name,
            'region': self.region,
            'sector': self. sector,
            'suns': self.suns,
            'moons': self.moons,
            'orbital_period_days': self.orbital_period_days,
            'diameter_km': self. diameter_km,
            'gravity_std': self.gravity_std,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
        }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length_m (float): starship length in meters
        max_atmosphering_speed (int): maximum sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew_members (Crew): Crew instance assigned to starship
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity_kg (float): cargo capacity in kilograms that the starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished

    Methods:
        assign_crew_members: assign < Crew > instance to starship
        add_passengers: assign < Passengers > instance to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = None
        self.length_m = None
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None
        self.armament = None
        self.crew_members = None
        self.passengers_on_board = None
        self.cargo_capacity_kg = None
        self.consumables = None


    def __str__(self):
        """String representation of the object."""

        return self.model # not name (which is usually too generic)

    def add_passengers(self, passengers):
        """Assigns passengers to the instance variable < self.passengers_on_board > if passenger
        accommodations on the starship are available. Confirms that the passed in < passengers >
        argument is an instance of the < Passengers > class. If not a < Passengers > instance the
        < self.passengers_on_board > variable assignment is NOT performed.

        Parameters:
            passengers (Passengers): object containing < Person | Droid > instances

        Returns:
            None
        """

        if isinstance(passengers, Passengers):
            self.passengers_on_board = passengers
        else:
            self.passengers_on_board = None

    def assign_crew_members(self, crew):
        """Assigns crew members to the instance variable < self.crew_members > if the crew size
        can be accommodated. Confirms that the passed in < crew > argument is an instance of
        the < Crew > class. If not a < Crew > instance the < self.crew_members > variable assignment
        is NOT performed.

        Parameters:
            crew (Crew): object comprising crew members ('< role >': < Person> / < Droid >)

        Returns:
            None
        """

        if isinstance(crew, Crew):
            self.crew_members = crew
        else:
            self.crew_members = None



    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            model
            starship_class
            manufacturer
            length_m
            max_atmosphering_speed
            hyperdrive_rating
            MGLT
            armament
            crew_members
            passengers_on_board
            cargo_capacity_kg
            consumables
        """
        if self.crew_members:
            crew_members = self.crew_members.jsonable()
        else:
            crew_members = None
        if self.passengers_on_board:
            passengers_on_board = self.passengers_on_board.jsonable()
        else:
            passengers_on_board = None
        return{
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'length_m': self.length_m,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'armament': self.armament,
            'crew_members': crew_members,
            'passengers_on_board': passengers_on_board,
            'cargo_capacity_kg': self.cargo_capacity_kg,
            'consumables': self.consumables
        }


def convert_episode_values(episodes):
    """Converts select string values to either int, float, list, or None in the passed in list of
    nested dictionaries. The function delegates to the `convert_to_*` functions located in the
    module `swapi_utils` the task of converting the specified strings to either int, float, or
    list. Converting empty or blank values to None is handled locally.

    Conversions:
        str to None: all blank or empty values
        str to int: 'series_season_num', 'series_episode_num', 'season_episode_num'
        str to float: 'episode_prod_code', 'episode_us_viewers_mm'
        str to list: 'episode_writers'

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """

    for episode in episodes:
        for key in episode:
            if not episode[key]:
                episode[key] = None
            if episode['series_season_num']:
                episode['series_season_num'] = utl.convert_to_int(episode['series_season_num'])
            if episode['series_episode_num']:
                episode['series_episode_num'] = utl.convert_to_int(episode['series_episode_num'])
            if episode['season_episode_num']:
                episode['season_episode_num'] = utl.convert_to_int(episode['season_episode_num'])
            if episode['episode_prod_code']:
                episode['episode_prod_code'] = utl.convert_to_float(episode['episode_prod_code'])
            if episode['episode_us_viewers_mm']:
                episode['episode_us_viewers_mm'] = utl.convert_to_float(episode['episode_us_viewers_mm'])
            if episode['episode_writers']:
                episode['episode_writers'] = utl.convert_to_list(episode['episode_writers'],', ')
    return episodes




def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with a
    count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director name >: < episode count >,
            < director name >: < episode count >,
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """
    name_accum = []
    count_accum = []
    Bullock = 0
    Filoni = 0
    Connell = 0
    Ridge = 0
    Coleman = 0
    Yeh = 0
    Takeuchi = 0
    Lee = 0
    Volpe = 0
    Dalva = 0
    Dunlevy = 0
    for episode in episodes:
        for key in episode:
            if episode['episode_director'] in name_accum:
                continue
            else:
                name_accum.append(episode['episode_director'])
    for episode in episodes:
        if 'Dave Bullock' in episode['episode_director']:
            Bullock = Bullock + 1
        elif 'Dave Filoni' in episode['episode_director']:
            Filoni = Filoni + 1
        elif "Brian Kalin O'Connell" in episode['episode_director']:
            Connell = Connell + 1
        elif "Justin Ridge" in episode['episode_director']:
            Ridge = Ridge + 1
        elif 'Rob Coleman' in episode['episode_director']:
            Coleman = Coleman + 1
        elif 'Jesse Yeh' in episode['episode_director']:
            Yeh = Yeh + 1
        elif 'Atsushi Takeuchi' in episode['episode_director']:
            Takeuchi = Takeuchi + 1
        elif 'Steward Lee' in episode['episode_director']:
            Lee = Lee + 1
        elif 'Giancarlo Volpe' in episode['episode_director']:
            Volpe = Volpe + 1
        elif 'Robert Dalva' in episode['episode_director']:
            Dalva = Dalva + 1
        elif 'Kyle Dunlevy' in episode['episode_director']:
            Dunlevy = Dunlevy +1
    count_accum.append(Bullock)
    count_accum.append(Filoni)
    count_accum.append(Connell)
    count_accum.append(Ridge)
    count_accum.append(Coleman)
    count_accum.append(Yeh)
    count_accum.append(Takeuchi)
    count_accum.append(Lee)
    count_accum.append(Volpe)
    count_accum.append(Dalva)
    count_accum.append(Dunlevy)
    director_dict = dict(zip(name_accum,count_accum))
    return(director_dict)




def create_droid(data):
    """Creates a < Droid > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible. Adding special instructions constitutes a seperate
    operation.

    Type conversions:
        height -> height_m (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Parameters:
        data (dict): source data

    Returns:
        Droid: new < Droid > instance
    """
    for a in data:
        utl.convert_to_none(a)
    new_instance = Droid(data, data['name'], data['model'])
    new_instance.manufacturer = data['manufacturer']
    new_instance.create_year = data['create_year']
    new_instance.height_m = utl.convert_to_float(data['height'])
    new_instance.mass_kg = utl.convert_to_float(data['mass'])
    new_instance.equipment = utl.convert_to_list(data['equipment'],'|')
    new_instance.url = data['url']
    return new_instance

def create_person(data, planets=None):
    """Creates a < Person > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible. Calls < utl.get_swapi_resource() > to retrieve homeworld
    data. Adds additional planet information to the homeworld data dictionary if an optional
    < planets > dictionary is passed in as a second argument. Calls < create_planet() > to add
    a < Planet > object to the person instance before returning the new instance to the caller.

    Type conversions:
        height -> height_m (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to Planet)

    Parameters:
        data (dict): source data
        planets (list): optional supplemental planetary data

    Returns:
        Person: new < Person > instance
    """
    base_url = 'https://swapi.py4e.com/api/'
    planet_params = {'search': data['homeworld'].lower()}
    planet_data = utl.get_swapi_resource(base_url + '/planets', planet_params)['results'][0]
    for dict in planets:
        if dict['name'].lower() == data['homeworld'].lower():
            planet_data.update(dict)
    for a in data:
        utl.convert_to_none(a)
    new_instance = Person(data['url'], data['name'], data['birth_year'], data['force_sensitive'])
    new_instance.height_m = utl.convert_to_float(data['height'])
    new_instance.mass_kg = utl.convert_to_float(data['mass'])
    new_instance.homeworld = create_planet(planet_data).jsonable()
    return new_instance


def create_planet(data):
    """Creates a < Planet > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible.

    Type conversions:
        suns -> suns (str->int)
        moon -> moons (str->int)
        orbital_period_days -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Parameters:
        data (dict): source data

    Returns:
        Planet: new < Planet > instance
    """

    new_instance = Planet(data, data['name'])

    new_instance.suns = utl.convert_to_none(data['suns'])
    if new_instance.suns is not None:
        new_instance.suns = utl.convert_to_int(data['suns'])

    new_instance.moons = utl.convert_to_none(data['moons'])
    if new_instance.moons is not None:
        new_instance.moons = utl.convert_to_int(data['moons'])

    new_instance.orbital_period_days = utl.convert_to_none(data['orbital_period'])
    if new_instance.orbital_period_days is not None:
        new_instance.orbital_period_days = utl.convert_to_float(data['orbital_period'])

    new_instance.diameter_km = utl.convert_to_none(data['diameter'])
    if new_instance.diameter_km is not None:
        new_instance.diameter_km = utl.convert_to_int(data['diameter'])

    new_instance.gravity_std = utl.convert_to_none(data['gravity'])
    if new_instance.gravity_std is not None:
        new_instance.gravity_std = utl.convert_gravity_value(data['gravity'])

    new_instance.climate = utl.convert_to_none(data['climate'])
    if new_instance.climate is not None:
        new_instance.climate = utl.convert_to_list(data['climate'],', ')

    new_instance.terrain = utl.convert_to_none(data['terrain'])
    if new_instance.terrain is not None:
        new_instance.terrain = utl.convert_to_list(data['terrain'],', ')

    new_instance.population = utl.convert_to_none(data['population'])
    if new_instance.population is not None:
        new_instance.population = utl.convert_to_int(data['population'])

    new_instance.region = utl.convert_to_none(data['region'])
    if new_instance.region is not None:
        new_instance.region = data['region']

    new_instance.sector = utl.convert_to_none(data['sector'])
    if new_instance.sector is not None:
        new_instance.sector = data['sector']

    new_instance.url = utl.convert_to_none(data['url'])
    if new_instance.url is not None:
        new_instance.url = data['url']


    return new_instance


def create_starship(data):
    """Creates a < Starship > instance from dictionary data, converting optional string values to
    the appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to float)

    Parameters:
        data (dict): source data

    Returns:
        starship: a new < Starship > instance
    """

    for a in data:
        utl.convert_to_none(a)
    new_instance = Starship(data['url'], data['name'], data['model'], data['starship_class'])
    new_instance.manufacturer = data['manufacturer']
    new_instance.length_m = utl.convert_to_float(data['length'])
    new_instance.max_atmosphering_speed = utl.convert_to_int(data['max_atmosphering_speed'])
    new_instance.hyperdrive_rating = utl.convert_to_float(data['hyperdrive_rating'])

    new_instance.MGLT = utl.convert_to_none(data['MGLT'])
    if new_instance.MGLT is not None:
        new_instance.MGLT = utl.convert_to_int(data['MGLT'])

    new_instance.armament = utl.convert_to_list(data['armament'],',')
    new_instance.cargo_capacity_kg = utl.convert_to_int(data['cargo_capacity'])
    new_instance.consumables = data['consumables']

    return new_instance


def get_least_viewed_episode(episodes):
    """Identifies and returns episode with the lowest recorded viewership. Ignores episodes with
    no viewship value. Ignores ties. Delegates to the function < has_viewer_data > the task of
    determing if the episode includes viewership "episode_us_viewers_mm" data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: episode with the lowest recorded viewership.
    """

    mini = []
    i = 5.0
    for episode in episodes:
        if has_viewer_data(episode):
            if episode['episode_us_viewers_mm'] < i:
                mini.clear()
                i = episode['episode_us_viewers_mm']
                mini.append(episode)
    return mini[0]

def get_most_viewed_episode(episodes):
    """Identifies and returns the episode with the highest recorded viewership. Ignores episodes
    with no viewship value. Ignores ties. Delegates to the function < has_viewer_data > the task
    of determing if the episode includes viewership "episode_us_viewers_mm" data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: episode with the highest recorded viewership.
    """
    maxi = []
    i = 0
    for episode in episodes:
        if has_viewer_data(episode):
            if episode['episode_us_viewers_mm'] > i:
                maxi.clear()
                i = episode['episode_us_viewers_mm']
                maxi.append(episode)
    return maxi[0]




def group_episodes_by_writer(episodes):
    """Utilizes a dictionary to group individual episodes by a contributing writer. The writer's
    name comprises the key and the associated value comprises a list of one or more episode
    dictionaries. Duplicate keys are NOT permitted.

    Format:
        {
            < writer name >: [{< episode_01 >}, {< episode_02 >}, ...],
            < writer name >: [{< episode_01 >}, {< episode_02 >}, ...],
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that groups episodes by a contributing writer
    """
    writer_accum = []
    new_dict = {}
    for episode in episodes:
        for key in episodes:
                for name in episode['episode_writers']:
                    if name in writer_accum:
                        continue
                    else:
                        writer_accum.append(name)
    for episode in episodes:
        for writer in writer_accum:
            if writer in episode['episode_writers']:
                if writer not in new_dict.keys():
                    new_dict[writer] = []
                new_dict[writer].append(episode)
    return(new_dict)

def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """
    if episode['episode_us_viewers_mm']:
        return True
    else:
        return False

def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    # 8.1 CHALLENGE 01
    clone_wars = read_csv('clone_wars.csv')
    clone_wars_22 = clone_wars[1:5]
    clone_wars_2012 = clone_wars[4:6]
    clone_wars_url = clone_wars[6][-1]
    clone_wars_even_num_seasons = clone_wars[2::2]

    # 8.2 CHALLENGE 02
    clone_wars_episodes = read_csv_to_dicts('clone_wars_episodes.csv')
    #a = has_viewer_data(clone_wars_episodes[3])

    # 8.3 Challenge 03

    # 8.4 Challenge 04
    clone_wars_episodes = convert_episode_values(clone_wars_episodes)
    utl.write_json('stu-clone_wars-episodes_converted.json',clone_wars_episodes)
    # 8.5 Challenge 05
    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)
    least_viewed_episode = get_least_viewed_episode(clone_wars_episodes)

    # 8.6 Challenge 06
    director_episode_counts = count_episodes_by_director(clone_wars_episodes)
    utl.write_json('stu-clone_wars-director_episode_counts.json', director_episode_counts)
    # 8.7 CHALLENGE 07
    writer_episodes = group_episodes_by_writer(clone_wars_episodes)
    utl.write_json('stu-clone_wars-writer_episodes.json',writer_episodes)
    # 8.8 CHALLENGE 08
    # 8.9 CHALLENGE 09
    base_url = 'https://swapi.py4e.com/api/'
    tatooine_params = {'search': 'tatooine'}
    wookiee_planets = utl.read_csv_to_dicts('wookieepedia_planets.csv')
    tatooine_data = utl.get_swapi_resource(base_url + '/planets', tatooine_params)['results'][0]
    for dict in wookiee_planets:
        if dict['name'].lower() == 'tatooine':
            tatooine_data.update(dict)
    tatooine = create_planet(tatooine_data)
    utl.write_json('stu-tatooine.json', tatooine.jsonable())

    # 8.10 CHALLENGE 10
    R2D2_params = {'search': 'R2-D2'}
    wookie_droids = utl.read_json('wookieepedia_droids.json')
    r2_d2_data = utl.get_swapi_resource(base_url + '/people', R2D2_params)['results'][0]
    for dict in wookie_droids:
        if dict['name'] == 'R2-D2':
            r2_d2_data.update(dict)
    r2_d2 = create_droid(r2_d2_data)
    utl.write_json('stu-r2_d2.json', r2_d2.jsonable())
    # 8.11 Challenge 11
    anakin_params = {'search': 'Anakin'}
    wookiee_people = utl.read_json('wookieepedia_people.json')
    anakin_data = utl.get_swapi_resource(base_url + '/people', anakin_params)['results'][0]
    for dict in wookiee_people:
        if dict['name'] == 'Anakin Skywalker':
            anakin_data.update(dict)
    anakin = create_person(anakin_data, wookiee_planets)
    utl.write_json('stu-anakin_skywalker.json', anakin.jsonable())

    # 8.12 CHALLENGE 12
    wookiee_starships = utl.read_csv_to_dicts('wookieepedia_starships.csv')
    twilight_data = wookiee_starships
    for dict in wookiee_starships:
        if dict['name'] == 'Twilight':
            twilight_data = dict
    twilight = create_starship(twilight_data)
    utl.write_json('stu-twilight.json',twilight.jsonable())

    # 8.13 CHALLENGE 13
    obi_wan_params = {'search': 'Obi-Wan Kenobi'}
    obi_wan_data = utl.get_swapi_resource(base_url + '/people', obi_wan_params)['results'][0]
    for dict in wookiee_people:
        if dict['name'] == 'Obi-Wan Kenobi':
            obi_wan_data.update(dict)
    obi_wan = create_person(obi_wan_data, wookiee_planets)
    crew_dict = {'pilot': anakin, 'copilot': obi_wan}
    crew = Crew(crew_dict)
    twilight.assign_crew_members(crew)
    utl.write_json('stu-twilight.json',twilight.jsonable())
    # 8.14 CHALLENGE 14
    padme_params = {'search': 'Padmé Amidala'}
    padme_data = utl.get_swapi_resource(base_url + '/people', padme_params)['results'][0]
    for dict in wookiee_people:
        if dict['name'] == 'Padme Amidala':
            padme_data.update(dict)
    padme = create_person(padme_data, wookiee_planets)

    c_3po_params = {'search': 'C-3PO'}
    c_3po_data = utl.get_swapi_resource(base_url + '/people', c_3po_params)['results'][0]
    for dict in wookie_droids:
        if dict['name'] == 'C-3PO':
            c_3po_data.update(dict)
    print(c_3po_data)
    c_3po = create_droid(c_3po_data)
    passengers = Passengers([padme, c_3po, r2_d2])
if __name__ == '__main__':
    main()
