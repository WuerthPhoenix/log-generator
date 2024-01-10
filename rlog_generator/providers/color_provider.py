def rand_color(fake, hue=None, luminosity=None, color_format='hex'):
    """
    Generate a color in a human-friendly way.
    Args:
        fake (Faker): The Faker instance to use.
        hue: Controls the hue value (number, tuple/list, or valid string like 'red').
        luminosity: Influences both saturation and value (e.g., 'bright', 'dark').
        color_format: The color model representation ('hsv', 'hsl', 'rgb', 'hex').
    """
    return fake.color(hue=hue, luminosity=luminosity, color_format=color_format)

def rand_color_name(fake):
    """
    Generate a color name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.color_name()

def rand_hex_color(fake):
    """
    Generate a color formatted as a hex triplet.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.hex_color()

def rand_rgb_color(fake):
    """
    Generate a color formatted as a comma-separated RGB value.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.rgb_color()

def rand_rgb_css_color(fake):
    """
    Generate a color formatted as a CSS rgb() function.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.rgb_css_color()

def rand_safe_color_name(fake):
    """
    Generate a web-safe color name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.safe_color_name()

def rand_safe_hex_color(fake):
    """
    Generate a web-safe color formatted as a hex triplet.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.safe_hex_color()
