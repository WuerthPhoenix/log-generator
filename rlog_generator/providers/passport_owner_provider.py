def rand_passport_dob(fake):
    """
    Generate a datetime date of birth for a passport.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.passport_dob()

def rand_passport_number(fake):
    """
    Generate a passport number by replacing tokens to be alphanumeric.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.passport_number()

def rand_passport_owner(fake, gender='X'):
    """
    Generate a given name and surname for a passport owner.
    Args:
        fake (Faker): The Faker instance to use.
        gender: Gender marker of a passport owner (M, F, or X for non-binary).
    """
    return fake.passport_owner(gender=gender)