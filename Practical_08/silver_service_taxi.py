from Practical_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(self.name, self.fuel,
                                                                                             self.odometer,
                                                                                             self.current_fare_distance,
                                                                                             self.price_per_km,
                                                                                             self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()


if __name__ == "__main__":
    taxi1 = SilverServiceTaxi("Hummer", 200, 2)
    print(taxi1)
    taxi1.drive(18)
    print(taxi1)
    print(taxi1.get_fare())
    