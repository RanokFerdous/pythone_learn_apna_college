# CHEPTER: 4 Dictionary  and Set

# dictonary store the ( key,value) pair.
# dictonary are: unordered, mutable(changable) and don't allow duplicate keys

#*** create a dictonary

info= {
    "key" : "value",
    "name":"apnacollege",
    "subject": ["python", "c", "java"],   # that is a list
    "learning" : "coding",
    "age": 52,
    "is_adult": True,
    "marks": 94.4,
    12.32:23,
    "topic" :  ("dict", "set")   # that is a tuples
}

#print ( info)
#ans: {'key': 'value', 'name': 'apnacollege', 'subject': ['python', 'c', 'java'], 'learning': 'coding', 'age': 52, 'is_adult': True, 'marks': 94.4, 'topic': ('dict', 'set')}

print ( type( info))  #ans:  <class 'dict'>

print(info["learning"])
print(info["is_adult"])


# **** no order in dictonary , because not index has.
#=========
# dictory is : mutable becuase can change

#create dictonary
document= {"mark":95.4,  "id": 34}
# change value of keys.
document["mark"]=80.3

print(document)   # ans: {'mark': 80.3, 'id': 34}
print(document["mark"])  # ans: 80.3
print(document["id"])  # ans: 34

# to assign or add new

document["name"]="ranok"  # add a new key name
print(document)


# create null dictonary
null_dict ={}
print(null_dict)  # ans: {}
null_dict["id"]=4
print(null_dict)   #ans: {'id': 4}

#=========================
# topic : nested dictonary

student = {
    "name": "shradha",
    "subjects": {
        "chem": 98,
        "phy": 97,
        "math":95
    }
}

print( student)  # ans: {'name': 'shradha', 'subjects': {'chem': 98, 'phy': 97, 'math': 95}}

print( student["subjects"])   # ans: {'chem': 98, 'phy': 97, 'math': 95}
print(student["subjects"]["phy"])  # ans: 97


#===========
# **** DICTONARY METHOD : KEYS( ), value(), .item(), .get("key"), .update( newDict)

#1.  myDict.key( )  => return all keys
#2. myDict.values( ) => return all values
#3. myDict.items()  => return all  ( key, val) pairs as tuples
#4.myDict.get( "key") => return the key according to the value
# 5.myDict.update( newKict) => insert specified items to the dictonary

# create a dictionary
student1 = {
    "name": "shradha",
    "subjects": {
        "chem": 98,
        "phy": 97,
        "math":95
    }
}

print (len(student1) )  # ans: 2
#we can find: the length of this list

print(len(list(student1)))  #ans: 2



print (student1.keys()) #  ans:  dict_keys(['name', 'subjects'])

# NOTE : in answer dict_key (...)  are coming.
# *** we can this dict_key( )  in a list format
# list format
print( list(student1.keys()))  # ans: ['name', 'subjects']


#question: print total number of key value pair
print( len( student1))  #ans: 2
print( len( list(student1.keys())))  # ans: 2

#============value method : give only value ======================

print( student1.values())  #ans: dict_values(['shradha', {'chem': 98, 'phy': 97, 'math': 95}])
print( list ( student1.values())) # ans:  ['shradha', {'chem': 98, 'phy': 97, 'math': 95}]
# here,  we ** store  dictionary inside a list.

#  here, dictonary store in the list .

#=============== items method:  return all ( key,val) pair as tuples
print( student1.items())  # print all pair  ( key, val)
 #ans: dict_items([('name', 'shradha'), ('subjects', {'chem': 98, 'phy': 97, 'math': 95})])

# ** we can typecast it into a list
print( list(student1.items()))
 # ans: [('name', 'shradha'), ('subjects', {'chem': 98, 'phy': 97, 'math': 95})]
 # here, inside list , store 2 tuple.


pairs= list( student1.items())
print( pairs[0])  # ans: ('name', 'shradha')
print( pairs[1])  #ans: ('subjects', {'chem': 98, 'phy': 97, 'math': 95})
#==============================================
#======== .get ("key")  method : return key value
# two way :( why we use 2 ways: )

print(student1["name"])
print(student1.get("name"))

# when enter wrong
# *** print( student1["name2"])  # ans: give error . since name2 not exist
print( student1.get( "name2")) # not give error. ans:None

#=====update method :

student1.update({"city": "delhi"})  # add a new :  ( key,value) pair.
print( student1)

new_dict={ "book": "harry porter"}
student1.update( new_dict)
print(student1)  # ans: {'name': 'shradha', 'subjects': {'chem': 98, 'phy': 97, 'math': 95}, 'city': 'delhi', 'book': 'harry porter'}

#topic: ***  change  old value of key and add another key

add_update_key = { "name":"neha kumer", "age":13}
student1.update(add_update_key)  # change previous name key value.
print(student1)  #ans: {'name': 'neha kumer', 'subjects': {'chem': 98, 'phy': 97, 'math': 95}, 'city': 'delhi', 'book': 'harry porter', 'age': 13}

# *** duplicate key not store  .

#============NEXT TOPIC : SET=======
