def rand_ssn(fake):
    """
    Generate a random Social Security Number (SSN).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ssn()