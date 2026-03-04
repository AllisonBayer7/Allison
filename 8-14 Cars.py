# car function and dictionary
def make_car(manufacturer, model, **options):
    """Build a dictionary containing everything we know about a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict
# Make a car with a couple of optional features.
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('audi', 'a4', color='black', year=2019)
print(car)
