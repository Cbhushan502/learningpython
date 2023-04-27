class Employee:
    company = "Monarch"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

chandra= Employee()
chandra.salary = 100000
chandra.getSalary("Thanks!") # Employee.getSalary(chandra)
chandra.greet() # Employee.greet()
chandra.time()
