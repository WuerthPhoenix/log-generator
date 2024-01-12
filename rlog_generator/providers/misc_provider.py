def rand_binary(fake, length=1048576):
    """
    Generate a random binary blob.
    Args:
        fake (Faker): The Faker instance to use.
        length: Length of the binary blob.
    """
    return fake.binary(length=length)

def rand_boolean(fake, chance_of_getting_true=50):
    """
    Generate a random boolean value.
    Args:
        fake (Faker): The Faker instance to use.
        chance_of_getting_true: Chance of the boolean being True.
    """
    return fake.boolean(chance_of_getting_true=chance_of_getting_true)

def rand_csv(fake, header=None, data_columns=None, num_rows=10, include_row_ids=False):
    """
    Generate random comma-separated values.
    Args:
        fake (Faker): The Faker instance to use.
        header: Optional header for the CSV.
        data_columns: Data columns for the CSV.
        num_rows: Number of rows in the CSV.
        include_row_ids: Include row IDs in the CSV.
    """
    return fake.csv(header=header, data_columns=data_columns, num_rows=num_rows, include_row_ids=include_row_ids)

def rand_dsv(fake, dialect='faker-csv', header=None, data_columns=None, num_rows=10, include_row_ids=False, delimiter=','):
    """
    Generate random delimiter-separated values.
    Args:
        fake (Faker): The Faker instance to use.
        dialect: Dialect for the DSV.
        header: Optional header for the DSV.
        data_columns: Data columns for the DSV.
        num_rows: Number of rows in the DSV.
        include_row_ids: Include row IDs in the DSV.
        delimiter: Delimiter used in the DSV.
    """
    return fake.dsv(dialect=dialect, header=header, data_columns=data_columns, num_rows=num_rows, include_row_ids=include_row_ids, delimiter=delimiter)

def rand_fixed_width(fake, data_columns, num_rows=10, align='right'):
    """
    Generate random fixed width values.
    Args:
        fake (Faker): The Faker instance to use.
        data_columns: Data columns for the fixed width output.
        num_rows: Number of rows.
        align: Alignment of the values.
    """
    return fake.fixed_width(data_columns=data_columns, num_rows=num_rows, align=align)

def rand_image(fake, size=(256, 256), image_format='png', hue=None, luminosity=None):
    """
    Generate an image with a random polygon.
    Args:
        fake (Faker): The Faker instance to use.
        size: Size of the image (width, height).
        image_format: Format of the image.
        hue: Hue of the image color.
        luminosity: Luminosity of the image color.
    """
    return fake.image(size=size, image_format=image_format, hue=hue, luminosity=luminosity)

def rand_json(fake, data_columns=None, num_rows=1, indent=None, cls=None):
    """
    Generate random JSON structure values.
    Args:
        fake (Faker): The Faker instance to use.
        data_columns: Specification for the data structure.
        num_rows: Number of rows the returned.
        indent: Number of spaces to indent the fields.
        cls: Optional JSON encoder to use for non-standard objects.
    """
    return fake.json(data_columns=data_columns, num_rows=num_rows, indent=indent, cls=cls)

def rand_json_bytes(fake, data_columns=None, num_rows=1, indent=None, cls=None):
    """
    Generate random JSON structure and return as bytes.
    Args:
        fake (Faker): The Faker instance to use.
        data_columns: Specification for the data structure.
        num_rows: Number of rows the returned.
        indent: Number of spaces to indent the fields.
        cls: Optional JSON encoder to use for non-standard objects.
    """
    return fake.json_bytes(data_columns=data_columns, num_rows=num_rows, indent=indent, cls=cls)

def rand_md5(fake):
    """
    Generate a random MD5 hash.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.md5()

def rand_null_boolean(fake):
    """
    Generate a random boolean value, which can also be None.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.null_boolean()

def rand_password(fake, length=10, special_chars=True, digits=True, upper_case=True, lower_case=True):
    """
    Generate a random password.
    Args:
        fake (Faker): The Faker instance to use.
        length: Length of the password.
        special_chars: Include special characters.
        digits: Include digits.
        upper_case: Include upper case letters.
        lower_case: Include lower case letters.
    """
    return fake.password(length=length, special_chars=special_chars, digits=digits, upper_case=upper_case, lower_case=lower_case)

def rand_psv(fake, data_columns=None, num_rows=10, include_row_ids=False):
    """
    Generate random pipe-separated values.
    Args:
        fake (Faker): The Faker instance to use.
        data_columns: Data columns for the PSV.
        num_rows: Number of rows in the PSV.
        include_row_ids: Include row IDs in the PSV.
    """
    return fake.psv(data_columns=data_columns, num_rows=num_rows, include_row_ids=include_row_ids)

def rand_sha1(fake):
    """
    Generate a random SHA1 hash.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.sha1()

def rand_sha256(fake):
    """
    Generate a random SHA256 hash.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.sha256()

def rand_tar(fake, file_name=None, file_mode=None, create_info=None):
    """
    Generate a random tar file.
    Args:
        fake (Faker): The Faker instance to use.
        file_name: Name of the file in the tar archive.
        file_mode: File mode for the file in the tar archive.
        create_info: Additional information for file creation.
    """
    return fake.tar(file_name=file_name, file_mode=file_mode, create_info=create_info)

def rand_tsv(fake, data_columns=None, num_rows=10, include_row_ids=False):
    """
    Generate random tab-separated values.
    Args:
        fake (Faker): The Faker instance to use.
        data_columns: Data columns for the TSV.
        num_rows: Number of rows in the TSV.
        include_row_ids: Include row IDs in the TSV.
    """
    return fake.tsv(data_columns=data_columns, num_rows=num_rows, include_row_ids=include_row_ids)

def rand_uuid4(fake):
    """
    Generate a random UUID4.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.uuid4()

def rand_xml(fake, root_element='data', num_rows=10, custom_fields=None):
    """
    Generate random XML data.
    Args:
        fake (Faker): The Faker instance to use.
        root_element: Root element of the XML.
        num_rows: Number of rows of data.
        custom_fields: Custom fields for the XML data.
    """
    return fake.xml(root_element=root_element, num_rows=num_rows, custom_fields=custom_fields)

def rand_zip(fake, file_name=None, file_mode=None, create_info=None):
    """
    Generate a random zip file.
    Args:
        fake (Faker): The Faker instance to use.
        file_name: Name of the file in the zip archive.
        file_mode: File mode for the file in the zip archive.
        create_info: Additional information for file creation.
    """
    return fake.zip(file_name=file_name, file_mode=file_mode, create_info=create_info)
