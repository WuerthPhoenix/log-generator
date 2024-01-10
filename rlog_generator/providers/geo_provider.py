def rand_coordinate(fake, center=None):
    """
    Generate a random coordinate.
    Args:
        fake (Faker): The Faker instance to use.
        center: Optionally center the coordinate and pick a point within a radius.
    """
    return fake.coordinate(center=center)

def rand_latitude(fake):
    """
    Generate a random latitude.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.latitude()

def rand_latlng(fake):
    """
    Generate a random latitude and longitude pair.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.latlng()

def rand_local_latlng(fake, country_code='US', coords_only=False):
    """
    Generate a random latitude and longitude pair for a known location in a specified country.
    Args:
        fake (Faker): The Faker instance to use.
        country_code: Country code for the location.
        coords_only: Return only the coordinates without additional metadata.
    """
    return fake.local_latlng(country_code=country_code, coords_only=coords_only)

def rand_location_on_land(fake, coords_only=False):
    """
    Generate a random coordinate set guaranteed to exist on land.
    Args:
        fake (Faker): The Faker instance to use.
        coords_only: Return only the coordinates without additional metadata.
    """
    return fake.location_on_land(coords_only=coords_only)

def rand_longitude(fake):
    """
    Generate a random longitude.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.longitude()
