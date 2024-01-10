def rand_address(fake):
    """
    Generate a random full address.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.address()

def rand_building_number(fake):
    """
    Generate a random building number.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.building_number()

def rand_city(fake):
    """
    Generate a random city name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.city()

def rand_city_suffix(fake):
    """
    Generate a random city suffix.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.city_suffix()

def rand_country(fake):
    """
    Generate a random country name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.country()

def rand_country_code(fake, representation='alpha-2'):
    """
    Generate a random country code.
    Args:
        fake (Faker): The Faker instance to use.
        representation: Format of the country code ('alpha-2', 'alpha-3', etc.).
    """
    return fake.country_code(representation=representation)

def rand_current_country(fake):
    """
    Generate the current country name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.current_country()

def rand_current_country_code(fake):
    """
    Generate the current country code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.current_country_code()

def rand_postcode(fake):
    """
    Generate a random postal code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.postcode()

def rand_street_address(fake):
    """
    Generate a random street address.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.street_address()

def rand_street_name(fake):
    """
    Generate a random street name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.street_name()

def rand_street_suffix(fake):
    """
    Generate a random street suffix.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.street_suffix()
