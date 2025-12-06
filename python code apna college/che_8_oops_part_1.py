# cheapter: 8 OOPS part_1

# describe: To map with real world scenarios, we started using objects in code.
# this is called : oop.
# function: reduce redundancy and increase reusability.
# oop: more preferable then function. here can use class ,object for reduce reusability.

# object: pen, mouse,book . ....anythings.
# oops: use for solving real world problem

# topic: class and  object
# class : class is a blueprint for creating objects.

class Student:
    name="ranok"

#creating object(instance)
s1=Student()
print(s1)
 #ans:<__main__.Student object at 0x000001F638BA6A50>    give location.
print(s1.name)  # ans: ranok

#create another object

s2=Student()
print(s2.name) #ans:ranok
#===================

class Car:
    color="blue"
    brand="marcedies"

car1=Car()
print(car1.color)
print(car1.brand)

#=========================

# topic: 02 :constructor
# defination: All classes have a function called __init__(), which is always executed when the class is being initiated.

# NOTE: IF  i CREATE NEW OBJECT , IT AUTOMATICALLY CALL -> THE   __init__ function.

# NOTE: if ** we not create __init__ function, when ojectwill be called: then it create  __init__ fnx automatically (internally) and call and execute .( same as constructor)

# self parameter:  self is point to the new object . for which object this __init__ fnx will be called here.

class Student2:
    name="Akbar Ali"
    def __init__ (self):
        print(self)  # ans: <__main__.Student2 object at 0x000001B533496CF0>
        print("adding new student in Database..")

s1=Student2()  # this obj call __init__ fnx.

print(s1)   #ans:<__main__.Student2 object at 0x000001B533496CF0>
#here, s1 and self  -> indicate the same pointer.

#==================================

class Student3:
    def __init__ (self, fullname,marks):  # <--CONSTRUCTOR
        self.name =fullname
        self.marks=marks
    # name is variable ,which store fullname
        print("adding new")
s1=Student3("rahim",92)
print(s1.name,s1.marks)

s2=Student3("ripon mondol",72)
print(s2.name,s2.marks)

# NOTE: IN CONSTRUCTOR ALWAYS WRITE: self argument. if not write gives error.

# NOTE: WE CAN WRITE ANYTHING IN THE PLACE OF self , but 1st parameter always point to the current .

#=================================
# attribute:
# all store : data, variable are called : attribute.

#====================

class Student4:


    # default constructor
    def __init__ (self):
        pass
        #print("adding new")

    # parameterize constructor
    def __init__ (self, name,marks):
        self.name =name
        self.marks=marks
        print("adding new")


s1=Student4("konok",92)
print(s1.name,s1.marks)

s2=Student4("ruplal",72)
print(s2.name,s2.marks)

#==========================
# topic: class and instance attribute.
# class.attr   and obj.attr

# class attribute: which is same for all class,
# object attribute: which is diff for every object.

# EXAMPLE: ***
# suppose, Student (class) has s1, s2,s3,s4 object  and every object has name  , where every name is diff .
#  for define every object name, mark , we use : self.name , self.mark .

# here, self.name, self.mark are :  instance attribute which is diff for every object.

#


class Student5:

    # SUPPOSE, EVERY STUDENT COLLEGE NAME IS SAME , THEN WE STORE THIS IN MEMORY JUST 1 TIME BY DECLARE HERE.

    # WHICH IS COMMON , WE CAN STORE THEM IN THIS WAY
     college_name= "ABC College"
     name ="anonymous" # class attribute
    # parameterize constructor
     def __init__ (self, name,marks):
        self.name =name
        self.marks=marks
        print("adding new")


s1=Student5("konok",92)
print(s1.name,s1.marks)

s2=Student5("ruplal",72)
print(s2.name,s2.marks)

#print college name
print( s2.college_name)
print (Student5.college_name)

# in this way , just 1 time store in memory the college name.


#============================

# TOPIC: ** METHOD
#=> Method are functions that belong to objects.
# in a class can store 2 things:
# 1. data( attribute=> properties )
#2. function or method , how work ? it explain .


#creating class

class Student6:

    # **class attribute use: ( use this when something is common for every one )
    college_name ="ABC college"
    #CONSTRUCTOR
    def __init__( self, name,marks):
        self.name= name   # obj attr
        self.marks=marks  # obj attr


    #METHOD
    def hello(self):
        print("hello")

    #method
    def welcome (self):
        print("welcome student,", self.name)

    #method
    def get_marks( self):
        return self.marks

    #method
    def get_college_name(self):
        return self.college_name

#creating OBJECT
s1 = Student6("pricila", 97)
s1.hello()  # ans: hello
s1.welcome()  #ans:welcome student, pricila
print ( s1.get_marks())  #ans: 97

# EX: class attribute.
print( s1.get_college_name())  # ans: ABC college



# why use constructor?
# ans: for initialize parameter

# ======================================
# question 1: create student class that takes name & marks of 3 subjects as arguments in constructor . Then create a method to print the average .

# ans:

class student:

    #constructor

    def __init__ ( self, name, marks):  # marks is list
        self.name= name
        self.marks=marks

    #method
    def get_avg(self):
        sum=0

        for val in self.marks:
            sum+=val
        print("hi", self.name,"your avg score is : ", sum/3)
s1= student("tony stark",[99,98,97])
s1.get_avg()  #ans:hi tony stark your avg score is :  98.0


# ==============================================
# TOPIC: STATIC METHOD.

# Method that don't use the *** self parameter .( work at class level )
#

class Student7:
    def __init__ ( self,name,marks):
        self.name=name
        self.marks=marks

    #method/ function
    # def hello():
    #     print( "hello") # it gives error, becuase not use self  paramter .

    # for solve this: we use decorator

    @staticmethod  # decorator
    def hello():
        print("in static method :ABC college")

#use @staticmethod   -> for convert normal function to static method

s1= Student7("shen watson",[23,5,99])
s1.hello()  # ans :in static method :ABC college

# what is decorator?
#ans:  Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.














#==============================
# topic: Abstraction & Encapsulation

# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation: Wrapping data and function into a single unit (object).



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