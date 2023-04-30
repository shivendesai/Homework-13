#Written by Shiven Desai
class Person:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, mailing_list=False):
        super().__init__(name, address, phone_number)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

# create a customer object
customer1 = Customer("John Doe", "123 Main St", "555-1234", "12345", True)

# print the customer's information
print("Customer name:", customer1.name)
print("Customer address:", customer1.address)
print("Customer phone number:", customer1.phone_number)
print("Customer number:", customer1.customer_number)
print("Wants to be on mailing list:", customer1.mailing_list)
