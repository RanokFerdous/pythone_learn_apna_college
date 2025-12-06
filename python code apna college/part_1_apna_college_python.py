print ("hellow world !")
print ("Apna college")

print( "hello world", "My age is 23")

# take automatic  next line python code
print(23)
print( 23 +34)
print( "23"+"34")

print ("name")

# variable
name="ranok"

print (name) # name= ranok .
print ( "my age is:  " , name)

age=23
age2=age
print( age2)

#  data type found
price=40
print( type(name))  # <class 'str'>
print(type(price))  # <class 'int'>

# ------------------------------------
age=23
old=True
a=None  # means not give any data type.

print (type(age))
print( type(a)) # <class 'NoneType'>


#input taking method

name1=input("name1: ")  # name1:  .....( give ranok)
print (name1)  #name1:ranok

# for int integer  taking as input
age1= int( input("age1: "))  #convert value input int
print( age1)

#for float input taking

newPrice =float(input ("Price: ")) # convert value in float.
print ( newPrice)

print( "My name is ",  name1,"and i am " , age1, "old. My bag price is just ", newPrice)

#======

#input 2 number print there sum

A =int( input("A: "))
B=int ( input("B: "))

print ( A, "AND", B)
print (A+B)

#WAP to input SIDE fo a square & print its area

area = float( input( "area: "))
print( "area is : ", area*area)

#WAP to input 2 floating point number & print their average

float_a =float( input( "float_a: "))
float_b=float(input("float_b: "))

print( (float_a +float_b)/2)  # give average

print( (float_a +float_b)//2)  # give integer division value


# wap to input 2 integer numbers, a and b
#print Ture if a is greater than or equal to b. if not print False

x =int( input("x: "))
y=int ( input("y: "))

if( x>=y):
    print ( "ture")
else:
    print ("false")
