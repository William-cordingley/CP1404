from Practical_06.car import Car


def main():
    my_car = Car(180)
    my_car.drive(30)
    print("Fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()