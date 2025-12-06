# PART_3: FROM 9:00:00
# TOPIC 01: INHERITANCE
# TOPIC: 02
#TOPIC: 03

#INHERITANCE:  -> when one class (child/ derived) derives the properties & methods of another class ( parents/ base)

# EXAMPLE: 01

class Car:
    color="red"
    #qs1: WHY USE  static method here?
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar ( Car):  # car is inheritant here
    #constructor
    def __init__(self,name):
        self.name=name
#create car1 and car2 obj
car1 =ToyotaCar("mercedes")
car2= ToyotaCar("pioner")

#call ToyotaCar er parent class Car
print(car1.start())  #ans: car started..
print(car1.stop()) #ans: None
print(car1.color) #ans: red


#==============TYPE OF INHERITANCE=======
#TYPES
# 1. Single Inheritance
#2.Multi-level inheritance
#3.Multiple Inheritance

#1.single Inheritance: it has 1 base class -> 1 derived class . parent->child class .

#EXAMPLE:


#2 Multi-level inheritance:
# here,  1-> 2->3->4....
#   level1 to level2 , level2 to level 3 inheritance

#EXAMPLE:

class Car1:
    color="red"
    @staticmethod
    def start1():
        print("car started..")

    @staticmethod
    def stop1():
        print("car stopped.")

#ToyotaCar1 inheritant the Car1 class
class ToyotaCar1 ( Car1):
    #constructor
   def __init__ (self,brand):
        self.brand=brand

#Fortuner class inheritant to ToyotaCar1 class
class Fortuner (ToyotaCar1):
    def __init__ (self,type):
        self.type=type

car1 =Fortuner("diesel")
car1.start1()  # ans: car started..
car1.stop1()  # ans: car stopped..

# car1 is Fortuner class object but start1 and stop1 are Car class fnx , access using inheritance.

#===========================
#===MULTIPLE INHERITANCE ======

#DEFINE:  1 child / derived class can be : inheritant 2,3 or more base or parent class .

# EX: Suppose, child class inheritant both par1 and par2 class .
#EXAMPLE:

class A:
    varA ="welcome to class A"

class B:
    varA ="welcome to class B"
# class C , inheritant both class A and class B
class C(A,B):
    varC ="welcome to class C"

# create object of class C , it call  default constructor
c1 =C()
print(c1.varA)  #ans: welcome to class A
print(c1.varC)  #ans: welcome to class B
print(c1.varC)  ##ans: welcome to class C

#====================================

#TOPIC: SUPER METHOD

# super() : method : is used to access methods of the parent class.

class Car2:
    #constructor
    def __init__(self,type):
        self.type =type

    @staticmethod
    def start2():
        print("car started..")

    @staticmethod
    def stop2():
        print("car Stopped..")

class ToyotaCar2(Car2):
    #constructor
    def __init__ (self,name,type):
        self.name=name
        # i want to take Car2 class type
        super().__init__(type)
# super class a constructor class call korbo, and pass the : type  method.
        super().start2()   #ans:

#NOTE: when ToyotaCar2 will be create obj , start2 method also will be called using super()

#NOTE: IN THIS WAY , USING super() , we can call parent class any  method , constructor,


car3 =ToyotaCar2("ranok","electric")
print(car3.type)  #ans: electric  car started..





#=====================================


# TOPIC: CLASS METHOD
# Defination: A class method is bound to the class & receive the class as an implicit first argument

# NOTE:
# QS: 1:  what is the meaning of @staticmethod ?

#ans: if we create a @staticmethod,  means:
# this method can't create every time for any object or instance

# this @staticmethod :  create only 1 time for all object and all obj can use it.

# because : this @staticmethod : can't access  or change instance

#NOTE: static method can't access or modify : class state & generally for utility .

# QS 1: generally where we use @staticmethod?
# ans: ** generally , where don't crate or don't use any  class attribute or instance attribute  ,there we use @staticmethod

#example:
# @staticmethod
# def start():
#     print("car started..")

#here, not use any class attribute or instance

#=================

#example:
class Person:
    # class attribute : name and work
    name="anonymous"
    work="part_time"

    def changeName(self,name):
        self.name= name
        #QS : how to change class attribute name  ?
        #ans: for this write below line
        Person.name= name   # change name

#2nd way: for change the class attribute :
        #change the work type
        self.__class__.work="full_time"
        # NOTE: HERE, __class__  : indicate the Person class

p1= Person()
p1.changeName("sakline")  #call fnx and define name
print(p1.name) #ans: sakline
# ( after change the class attribute Person name )
print(Person.name)  #ans: sakline

print(Person.work) #ans: full_time


#================
# QS 1: we want directly access inside the fnx , how?
#ans:   for this :   use: class method ,
#  using class method: we can change the class attribute.

class person1:
    #class attribute
    name ="ranok"

#change the class attribute value

    @classmethod
    def changeName2(cls, name):
        cls.name=name


p2 =person1()
# p2.changeName2("mehrab")
print(p2.name)   #ans: ranok
print(person1.name) # ans: ranok

p2.changeName2("mehrab")
print(p2.name) #ans: mehrab
print(person1.name)  #ans: mehrab

#==========================

# we have 3 type fnx or method:
#1 . static method  ( @staticmethod) : use : where we have just  don't need any class or instance method , there we use static method :

#EX:
#    @staticmethod
#     def start2():
#         print("car started..")

#2. class method  ( cls):  use: where just need class attribute ,there we use class method

# class person1:
#     #class attribute
#     name ="ranok"

#     @classmethod
#     def changeName2(cls, name):
#         cls.name=name


# p2 =person1()
# # p2.changeName2("mehrab")
# print(p2.name)   #ans: ranok
# print(person1.name) # ans: ranok


#3 . instance method ( self): where just need instance properties , there use instance method.

# EX: self using :


#=========topic: property decorator====================

# Property: we use @property decorator on any method in the class to use the method as a property .

# EXAMPLE:

#QS 1: i want to change value 98 to 86 . and calculate avg
#ans:

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math= math
        self.percentange =str((self.phy +self.math +self.chem)/3) + "%"

    #create fnx for percentange calculate
    def calcPercentage(self):
        self.percentange = str((self.phy +self.math +self.chem)/3) + "%"


stu1 =Student(98,92,95)
print(stu1.percentange) #ans: 95.0%

stu1.phy=86
print(stu1.phy)   #ans: 86   give change value
print(stu1.percentange) #ans: 95.0%  give previous %

stu1.phy=34
#call fnx
stu1.calcPercentage()
print(stu1.percentange)  #ans:73.66666666666667%


#====another way : for solving this problem :use @property decorator

#EXPLAIN: ** We use @property decorator on any method in the class to use the method as a property.

#  if an attribute value - > depend on function , then :  we can create this function , to a : property/ attribute .

#so, way:


class Student3:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math= math



    @property
    def percentage(self):
        return   str((self.phy +self.math +self.chem)/3) + "%"



stu1 =Student3(98,92,95)
print(stu1.percentage) #ans: 95.0%

stu1.phy=86
print(stu1.percentage) #ans: 91.0%

#======================================

