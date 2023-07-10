class Employee:
    company = "Monarch"
    salary = 100

chandra = Employee()
rajni = Employee()
chandra.salary = 10000
rajni.salary = 800

print(chandra.company)
print(rajni.company)
Employee.company = "YouTube"
print(chandra.company)
print(rajni.company)
print(chandra.salary)
print(rajni.salary)