# time: 8:36:00
# topic: Abstraction & Encapsulation

# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.

#abstraction:

class Car:
    def __init__(self):
    # at first all are false,not press anything.
        self.acc=False
        self.brk=False
        self.clutch=False

    def start (self):
        #when start the car ,all true
        # below 2 line are unnecessary part,not need to show these line.
        self.clutch=True   # abstract part
        self.acc=True    # abstract part.
        print("car started >> ")

#create obj
car1 =Car()
car1.start()  # this line is necessary part
# call start fnx

#=============================================

# Encapsulation: Wrapping data and function into a single unit (object).

# here,  (data + fnx) are : stay together.

#====================================

# Let's practice :
# qs1: Create Account class with 2 attribute - balance & account no .  Create methods for debit, credit & printing the balance.

class Account:
    def __init__ (self,bal,acc):
        self.balance=bal
        self.account_no=acc

    #debit method
    def debit ( self,amount):
        # self is point to acc1 and amount is new variable which i declare
        self.balance-= amount
        print("Rs.", amount,"was debited")

    #credit method: for add some amount
    def credit ( self,amount):
        self.balance+= amount
        print("Rs.", amount,"was credited")

    #return balance
    def get_balance(self):
         # self point to the acc1 obj.
        return self.balance

acc1 = Account( 30000,1213)
print(acc1.balance) # ans: 30000
print(acc1.account_no)  #ans: 1213

acc1.debit(1200)
acc1.credit(300)
print( acc1.get_balance())


# oops part_2_ from video
# time : 8: 51:00

# topic: 1: del keyword

# ==> used to delete object properties or object itself.

# example:  del s1.name   => for delete properties
#           del  s1     => for delete object .


# example : 01 of delete

class Student1:
    def __init__ (self,name):
        self.name=name

s1=Student1("ranok")
print(s1.name)   # ans: ranok
del s1  # delete s1 obj
# print(s1)  #  ans: give error , because already deleted.

#====================PRIVATE ===================


# TOPIC: PRIVATE ( like) attribute & method

# Conceptual implementation in Python

# explain:  PRIVATE ( like) attribute & method are:  meant to be used only within the class and are not accessible from outside the class.

#qs1: how to declare private ?
# ans: use double underscore( __) : at  starting position of any variable which we want to declare as private.

class Account1:
    def __init__( self, acc_no,acc_pass):
        # public acc_no
        self.acc_no =acc_no
        #declare as a private acc_pass using (__)
        self.__acc_pass= acc_pass
# so we can't access acc_pass outside this class

#create fnx and access private  __acc_pass inside the class
    def  reset_pass (self):
        print(self.__acc_pass)

acc1 =Account1("12345","abacds")

print(acc1.acc_no) # ans: 12345

print(acc1.reset_pass())  # ans: abacds  None

# NOTE: why None print , don't know?
#print( acc1.__acc_pass) # ans: give error ,because private.

#=======================================

# EXAMPLE: 02: PRIVATE

class Person:
    # declare name as : private
    __name ="anonymous"
    subject="math"

#fnx as private ( can't access from outside the class this fnx)
    def __hello(self):  # qs1: why have to give self here?
        print("hello, person")

    # call private fnx inside class
    def welcome (self):
        self.__hello()


p1= Person()
print(p1.subject)   #ans: math
#print(p1.__name)  # ans: error , because private.

# NOTE: can't call private fnx from outside ,
#print(p1.__hello()) # ans: give error, because private.

print(p1.welcome())  #ans: hello, person

#======

