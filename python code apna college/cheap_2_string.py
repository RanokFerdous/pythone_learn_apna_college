#Cheapter : 02  string

str1 ="this is string"
str2='ApnaCollege'
str3="""This is another string"""

# why use different type of  inverted comman or apostrpoy

#example:  'this is apnacollege's tutorial'   ( it will get confution )

#1 take new line : use escape sequence character for space, next line

str4 ="this is a string .\n we are creating it in python"
print (str4)

#2. concatanation
print( str2 +str3)

#3. length of string
print( len( str2))
final_str = str1 +" "+str2
print(final_str)


#===================================
# Topic: indexing of string

str="Apna_college"  # str[0]=A , str[2]=n
ch =str[0]
print(ch)   # A
# ******not allow  str[0]=p

print( str[1:4]) # pna   . last index can't include.
print( str[ :4])   # means: [0:4]
print( str [1: ])   # means: [1:len(str)]
print( str[ 5:len(str)])

# **special case of string . can run in backward indexing from  -5 -4 -3 -2 -1
str1="apple"
print( str1[-3: -1])  # pl

# some string function leanr
str='i am studying python from Apnacollege'
#1. str.endswith ( "ege")
print( str.endswith("ege"))  # ans :True # if correct , True , else False

#2. str.capitalize()   => capitalize the 1st letter
print( str.capitalize())  # ans: I am study....
print( str)  # ans: i am stu   ( ***not change original string)

#3 . str ( old, new)  replace old with new
print( str.replace( "o", "a")) # i am studying pythan fram Apnacallage

print( str.replace("python","javascript"))

#4.str.find( word)   # return 1st index of 1st occurance

print( str.find( 'o'))   #ans: 18
print( str.find("from"))  # ans: 21
print( str.find( "z"))  # ans: -1  ( when not find . because -1 invalid)

#5. count
print( str.count("o")) #ans: 3

# question: WAP to input user's first name and print its length

first_name= input( "enter your first name: ")
print( "first name lenght is : " , len(first_name))  # ans: 5


#question : WAP to find the occurrence of '$' in a string

str5= " i no $ so want $ what $ want $$$ $ "
print( "number of $ letter are present: ", str5.count("$"))  #ans: 7


#============================
# topic: nesting condition

age=34
if( age>=18 ):
    if( age>=80):
        print( "can not drive")
    else:
        print( "can drive")
else:
    print("cannot drive")

#practice question

#1.WAP  to check if a number entered by the user is odd or even

number = int ( input( "enter a number : "))
if( number %2==0):
    print("number is even ")
else:
    print ("number is odd")

#2. WAP to find the greatest of 3 numbers entered by the user.

a= int ( input( "enter first number a: "))
b= int ( input( "enter first number b: "))
c= int ( input( "enter first number c: "))

if ( a> b and a>c ):
    print( "a is greatest")
elif( b>c):
    print( "b is greatest")
else:
    print( "c is greatest")

#=======================
