
def describe_city(city, country='USA'):
    """Display city and country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('new york')
describe_city('paris', 'france')