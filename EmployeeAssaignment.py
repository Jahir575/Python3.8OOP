"""
Create an Employee class with following attributes and methods:

- constructor, which will create an instance of Employee class based on provided arguments:
    first name, last name, email address and monthly salary

- get_annual_salary method, which will calculate and return employee annual salary

- show_employee_information method, which will show employee information in such syntax:
    Employee: <full name>
    Email address: <email>
    Annual salary: <annual salary>

- an attribute, which will store the number of created objects of an Employee class
"""


class Employee:
    def __init__(self, first_name, last_name, email, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        annual_salary = self.monthly_salary * 12
        return annual_salary

    def employee_details(self):
        print(f"Employee: {self.first_name} {self.last_name}\n")
        print(f"Email: {self.email}\n")
        print(f"Annual Salary: {self.annual_salary()}\n")


employee1 = Employee('Sudhir', 'Ghosh','sudhir.ghosh@gmail.com', 16000)

employee2 = Employee('Ismail', 'Sheikh','ismail.sk@gmail.com', 18000)

employees = [employee1, employee2]

for employee in employees:
    employee.employee_details()
    print('\n')
    