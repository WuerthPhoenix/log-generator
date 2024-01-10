def rand_android_platform_token(fake):
    """
    Generate an Android platform token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.android_platform_token()

def rand_chrome(fake, version_from=13, version_to=63, build_from=800, build_to=899):
    """
    Generate a Chrome web browser user agent string.
    Args:
        fake (Faker): The Faker instance to use.
        version_from: Starting version number.
        version_to: Ending version number.
        build_from: Starting build number.
        build_to: Ending build number.
    """
    return fake.chrome(version_from=version_from, version_to=version_to, build_from=build_from, build_to=build_to)

def rand_firefox(fake):
    """
    Generate a Mozilla Firefox web browser user agent string.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.firefox()

def rand_internet_explorer(fake):
    """
    Generate an Internet Explorer web browser user agent string.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.internet_explorer()

def rand_ios_platform_token(fake):
    """
    Generate an iOS platform token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ios_platform_token()

def rand_linux_platform_token(fake):
    """
    Generate a Linux platform token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.linux_platform_token()

def rand_linux_processor(fake):
    """
    Generate a Linux processor token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.linux_processor()

def rand_mac_platform_token(fake):
    """
    Generate a MacOS platform token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.mac_platform_token()

def rand_mac_processor(fake):
    """
    Generate a MacOS processor token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.mac_processor()

def rand_opera(fake):
    """
    Generate an Opera web browser user agent string.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.opera()

def rand_safari(fake):
    """
    Generate a Safari web browser user agent string.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.safari()

def rand_user_agent(fake):
    """
    Generate a random web browser user agent string.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.user_agent()

def rand_windows_platform_token(fake):
    """
    Generate a Windows platform token used in user agent strings.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.windows_platform_token()
