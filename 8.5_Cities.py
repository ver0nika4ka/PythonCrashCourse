# Give the parameter for the country a default value
# Call your function for three different cities,
# at least one of which is not in the default country. 
def describe_city(city, country='japan'):
    print(f"{city.title()} is in {country.title()}.")
describe_city('tokyo')

def describe_city(city, country='japan'):
    print(f"{city.title()} is in {country.title()}.")
describe_city(city='osaka')

def describe_city(city, country='japan'):
    print(f"{city.title()} is in {country.title()}.")
describe_city(city='minsk', country='belarus')
