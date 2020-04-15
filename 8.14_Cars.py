# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments
def car_info(manufacturer, model, **kwargs):
    kwargs['manufacturer_name'] = manufacturer
    kwargs['model_name'] = model
    return kwargs
car1 = car_info('subaru','outback',
                color='blue',
                tow_package=True)
car2 = car_info('suzuki','lapin',
                color='grey',
                tow_package=True)
print(f"{car1}\n{car2}")