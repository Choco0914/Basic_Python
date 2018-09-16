from car_s import Car
from electric_cars import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2018)
print(my_tesla.get_descriptive_name())
