def rand_ascii_company_email(fake):
    """
    Generate a random ASCII company email.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ascii_company_email()

def rand_ascii_email(fake):
    """
    Generate a random ASCII email.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ascii_email()

def rand_ascii_free_email(fake):
    """
    Generate a random ASCII free email.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ascii_free_email()

def rand_ascii_safe_email(fake):
    """
    Generate a random ASCII safe email.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ascii_safe_email()

def rand_company_email(fake):
    """
    Generate a random company email.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.company_email()

def rand_dga(fake, year=None):
    """
    Generate a random DGA domain name.
    Args:
        fake (Faker): The Faker instance to use.
        year: Optional; year to base the DGA generation on.
    """
    return fake.dga(year=year)

def rand_domain_name(fake, levels=1):
    """
    Generate a random domain name.
    Args:
        fake (Faker): The Faker instance to use.
        levels: Number of subdomain levels.
    """
    return fake.domain_name(levels=levels)

def rand_domain_word(fake):
    """
    Generate a random domain word.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.domain_word()

def rand_email(fake, safe=True, domain=None):
    """
    Generate a random email.
    Args:
        fake (Faker): The Faker instance to use.
        safe: Optional; whether to generate a safe domain email.
        domain: Optional; specific domain for the email.
    """
    return fake.email(safe=safe, domain=domain)

def rand_free_email(fake):
    """
    Generate a random free email.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.free_email()

def rand_free_email_domain(fake):
    """
    Generate a random free email domain.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.free_email_domain()

def rand_hostname(fake, levels=1):
    """
    Generate a random hostname.
    Args:
        fake (Faker): The Faker instance to use.
        levels: Number of subdomain levels.
    """
    return fake.hostname(levels=levels)

def rand_http_method(fake):
    """
    Generate a random HTTP method.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.http_method()

def rand_iana_id(fake):
    """
    Generate a random IANA ID.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.iana_id()

def rand_ipv4(fake, network=False):
    """
    Generate a random IPv4 address.
    Args:
        fake (Faker): The Faker instance to use.
        network: Optional; whether to include network address.
    """
    return fake.ipv4(network=network)

def rand_ipv4_network_class(fake):
    """
    Generate a random IPv4 network class.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ipv4_network_class()

def rand_ipv4_private(fake):
    """
    Generate a random IPv4 private address.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ipv4_private()

def rand_ipv4_public(fake):
    """
    Generate a random IPv4 public address.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.ipv4_public()

def rand_ipv6(fake, network=False):
    """
    Generate a random IPv6 address.
    Args:
        fake (Faker): The Faker instance to use.
        network: Optional; whether to include network address.
    """
    return fake.ipv6(network=network)

def rand_mac_address(fake):
    """
    Generate a random MAC address.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.mac_address()

def rand_port_number(fake):
    """
    Generate a random port number.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.port_number()

def rand_slug(fake):
    """
    Generate a random slug.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.slug()

def rand_tld(fake):
    """
    Generate a random top-level domain.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.tld()

def rand_uri(fake):
    """
    Generate a random URI.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.uri()

def rand_uri_extension(fake):
    """
    Generate a random URI extension.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.uri_extension()

def rand_uri_page(fake):
    """
    Generate a random URI page.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.uri_page()

def rand_uri_path(fake, deep=None):
    """
    Generate a random URI path.
    Args:
        fake (Faker): The Faker instance to use.
        deep: Optional; how deep the path should be.
    """
    return fake.uri_path(deep=deep)

def rand_url(fake):
    """
    Generate a random URL.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.url()

def rand_user_agent(fake):
    """
    Generate a random user agent.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.user_agent()

def rand_user_name(fake):
    """
    Generate a random user name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.user_name()