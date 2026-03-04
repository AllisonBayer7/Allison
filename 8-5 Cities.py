# Functions with default values
def describe_city(city, country='usa'):
    """Display a simple message about a city."""
    print(f"{city.title()} is in {country.title()}.")   

# Call function with one not in the default value
describe_city('charelston')
describe_city('roaton', 'belize ')
describe_city('savannah')