def rand_license_plate(fake):
    """
    Generate a random license plate.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.license_plate()

def rand_vin(fake):
    """
    Generate a random VIN (Vehicle Identification Number).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.vin()