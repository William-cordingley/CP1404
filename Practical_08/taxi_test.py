from Practical_08.taxi import Taxi

taxi1 = Taxi("Prius 1", 100)
taxi1.drive(40)
print(taxi1)
taxi1.start_fare()
taxi1.drive(100)
print(taxi1)
print(taxi1.get_fare())