from abc import ABC, abstractmethod
import datetime

class Vehicle(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Car(Vehicle):
    def __init__(self):
        self._brand = None
        self._model = None
        self._year = None

    def set_brand(self, brand):
        self._brand = brand

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def display_info(self):
        print("Car Information:")
        print("Brand:", self._brand)
        print("Model:", self._model)
        print("Year:", self._year)

class Airplane(Vehicle):
    def __init__(self):
        self._flights = None
        self._seats = None
        self._pilots = None

    def set_flights(self, flights):
        self._flights = flights

    def get_flights(self):
        return self._flights

    def set_seats(self, seats):
        self._seats = seats

    def get_seats(self):
        return self._seats

    def set_pilots(self, pilots):
        self._pilots = pilots

    def get_pilots(self):
        return self._pilots

    def display_info(self):
        print("Airplane Information:")
        print("Flights:", self._flights)
        print("Seats:", self._seats)
        print("Pilots:", self._pilots)

def create_car():
    car = Car()

    brand = input("Enter car brand (word): ")
    car.set_brand(brand)

    model = input("Enter car model (word): ")
    car.set_model(model)

    while True:
        try:
            year = input("Enter year of production (yyyy-mm-dd): ")
            year = datetime.datetime.strptime(year, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the year in the format yyyy-mm-dd.")

    car.set_year(year)

    return car

def create_airplane():
    airplane = Airplane()

    flights = input("Enter number of flights: ")
    airplane.set_flights(int(flights))

    seats = input("Enter number of seats: ")
    airplane.set_seats(int(seats))

    pilots = input("Enter number of pilots: ")
    airplane.set_pilots(int(pilots))

    return airplane

vehicle_type = input("Enter vehicle type (car or airplane): ")

if vehicle_type == "car":
    vehicle = create_car()
elif vehicle_type == "airplane":
    vehicle = create_airplane()
else:
    print("Invalid vehicle type.")
    exit()

vehicle.display_info()
