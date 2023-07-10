class Number:
    def __init__(self,num):
            self.num = num
        
    def __add__(self, num2):
          print(" Lets add ") 
          return self.num +num2.num
    def __mul__(self, num2):
          print(" Lets multiply") 
          return self.num * num2.num


n1=(6)
n2=(5)
sum = n1 + n2
mul = n1*n2
print(sum)   
print(mul)