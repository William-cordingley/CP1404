# Classes
class Student:
    def __init__(self, first_name=" ", last_name=" ", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.id)


# Simple example class usage
first_name = input("First Name: ")
last_name = input("Last Name: ")
student_id = input("ID: ")
s1 = Student(first_name, last_name, student_id)
print(s1.first_name, "has ID", s1.id)


# in lecture example of class using the product thingy above
class Product:
    GST_RATE = 0.1  # 10%

    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        sale_status = 'y' if self.is_on_sale else 'n'
        return "{}, ${:.2f} ({})".format(self.name, self.price, self.is_on_sale)


p1 = Product("Phone", 365.4, True)
# p1.name = "Phone"
print(p1.name, p1.price, p1.is_on_sale)
print(p1.GST_RATE)
