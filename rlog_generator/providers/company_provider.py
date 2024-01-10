def rand_bs(fake):
    """
    Generate a random company BS (Buzzword).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.bs()

def rand_catch_phrase(fake):
    """
    Generate a random company catch phrase.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.catch_phrase()

def rand_company(fake):
    """
    Generate a random company name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.company()

def rand_company_suffix(fake):
    """
    Generate a random company suffix.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.company_suffix()
