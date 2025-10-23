"""Create a Python program that manages employee payroll using functions,
 default & keyword arguments, lambda functions, and scope concepts."""

# calculate salary with bonus and tax
def calculate_salary(base_salary,tax_rate,bonus=5000):
    return base_salary+bonus-(base_salary*tax_rate)

#diaplay employees inf0
def display_employee_info(name,role,salary):
    print(f"Name: {name} | Role: {role} | Monthly Salary: {salary}")

#calculate yearly salary using lamba function
yr_salary=lambda salary:salary*12

#sort employees by salary
def sort_by_salary(employees):
    employees.sort(key=lambda item:item['base_salary'])
    return employees

#sort employees by name
def sort_by_name(employees):
    employees.sort(key=lambda item:item['name'])
    return employees

#employee details
employees=[
    {"name":"Alice","role":"developer","base_salary":30000},
    {"name":"Bob","role":"manager","base_salary":50000},
    {"name":"carol","role":"designer","base_salary":25000},
    { "name":"John","role":"HR","base_salary":35000},
]
#output
print("----Employee Payroll Processor----")

print("company: TecNOva Pvt ltd\n")
for i in employees:
    display_employee_info(i["name"],i["role"],i["base_salary"])

print("\nsorted by salary")
for i,dict in enumerate(sort_by_salary(employees)):
    print(f"{i+1}) {dict['name']}-{dict['base_salary']:,.2f}")

print("\nsorted by name")
for i,dict in enumerate(sort_by_name(employees)):
    print(f"{i+1}) {dict['name']}-{dict['base_salary']:,.2f}")

print("\nyearly salaries:")
for i in employees:
    print(f"{i['name']}->{yr_salary(i['base_salary']):,.2f}")

print("\ntotal processed employees: ",len(employees))
