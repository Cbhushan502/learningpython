# this is a base class of inheritance 
class Emplopyee:
    company="Monarch"
    def showDetails(self):
        print("This is a employee")

# this is a child class or derived class
class Programmer(Emplopyee):
    language = "Python"
    # company ="Microsoft"

    def getlanguage(self):
        print("fThe language is {self.language}"        )

    def showDetails(self):
        print("This is a prgrammer")

e = Emplopyee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)

