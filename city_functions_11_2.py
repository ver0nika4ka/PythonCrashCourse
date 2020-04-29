def get_city_country(city_name, country_name, population=None):
    """Slightly formatted city name and country."""
    result_string = f"{city_name}, {country_name}".title()
    if population:
        result_string += f" – population: {population}."
    return result_string