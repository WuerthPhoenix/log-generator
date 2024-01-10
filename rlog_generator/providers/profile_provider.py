def rand_profile(fake, fields=None):
    """
    Generates a complete profile.
    Args:
        fake (Faker): The Faker instance to use.
        fields: Optional; list of fields to include in the profile.
    """
    return fake.profile(fields=fields)

def rand_simple_profile(fake, sex=None):
    """
    Generates a basic profile with personal information.
    Args:
        fake (Faker): The Faker instance to use.
        sex: Optional; gender of the profile ('M' or 'F').
    """
    return fake.simple_profile(sex=sex)
