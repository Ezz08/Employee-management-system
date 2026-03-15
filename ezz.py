class Employee:
    count = 0
    company = "rocket"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        Employee.count += 1

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")
        print(f"Company: {Employee.company}")


class Manager(Employee):
    bonus = 5000
    pass

m1 = Manager("Ezz", 80000, "Manager")
E1 = Employee("Ali", 45000, "Employee")
E2 = Employee("Mostafa", 25000, "Employee")
E3 = Employee("Adham", 32000, "Employee")

m1.display()
print(f"Bonus: {m1.bonus}")
print()

E1.display()
print()

E2.display()
print()

E3.display()
print()

print(f"The number of individuals is {Employee.count}")