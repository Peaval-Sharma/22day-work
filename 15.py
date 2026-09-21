class Employee:

    def calculateSalary(self):
        pass


class Manager(Employee):

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculateSalary(self):
        allowance = self.basic_salary * 30 / 100
        salary = self.basic_salary + allowance

        print("Employee Name :", self.name)
        print("Basic Salary  :", self.basic_salary)
        print("Allowance     :", allowance)
        print("Final Salary  :", salary)


class Developer(Employee):

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculateSalary(self):
        allowance = self.basic_salary * 20 / 100
        salary = self.basic_salary + allowance

        print("Employee Name :", self.name)
        print("Basic Salary  :", self.basic_salary)
        print("Allowance     :", allowance)
        print("Final Salary  :", salary)


# Manager Details
name1 = input("Enter Manager Name: ")
salary1 = float(input("Enter Manager Basic Salary: "))

m = Manager(name1, salary1)

print("\n--- Manager Details ---")
m.calculateSalary()


# Developer Details
name2 = input("\nEnter Developer Name: ")
salary2 = float(input("Enter Developer Basic Salary: "))

d = Developer(name2, salary2)

print("\n--- Developer Details ---")
d.calculateSalary()