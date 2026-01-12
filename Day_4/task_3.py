# function based calculate net salary of an employee
def calculate_net_salary(gross_salary, deductions):
    net_salary = gross_salary - deductions
    return net_salary
gross_salary = 5000
deductions = 1200
net_salary = calculate_net_salary(gross_salary, deductions)
print("Net Salary:", net_salary)
