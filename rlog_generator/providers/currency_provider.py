def rand_cryptocurrency(fake):
    """
    Generate a random cryptocurrency name and code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.cryptocurrency()

def rand_cryptocurrency_code(fake):
    """
    Generate a random cryptocurrency code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.cryptocurrency_code()

def rand_cryptocurrency_name(fake):
    """
    Generate a random cryptocurrency name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.cryptocurrency_name()

def rand_currency(fake):
    """
    Generate a random currency name and code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.currency()

def rand_currency_code(fake):
    """
    Generate a random currency code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.currency_code()

def rand_currency_name(fake):
    """
    Generate a random currency name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.currency_name()

def rand_currency_symbol(fake, code=None):
    """
    Generate a currency symbol.
    Args:
        fake (Faker): The Faker instance to use.
        code: Optional; currency code to get the symbol for.
    """
    return fake.currency_symbol(code=code)

def rand_pricetag(fake):
    """
    Generate a random price tag.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.pricetag()
