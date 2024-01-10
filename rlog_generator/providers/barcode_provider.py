def rand_ean(fake, length=13, prefixes=None):
    """
    Generate an EAN barcode of the specified length.
    Args:
        fake (Faker): The Faker instance to use.
        length: Length of the EAN barcode (8 or 13).
        prefixes: Optional; sequences with which the result will begin.
    """
    return fake.ean(length=length, prefixes=prefixes)

def rand_ean13(fake, prefixes=None):
    """
    Generate an EAN-13 barcode.
    Args:
        fake (Faker): The Faker instance to use.
        prefixes: Optional; sequences with which the result will begin.
    """
    return fake.ean13(prefixes=prefixes)

def rand_ean8(fake, prefixes=None):
    """
    Generate an EAN-8 barcode.
    Args:
        fake (Faker): The Faker instance to use.
        prefixes: Optional; sequences with which the result will begin.
    """
    return fake.ean8(prefixes=prefixes)

def rand_localized_ean(fake, length=13):
    """
    Generate a localized EAN barcode of the specified length.
    Args:
        fake (Faker): The Faker instance to use.
        length: Length of the EAN barcode (8 or 13).
    """
    return fake.localized_ean(length=length)

def rand_localized_ean13(fake):
    """
    Generate a localized EAN-13 barcode.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.localized_ean13()

def rand_localized_ean8(fake):
    """
    Generate a localized EAN-8 barcode.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.localized_ean8()
