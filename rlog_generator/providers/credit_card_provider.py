def rand_credit_card_expire(fake, start='now', end='+10y', date_format='%m/%y'):
    """
    Generate a credit card expiry date.
    Args:
        fake (Faker): The Faker instance to use.
        start: Start date for expiry date generation.
        end: End date for expiry date generation.
        date_format: Format of the expiry date.
    """
    return fake.credit_card_expire(start=start, end=end, date_format=date_format)

def rand_credit_card_full(fake, card_type=None):
    """
    Generate a set of credit card details.
    Args:
        fake (Faker): The Faker instance to use.
        card_type: Optional; type of credit card to generate.
    """
    return fake.credit_card_full(card_type=card_type)

def rand_credit_card_number(fake, card_type=None):
    """
    Generate a valid credit card number.
    Args:
        fake (Faker): The Faker instance to use.
        card_type: Optional; type of credit card to generate.
    """
    return fake.credit_card_number(card_type=card_type)

def rand_credit_card_provider(fake, card_type=None):
    """
    Generate a credit card provider name.
    Args:
        fake (Faker): The Faker instance to use.
        card_type: Optional; type of credit card to generate.
    """
    return fake.credit_card_provider(card_type=card_type)

def rand_credit_card_security_code(fake, card_type=None):
    """
    Generate a credit card security code.
    Args:
        fake (Faker): The Faker instance to use.
        card_type: Optional; type of credit card to generate.
    """
    return fake.credit_card_security_code(card_type=card_type)
