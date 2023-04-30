#Written by Shiven Desai
class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
    
    def set_name(self, name):
        self.__name = name
        
    def set_id_number(self, id_number):
        self.__id_number = id_number
        
    def get_name(self):
        return self.__name
    
    def get_id_number(self):
        return self.__id_number
    
class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, annual_salary, annual_bonus):
        super().__init__(name, id_number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus
        
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        
    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus
        
    def get_annual_salary(self):
        return self.__annual_salary
    
    def get_annual_bonus(self):
        return self.__annual_bonus

# Sample program
supervisor = ShiftSupervisor("John Smith", "1234", 50000, 10000)
print("Name:", supervisor.get_name())
print("ID number:", supervisor.get_id_number())
print("Annual salary:", supervisor.get_annual_salary())
print("Annual bonus:", supervisor.get_annual_bonus())
