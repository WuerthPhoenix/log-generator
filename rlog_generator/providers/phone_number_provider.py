def rand_country_calling_code(fake):
    """
    Generate a random country calling code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.country_calling_code()

def rand_msisdn(fake):
    """
    Generate a random MSISDN (Mobile Station International Subscriber Directory Number).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.msisdn()

def rand_phone_number(fake):
    """
    Generate a random phone number.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.phone_number()