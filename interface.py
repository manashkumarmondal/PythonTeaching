# -*- coding: utf-8 -*-
"""Untitled47.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-IrAxfeGeYoR9wz906s5nCDvbwDc8jvc
"""

from abc import*
class Myclass(ABC):
  @abstractmethod
  def connect(self):
    pass
  @abstractmethod
  def disconnect(self):
    pass 

class Oracle(Myclass):
  def connect(self):
    print('Connecting to oracle database....')  

  def disconnect(self):
    print('Disconnected from Oracle database')   


class Sybase(Myclass):
  def connect(self):
    print('Connecting to sybase database....')

  def disconnect(self):
    print('Disconnected from sybase database') 



class Database:
  str=input('Enter your dayabase name')
  classname=globals()[str]
  #classname=str
  x=classname()

  # y=Oracle()
  # z=Sybase()
  x.connect()
  x.disconnect()

from abc import*
class Printer(ABC):
  @abstractmethod
  def printit(self, text):
    pass

  @abstractmethod
  def disconnect(self):
    pass

class IBM(Printer):
  def printit(self, text):
    print(text)

  def disconnect(self):
    print('Printing completed on IBM printer')


class Epson(Printer):
  def printit(self, text):
    print(text)


  def disconnect(self):        
    print("Printing completed on Epson printer")

class UserPrinter:
  with open("config.txt", "r") as f:
    str=f.readline()

    classname=globals()[str]

    y=classname()

    y.printit('Hello , this is sent to printer')
    y.disconnect()