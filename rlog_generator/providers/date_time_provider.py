def rand_am_pm(fake):
    """
    Generate a random AM or PM.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.am_pm()

def rand_century(fake):
    """
    Generate a random century.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.century()

def rand_date(fake, pattern='%Y-%m-%d', end_datetime=None):
    """
    Generate a random date string.
    Args:
        fake (Faker): The Faker instance to use.
        pattern: Format of the date.
        end_datetime: Latest possible date.
    """
    return fake.date(pattern=pattern, end_datetime=end_datetime)

def rand_date_between(fake, start_date='-30y', end_date='today'):
    """
    Generate a random date between two dates.
    Args:
        fake (Faker): The Faker instance to use.
        start_date: Start date for generation.
        end_date: End date for generation.
    """
    return fake.date_between(start_date=start_date, end_date=end_date)

def rand_date_between_dates(fake, date_start=None, date_end=None):
    """
    Generate a random date between two specific dates.
    Args:
        fake (Faker): The Faker instance to use.
        date_start: Start date for generation.
        date_end: End date for generation.
    """
    return fake.date_between_dates(date_start=date_start, date_end=date_end)

def rand_date_object(fake, end_datetime=None):
    """
    Generate a random date object.
    Args:
        fake (Faker): The Faker instance to use.
        end_datetime: Latest possible date.
    """
    return fake.date_object(end_datetime=end_datetime)

def rand_date_of_birth(fake, tzinfo=None, minimum_age=0, maximum_age=115):
    """
    Generate a random date of birth.
    Args:
        fake (Faker): The Faker instance to use.
        tzinfo: Timezone information.
        minimum_age: Minimum age.
        maximum_age: Maximum age.
    """
    return fake.date_of_birth(tzinfo=tzinfo, minimum_age=minimum_age, maximum_age=maximum_age)

def rand_date_this_century(fake, before_now=True, after_now=False, tzinfo=None):
    """
    Generate a random datetime object for the current century.
    Args:
        fake (Faker): The Faker instance to use.
        before_now: Include dates before today.
        after_now: Include dates after today.
        tzinfo: Timezone information.
    """
    return fake.date_this_century(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def rand_date_this_decade(fake, before_now=True, after_now=False, tzinfo=None):
    """
    Generate a random datetime object for the current decade.
    Args:
        fake (Faker): The Faker instance to use.
        before_now: Include dates before today.
        after_now: Include dates after today.
        tzinfo: Timezone information.
    """
    return fake.date_this_decade(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def rand_date_this_month(fake, before_now=True, after_now=False, tzinfo=None):
    """
    Generate a random datetime object for the current month.
    Args:
        fake (Faker): The Faker instance to use.
        before_now: Include dates before today.
        after_now: Include dates after today.
        tzinfo: Timezone information.
    """
    return fake.date_this_month(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def rand_date_this_year(fake, before_now=True, after_now=False, tzinfo=None):
    """
    Generate a random datetime object for the current year.
    Args:
        fake (Faker): The Faker instance to use.
        before_now: Include dates before today.
        after_now: Include dates after today.
        tzinfo: Timezone information.
    """
    return fake.date_this_year(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def rand_day_of_month(fake):
    """
    Generate a random day of the month.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.day_of_month()

def rand_day_of_week(fake):
    """
    Generate a random day of the week.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.day_of_week()

def rand_future_date(fake, end_date="+30d", tzinfo=None):
    """
    Generate a random future date.
    Args:
        fake (Faker): The Faker instance to use.
        end_date: Latest possible date.
        tzinfo: Timezone information.
    """
    return fake.future_date(end_date=end_date, tzinfo=tzinfo)

def rand_future_datetime(fake, end_date="+30d", tzinfo=None):
    """
    Generate a random future datetime.
    Args:
        fake (Faker): The Faker instance to use.
        end_date: Latest possible datetime.
        tzinfo: Timezone information.
    """
    return fake.future_datetime(end_date=end_date, tzinfo=tzinfo)

def rand_iso8601(fake, tzinfo=None, sep='T', timespec='auto'):
    """
    Generate a random timestamp in ISO 8601 format.
    Args:
        fake (Faker): The Faker instance to use.
        tzinfo: Timezone information.
        sep: Separator between date and time.
        timespec: Format specifier for the time part.
    """
    return fake.iso8601(tzinfo=tzinfo, sep=sep, timespec=timespec)

def rand_month(fake):
    """
    Generate a random month (number).
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.month()

def rand_month_name(fake):
    """
    Generate a random month name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.month_name()

def rand_past_date(fake, start_date="-30d", tzinfo=None):
    """
    Generate a random past date.
    Args:
        fake (Faker): The Faker instance to use.
        start_date: Earliest possible date.
        tzinfo: Timezone information.
    """
    return fake.past_date(start_date=start_date, tzinfo=tzinfo)

def rand_past_datetime(fake, start_date="-30d", tzinfo=None):
    """
    Generate a random past datetime.
    Args:
        fake (Faker): The Faker instance to use.
        start_date: Earliest possible datetime.
        tzinfo: Timezone information.
    """
    return fake.past_datetime(start_date=start_date, tzinfo=tzinfo)

def rand_pytimezone(fake):
    """
    Generate a random timezone.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.pytimezone()

def rand_time(fake, pattern='%H:%M:%S', end_datetime=None):
    """
    Generate a random time string.
    Args:
        fake (Faker): The Faker instance to use.
        pattern: Format of the time.
        end_datetime: Latest possible time.
    """
    return fake.time(pattern=pattern, end_datetime=end_datetime)

def rand_time_delta(fake, end_datetime=None):
    """
    Generate a random timedelta object.
    Args:
        fake (Faker): The Faker instance to use.
        end_datetime: Latest possible timedelta.
    """
    return fake.time_delta(end_datetime=end_datetime)

def rand_time_object(fake, end_datetime=None):
    """
    Generate a random time object.
    Args:
        fake (Faker): The Faker instance to use.
        end_datetime: Latest possible time object.
    """
    return fake.time_object(end_datetime=end_datetime)

def rand_time_series(fake, start_date=None, end_date=None, precision=None, distrib=None):
    """
    Generate a random time series.
    Args:
        fake (Faker): The Faker instance to use.
        start_date: Start date for the time series.
        end_date: End date for the time series.
        precision: Time interval for the time series.
        distrib: Callable to generate values for each point in time.
    """
    return fake.time_series(start_date=start_date, end_date=end_date, precision=precision, distrib=distrib)

def rand_timezone(fake):
    """
    Generate a random timezone name.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.timezone()

def rand_unix_time(fake, end_datetime=None):
    """
    Generate a random Unix timestamp.
    Args:
        fake (Faker): The Faker instance to use.
        end_datetime: Latest possible timestamp.
    """
    return fake.unix_time(end_datetime=end_datetime)

def rand_year(fake):
    """
    Generate a random year.
    Args:
        fake (Faker): The Faker instance to use.
    """
    return fake.year()
