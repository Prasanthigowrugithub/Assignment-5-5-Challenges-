#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Challenge 1: Square Numbers and Return Their Sum

class Point :
        
        
    def _init_(self):
        self.x=int(input("enter first number"))
        self.y=int(input("enter second number"))
        self.z=int(input("enter third number"))
        
    def sqSum(self):

        a=self.x*2+self.y2+self.z*2
        return a
    
     
obj=Point()
print(obj.sqSum())





Challenge 2: Implement a Calculator Class
class Calculator:
    num1=float(input("enter num : "))
    num2=float(input("enter other num : "))
    print(f"numbers are {num1} and {num2}")
    def add(self):
        return (self.num1+self.num2)
    def subtract(self):
        return (self.num1-self.num2)
    def multiply(self):
        return (self.num1*self.num2)
    def divide(self):
        return (self.num1//self.num2)
obj=Calculator()
print(obj.add())
print(obj.divide())
print(obj.subtract())
print(obj.multiply())






# Challenge 3: Implement the Complete Student Class
class Student:
    def _init(self,name,_RollNmber):  #private properties
        self._name=_name
        self._RollNumber=_RollNmber
        print(f"name  : {self._name} \nrollno : {_RollNmber}")

    def setName(self,name): 
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,Rollnumber):
        self.__RollNumber=Rollnumber
    def getRollNumber(self):
        return self.__RollNumber
obj=Student("sia",67)
(obj.setName("kim"))
(obj.setRollNumber(7))
print((obj.getName()))
print((obj.getRollNumber()))





Challenge 4:
class Account:  #create class 
    def _init_(self,title=0,Balance=0):
        self.title=title
        self.Balance=Balance


class SavingsAccount(Account):  #create subclass
    def _init_(self,title,Balance,interestRate):
        self.interestRate=interestRate
        super()._init_(title,Balance)
        
        

    def display(self): 
     return(f"{self.title} is the title , and the {self.Balance} is the account balance and {self.interestRate} is the interrestRate")

obj=SavingsAccount("sia",5000,2)
print(obj.display())






Challenge 5: Handling a Banking Account
class Account:
    def _init_(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance
    def getBalance(self):
        print("your balance is :")
        return self.Balance
    def deposit(self,amount):
        self.amount=amount
        self.Balance=self.Balance+self.amount
        print("Balance after deposited is :")
        return self.Balance

    def withdrawal(self,amount):
        self.amount=amount
        self.Balance=self.Balance-self.amount
        print("Balance after withdrawn is : ")
        return self.Balance
    
    
class SavingsAccount(Account):
    def _init_(self,title=None,Balance=0,interestRate=0):
        super()._init_(title,Balance) 
        
        self.interestRate= interestRate 
    def InterestAmount(self):
        print("interest amount is: ")
        return ((self.interestRate*self.Balance)//100)
    def display(self):
   
        return  f"{self.title} has balance {self.Balance} in account  and interest is: {self.interestRate} "
    

    
obj=SavingsAccount("sia",5000,2)
print(obj.display())
print(obj.InterestAmount())

print(obj.getBalance())
print(obj.deposit(88))
print(obj.withdrawal(10))

