#cheapter:8 part_4 Polymorthism
# time: 9:30:00
#topic: 1: polymorphism

#explain: when the same operator is allowed to have different meaning according to the context.

#poly->means: many   morphism: form
# means:  many form

# HOWEWORK: ******getter and setter  decorator.

# operators & Dunder fnx
#  a+b       =>

print(1 +2)  #ans: 3
print(type(3)) #ans: <class 'int'>
print("apna" +"college") #ans: apan college
#here,overloadding happen: using + operator

print(type("apna")) #ans: <class 'int'>

print([1,2,3] +[4,5,6]) #merge ,
#ans:[1, 2, 3, 4, 5, 6]

#here,both 3 case : operator overloadding happen.  => that is type of polymorphism.

print(type([1,2,3,4]))  #ans: <class 'list'>

# upper all are implicit using :in python ,

#====================================
#=now ,WE LEARN HOW TO USE THE UPPER CONCEPT IN CLASS IN PYTHON

#TOPIC: POLYMORPHISM : OPERATOR OVERLOADING .
#COMPLEX NUMBER:   3i +4j ,  2i+9j
#complex number: use in voice recognization .

#create Complex class which can create complex class

class Complex:
    def __init__(self,real,img):
        self.real =real
        self.img =img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

# add 2 complex number
    def add(self,num2):
        newReal =self.real +num2.real
        newImg =self.img +num2.img
        return Complex (newReal,newImg)




num1= Complex(1,3)
num1.showNumber()  # 1i + 3j

num2 = Complex(3,5)
num2.showNumber()  # 3i +5j

#***dunder fnx :  double underscore use :
#add
num3 = num1.add(num2)
# i can't write : num3 =num1 +num2  here. for using this ,i have to use dunder fnx.
num3.showNumber()  # 4i +8j





#===================================
#QS1: but i want to use : num1 +num2 for addition
#ans: for this , i have to use: dunder fnx.

class Complex1:
    def __init__(self,real,img):
        self.real =real
        self.img =img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

# using dunder fnx: substract  2 complex number
#  __sub__   this is dunder fnx :
    def __sub__(self,num2):
        newReal =self.real -num2.real
        newImg =self.img -num2.img
        return Complex1 (newReal,newImg)


num1= Complex1(1,3)
num1.showNumber()  # 1i + 3j

num2 = Complex1(3,5)
num2.showNumber()  # 3i +5j

#***dunder fnx :  double underscore use :
# for using dunder fnx , we can use : the below simple line for addition , multiplication, substraction , modulus and so on .
num3 = num1 -num2
num3.showNumber()  # -2i + -2j

#==========================
# **** more dunder fnx EXAMPLE

# a* b      use : __mul__
#a/b        use: __truediv__
#a%b        use: __mod__

# __XOR_ , __and__, __or__,
# in documentation , i can find more dunder fnx.
#===================================


#TOPIC: QS1: PRACTICE QUESTION ON OOPS
# QS1: Define a Circle class to create a circle with radius r usingconstructor
#->Define an Area() method of the class which calculates the area of the circle .
#-> Define a Perimeter() method of the class which allows you to calculate the perimeter fo the circle

#solve:

class Circle:
    def __init__(self,radius):
        self.radius =radius

    def area (self):
        return (22/7)* self.radius**2

    def perimeter (self):
        return 2*(22/7)*self.radius

c1 =Circle(21)
print(c1.area())
print(c1.perimeter())

#=================================

#QS 2: Define a Employee class with attribute role, department, salary. this class has  showDetails() method
#=> Create an Engineer class that inherits properties from Employee & has additional attribute name & age .

class Employee:
    def __init__(self, role, dept,salary):
        self.role =role
        self.dept= dept
        self.salary= salary
    def  showDetails(self):
        print("role :",self.role)
        print("dept:",self.dept)
        print("salaray: ",self.salary)

class Engineer (Employee):
    #name and age attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)  #ans:Elon Musk
        print(self.age) #ans:40
        super().__init__("Engineer","IT","75000")



e1 = Employee("accountant","Finance","50000")
e1.showDetails()
#ans:role : accountant dept: Finance salaray:  50000
engg1 = Engineer("Elon Musk",40)
engg1.showDetails()
 #ans:  role : Engineer dept: IT salaray:  75000

#==============================

#QS3: Create a class called Order which stores item & its price

# Use Dunder fucntion __gt__() to convey that:
# order1 > order2  if price of order1> price of order2

#ans:

class  Order:
    def __init__( self, item, price):
        self.item= item
        self.price =price
    #use dunder fnx: a>  __gt__
    def __gt__ ( self,order2):
        return self.price >order2.price
#NOTE: here, self is indicate the order1 obj.

order1= Order("chips",23)
order2 =Order("tea", 10)

print(order1>order2) # ans: True