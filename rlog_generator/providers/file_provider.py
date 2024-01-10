def rand_file_extension(fake, category=None):
    """
    Generate a random file extension.
    Args:
        fake (Faker): The Faker instance to use.
        category: Optional; category of the file extension.
    """
    return fake.file_extension(category=category)

def rand_file_name(fake, category=None, extension=None):
    """
    Generate a random file name.
    Args:
        fake (Faker): The Faker instance to use.
        category: Optional; category of the file.
        extension: Optional; file extension.
    """
    return fake.file_name(category=category, extension=extension)

def rand_file_path(fake, depth=1, category=None, extension=None):
    """
    Generate a random file path.
    Args:
        fake (Faker): The Faker instance to use.
        depth: Depth of the file path.
        category: Optional; category of the file.
        extension: Optional; file extension.
    """
    return fake.file_path(depth=depth, category=category, extension=extension)

def rand_mime_type(fake, category=None):
    """
    Generate a random MIME type.
    Args:
        fake (Faker): The Faker instance to use.
        category: Optional; category of the MIME type.
    """
    return fake.mime_type(category=category)

def rand_unix_device(fake, prefix=None):
    """
    Generate a random Unix device file name.
    Args:
        fake (Faker): The Faker instance to use.
        prefix: Optional; prefix for the Unix device.
    """
    return fake.unix_device(prefix=prefix)

def rand_unix_partition(fake, prefix=None):
    """
    Generate a random Unix partition name.
    Args:
        fake (Faker): The Faker instance to use.
        prefix: Optional; prefix for the Unix partition.
    """
    return fake.unix_partition(prefix=prefix)
