# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LRsOp3ZXas_tDWCwm7VVWH7ygKBFZr_g
"""

def swar():
  print('I am swarnaly')
  print('I am Indian')


swar()

def fun(fullname):
  print('My name is', fullname)



for i in range(5):
  
  fun('Swarnaly')
  fun('Partha')
  fun('21 cr')
  print()

def cbi(first, second):

  print(first +' is the friend of '+ second)


#cbi('swarnaly','partha')

def ed():
  print('Thaank you for callin me...')
  fname=input('Enter the first friend')
  lname=input('Enter the second friend')
  cbi(fname,lname)


ed()

def collection(*element):
  print('We found '+ element[3] +' as a 4th element')

collection('gold','bidesimudra','mohor','dolil')



def food(dish='Niramis'):
  print('I love to eat '+dish )


food('Biriyani')
food('Moglai')
food('Chinees')
food() 
food('Indian')
food('Octopas')

def menu(item):
  for i in item:
    print(i)


lst=['sweet','chicken','rice','vejdal']

menu(lst)

def orange(k):
  l=k**2
  return l



result=orange(5)
result=result-4
print("The result is ", result )

print("the result is", orange(6))
