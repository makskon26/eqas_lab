class Component:
    def accept(self, visitor):
        pass

class Company(Component):
    def __init__(self, departments):
        self.department_list = departments

    def accept(self, visitor):
        visitor.visit_company(self)

class Department(Component):
    def __init__(self, employees):
        self.employee_list = employees

    def accept(self, visitor):
        visitor.visit_department(self)

class Employee:
    def __init__(self, position_name, salary):
        self.position_name = position_name
        self.salary = salary

class Visitor:
    def visit_company(self, component):
        i = 1
        print("Зарплатна відомість компанії")
        for department in component.department_list:
            print(f"Департамент {i}")
            for employee in department.employee_list:
                print(f"Співробітник {employee.position_name} зарплата {employee.salary}")
            i += 1

    def visit_department(self, component):
        print("Зарплатна відомість департаменту")
        for employee in component.employee_list:
            print(f" {employee.position_name} заробітна плата {employee.salary}")

employee_1 = Employee('HR-менеджер', 10)
employee_2 = Employee('Програміст - j', 20)
employee_3 = Employee('Team-lead', 30)
employee_4 = Employee('Програміст', 11)
employee_5 = Employee('Програміст - m', 22)
employee_6 = Employee('team lead', 33)

department_1 = Department([employee_1, employee_2, employee_3])
department_2 = Department([employee_4, employee_5, employee_6])

company = Company([department_1, department_2])

visitor = Visitor()
department_1.accept(visitor)
department_2.accept(visitor)
company.accept(visitor)
