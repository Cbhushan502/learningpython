# class Employee:
#     company = "Bharat Gas"
#     salary = 4500
#     salarybonus = 500
#     # totalSalary = 5000

#     @property   
#     def totalSalary(self):
#         return self.salary + self.salarybonus

#     @totalSalary.setter
#     def totalSalary(self, val):
#         self.salarybonus = val - self.salary

# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 5800
# print(e.salary)
# print(e.salarybonus)

# def func(a):
#     return a+5

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6