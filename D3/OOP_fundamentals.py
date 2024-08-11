class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')

# myCar = Car('Kitt', 180)
# myOtherCar = Car('Speedy', 55)

# myCar.talk('Michael')


class Driver: 
    number_of_drivers = 0
    def __init__(self, name, age, ranking): 
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1
    def get_ranking(self): 
        return self.ranking
    def get_num_drivers(self): 
        return Driver.number_of_drivers

class Race: 
    def __init__(self, name, driver_limit, drivers):
        self.name = name
        self.driver_limit = dirver_limit
        self.drivers = []

    def add_driver(self,driver): 
        if len(self.drivers) < self.driver_limit: 
            self.drivers.append(driver)
            return True
        return False

    def get_average_ranking(self): 
        value = 0 
        for driver in self.drivers:
            value += driver.get_ranking()

        return value/ len(self.drivers)


my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

# printsSeattle 500 4 []
