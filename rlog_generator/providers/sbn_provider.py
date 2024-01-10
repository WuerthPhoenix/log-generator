def rand_sbn9(fake, separator='-'):
    """
    Generate a random Standard Book Number (SBN).
    Args:
        fake (Faker): The Faker instance to use.
        separator: The separator to use in the SBN number.
    """
    return fake.sbn9(separator=separator)
