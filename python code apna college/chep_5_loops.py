#cheapter: 05 Loops in python language.

# while True:
#     print("hello")
# ** here, hello will be print infinite time, never stop.

# ===============
# ques: print hello 5 time using while loop

count=1

while count <=5 :
    print("hello")
    count +=1


print( "ok")

# let's practice
# ques 01: print number from 1to 100 and 100 to 1
# 2. print multiplication table of a number
# 3. print element of the following list uisng loop:
# [ 1,4,9,16,25,36,49]
# 4. Search  for a number x in this tuple using loop :
#  [ 1,4,9,16,25,36,49]

#  qs 1 :

i =1
while i<=10:
    print (i)
    i+=1

#qs: 02
j=1
while j<=10:
    print(j*3)
    j+=1

#qs : 03

nums =[ 1,4,9,16,25,36,49]
idx =0
while  idx <len(nums):
    print(nums[idx])
    idx+=1

#qs: 04 search

nums1 =[ 1,4,9,16,25,36,49]

x=36

i=0
while i<len(nums1):
    if( nums1[i]==x):
        print("Found at idx:", i)  #Found at idx: 5
    else:
        print("finding..")
    i+=1

#===============
# topic: break and continue topic learn here.
# break :

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print( "end of loop ")

# ans: 1 2 3
x=1
while x<=5:

    if(x==3):
        x+=1
        continue
    print(x)
    x+=1

print( "end of loop ")

#ans: 1 2 3 4

# ===============================

#topic: Loops in Python

# Loops are used for sequential traversal. For traversing list, string tuples etc.


nums = [1,2,3,4,5]

for val in nums:
    print( val)

veggies =["potota", "brinjal","ladyfinger","cucumber"]

for val in veggies:
    print(val)


# tuple print using for loop

tup= ( 1,2,3,4,5,6,7,88)

for num in tup:
    print(num)

print("end of loop")

# print each character
str ="apna"

for char in str:
    print(char)
else:
    print("end")

# print each character indivisually
#=============================
str ="apnacollege"

for char in str:
    if( char =='o'):
        print("o is found")
        break
    print(char)

print("end")

# ===========================

# qs1: 1:  print the element of the following list using loops:
# [1,4,9,16,25,36,49,64,81,100]

# qs 2: Search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]

# ans: qs1:

# create a list
nums= [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print( el)

# search:
idx =0
x=49
for el in nums:
    if( el==x):
        print ( "number is found at idx",idx)
    idx+=1

#===========================

# topic: range function

# what is range function  ?
#ans: Range function return a sequence of numbers, starting from 0 by default, and increments by 1 ( by default), and stops before a specified number.

# range (start ? , stop, step? )
# step means: every time increasing

for el in range(5):  # range( stop ) condition
    # ans: 0 1 2 3 4
    print(el)

for el in range( 1,5):  # range(start,stop) condition,
    #step : 1 is bydefault .

    # ans: 1 2 3 4
    print (el )

# stop before value : 5

for  el in range ( 1,5,2):  # range( start,stop, increament)
    #ans: 1 3
    print(el )

# here , also stop before  5

#========================================

# qs: print all even from 2 to 20

for i in range( 2, 21,2):
    print(i)
print ("end")

# =========================
# practiec qs using:  for and range ()

#qs 1: print from 1 to 100
#qs 2: print from 100 to 1
# qs 3: print the multiplication table of a number n

# ans: qs1:

for i in range ( 1,51):
    print( i)
print( "end")

for j in range ( 50,0,-1):
    print(j)
print( "ok. ")

# qs 3:

for k in range ( 1,11):
    print(k*4)
#====================

# topic: Pass statement:   *** not doing anything
# defination : pass is a null statement that does noting . It is used as a placeholder for future code.

# *** why  need this ?

for i in range(5):
    pass

print( "some useful work ")

# why use pass key ?
# ans: use pass key , when we don't work anything.
# we can work here, when need to work . now , not work , so use pass.
# also , in try case section we can use it.

#===============================

# qs1: WAP to find the sum of 1st n number ( using while )

i=1
n=5
sum=0
while i<=n :
    sum+=i
    i+=1

print ( "sum=",sum)


n=5
sum=0
for i in range( 1,n+1):
    sum+=i

print("total sum =",sum)  # ans: 15

#===========================

# qs 2 : find factorial of first n numbers

sum2=1
for i in range( 5,1,-1):
    sum2*=i
print ( sum2 )  # ans: 120

