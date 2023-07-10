
class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer( Employee,Freelancer): #if you write 1st freelencer in line then fiverr will come
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.company)