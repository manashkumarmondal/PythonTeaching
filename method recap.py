# -*- coding: utf-8 -*-
"""Untitled32.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LAqs-fmvQAOh2Ftqz1tnhrSTWkWDP2dZ
"""

class Student:
  #constructor
  def __init__(self,a='',b=0):
    self.name=a
    self.marks=b
    
    

#instance method
  def display(self):
    print('Your name is',self.name)
    print('Your marks are', self.marks)

  def calculate(self):
    if(self.marks>=600):
      print("You got grade A")
    elif(self.marks>=500):
      print("You got  grade B")  
    elif(self.marks >=330):
      print('You got grade C')
    else:
      print("Sorry, you fail!")        


n=int(input("Enter number of students"))

i=0

while i<n:
  namein=input("Enter student name")
  marksin=int(input("Enter your marks"))

  s=Student(namein,marksin)
  s.display()
  s.calculate()

  i+=1

  print("------- -------- ------- --------")



#mutator and Accessor method
class demo:

  #mutator method
  def setName(self,e):
    self.name=e
  
  #accessor method
  def getName(self):
    return self.name  
  
  #mutator method
  def setMarks(self, m):
    self.marks=m 
  
  #accessor method
  def getMarks(self):
    return self.marks  


d=demo()
name=input("enter your name")
d.setName(name)
mark=int(input("enter your mark"))
d.setMarks(mark)

print('Your name is', d.getName())

#class method

class Bird:
  wings=2

  @classmethod
  def fly(cls, name):
    print('{} flies with {} wings'.format(name,cls.wings))


Bird.fly('Tuntuni')
Bird.fly('Crow')

class Myclass:
  m=0

  def __init__(self):
    Myclass.m=Myclass.m+1


  @staticmethod
  def noofObjects():
    print("No of Instances created :", Myclass.m)  



ob1=Myclass() 
ob2=Myclass()
Myclass.noofObjects()
ob3=Myclass()
ob=Myclass()
Myclass.noofObjects()