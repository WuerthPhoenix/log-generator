def rand_aba(fake):
    """
    Generate an ABA routing transit number.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.aba()

def rand_bank_country(fake):
    """
    Generate the bank provider’s ISO 3166-1 alpha-2 country code.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.bank_country()

def rand_bban(fake):
    """
    Generate a Basic Bank Account Number (BBAN).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.bban()

def rand_iban(fake):
    """
    Generate an International Bank Account Number (IBAN).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.iban()

def rand_swift(fake, length=None, primary=False, use_dataset=False):
    """
    Generate a SWIFT code.
    Args:
        fake (Faker): The Faker instance to use.
        length: Length of the SWIFT code (8, 11, or None for random).
        primary: If True, generate a primary branch SWIFT code.
        use_dataset: If True, use locale-specific dataset for generating SWIFT code.
    """
    return fake.swift(length=length, primary=primary, use_dataset=use_dataset)

def rand_swift11(fake, primary=False, use_dataset=False):
    """
    Generate an 11-digit SWIFT code.
    Args:
        fake (Faker): The Faker instance to use.
        primary: If True, generate a primary branch SWIFT code.
        use_dataset: If True, use locale-specific dataset for generating SWIFT code.
    """
    return fake.swift11(primary=primary, use_dataset=use_dataset)

def rand_swift8(fake, use_dataset=False):
    """
    Generate an 8-digit SWIFT code.
    Args:
        fake (Faker): The Faker instance to use.
        use_dataset: If True, use locale-specific dataset for generating SWIFT code.
    """
    return fake.swift8(use_dataset=use_dataset)
