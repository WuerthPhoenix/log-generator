def rand_isbn10(fake, separator='-'):
    """
    Generate a random ISBN-10 number.
    Args:
        fake (Faker): The Faker instance to use.
        separator: The separator to use in the ISBN number.
    """
    return fake.isbn10(separator=separator)

def rand_isbn13(fake, separator='-'):
    """
    Generate a random ISBN-13 number.
    Args:
        fake (Faker): The Faker instance to use.
        separator: The separator to use in the ISBN number.
    """
    return fake.isbn13(separator=separator)