# Topic : set  in python
#4:34:00
# what is set?
#ans: set is a collection of the unordered items.
# Each element in the set must be unique & immutable( not change ).

collection3 ={1,2,3,4}
print(collection3)
print(type(collection3 ))  # <class 'set'>
# set is unordered . not allow duplicate. always unique

document ={ 1,2,4,2,2, "hello", "world","world"}
print( document) # ans: {1, 2, 'hello', 4, 'world'}
print ( len(document)) # ans: 5

# *********vvvvvvvviiiiiiiippppppppp
# create empty set
coll ={ }  # this is dictory type
print( type(coll))  # *****<class 'dict'>

# create an empty set.
collection1= set ()  # this is an empty set.
print( type( collection1))  # <class 'set'>

#=====================set method ==================
# 1. set.add(el)   =? add an element
#2.set.remove(el)  =? remove the element
#3.set.clear()  =? empties the set
#4. set.pop()  =? removes a random value

# NOTE:  set  -> mutable   , but  set element => immutable
# ( so ***  set.add  a we can pass -> tuple ,but not can pass the dictonary and list).

collection  =set()  # declare as an empty set
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)  # ans: {1 ,2}

# remove
collection.remove( 1)   # if element 1 is not exist give error : key error .
print(collection)  # ans: {2}

collection.add("apnacollege")
collection.add((1,2,3))  # add a tuples.
# important below topic:

# collection.add([1,2,3])  # this gives error . because list can't add.
# because list is an unhashable type "list "  . what is the meaning  ?
# ans:  which value are immutable ( not changeable , ) these value can add in set , because  we can create there hash table. ( hash table => where we change there original value to another value using hashing.  )

#  suppose , we have  1,2,4,1,4 . here, both 1 have the same hashing value which indicate the unique.
# but , in set [1,2] and [1,2,3] , if we change any set value , there hash value will be change .so can't use set.
#  here,   variable assign value can't change in lifetime. same as , hash value not change.

# remember: *****
# unhashable ( immutable=>can be change)=> dictonary, set, list
# =========================================

collection4=set()
collection4.add(1)
collection4.add(2)
collection4.add("apnacollege")
collection4.add( (1,2,3)) # add a tuples
print( len(collection4))   # ans: 4

# clear method
collection4.clear()  # ans:
print( len(collection4))  # ans: 0

#==============
collection5 ={ "hello","apnacollege","world","coding","pytho" }

# pop method
print(collection5.pop()) # pop  randomly any value
print(collection5.pop())

#======================
#set union and intersection
set={1,2,3}
set2={ 3,5,4}
print(set.union(set2))  #ans: {1, 2, 3, 4, 5}

print( set)  # ans: {1, 2, 3}
print( set2) # ans: {3,4,5}

print( set.intersection (set2)) #ans: 3
#======================
# we can store in set: boolean, int, float, str, tuples,
# but can't store  list, dict.
# practice question

#QUESTION: 1:  Store following word meanings in a python dictONARy:

dictionary = {
    "cat":"a small animal",
    "table": [ "a piece of furniture", "lists of fact"]
}
print ( dictionary)

# question : 2: How many classroom are needed by all student.? for each subject need 1 classroom .
subjects = { "python","java","python","javascript", "java", "python","java", "c++","c" }  # take as a set

print( len( subjects))  # ans: 5

#===============update method use ================
#question: 03 :  enter 3 subject from users in dictonary. start with an empty set and add one by one. subject name ans key

marks={}  #  empty dictionary
x=int ( input( "enter phy : "))
marks.update ({ "phy" : x})  # method for using update method.
x= int ( input( "enter math : "))
marks.update({"math" : x})
x= int( input( "enter chem :" ))
marks.update( {"chem" : x})
print( marks) # ans: {'phy': 43, 'math': 24, 'chem': 5}

# question: 4: Figure out a way to store 9 and 9.0 as separate values in the set . ( You can take help of built-in data types)

#ans: can store in set { 9, 9.0}
# without other built in function write set
values ={ 9,9.0, 8, 8.34}
print( values)  # ans: {8, 9, 8.34}
# for answer : the possible solution are : using string.

values1={ 9, "9.0"}
print( values1)   #ans: {9, '9.0'}
#another way use : tuples
values2= { ( "float",9.0),    ("int",9 )}  # ans:
print( values2)  #ans( for tuples): {('float', 9.0), ('int', 9)}
#===================================
