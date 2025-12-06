#cheapter: 07 File i/o in python

# Python can be used to perform operation on file.

# (read & write data)
# RAM: ( all code , create variable create here,
# RAM is volatile, not memorize,
# **if we want to store or save data or code , then we use ** file. using file, for store data in long term. )

#types of all files:
#1. Text files: .txt, .docs, .log
# 2.Binary Files: ( store data another format ,but not in binary form )
# example:  .mp4, .mov, .png, .jpeg
# video file: .mp4 and .mov

#** here , we learn ,: how can we open,read, write, re-write ,delete a file ?

# NOTE: ** all file are at last store in : 0 1 format.

# file are store in : ssd or hdd

# operation 1:  open , read , close file
# we have to open a file before reading or writing.

#  f =open ("file_name","mode")

#mode can be: r, w (r: read, w:write)

# by default: read mode

# crate demo.txt file

#open file:
f =open("demo.txt","r")
data= f.read()

print(data)

print(type(data))  # string
#close the file
f.close()

#=====================

# diff mode of operation

# 'r'   open for reading ( default)
# 'w'  open fo writing ,truncation the file first. ( : all previous text will be deleted and new text will be stored here.)

# 'x'  : create a new file and open it for writing.

# 'a'  : open for writing, appending to the end of the file if it exists  ( add more data with exist data)

# 'b' : binary mode  ( when ** we want to open a binary file )
# 't' : text mode (default)
# '+' : open a disk file for updating ( reading and writing.) NOTE: use '+' for 2 operation at a time.


# NOTE: ** HERE, f= open("demo.txt","rt")

#here, rt place we can write just: r for  text file
# rb :  for binary file
# wb: for open and write in binary file.
#

# ( r+ ) , (w+ ) -> means :  read and write in file

# a+  -> data append and read the file.

# NOTE:   data = f.readline()  # read 1 line at a time.

# text file:
# I am learning python file
# input and output

#  qs1:  we want print 1st 5 letter

f=open( "demo.txt","r")

data= f.read(5)  # read 1st 5 letter
print(data)  # ans: i am

line1=f.readline()
#ans: the remaining part of 1st line , after print the 1st 5 letter.
print(line1)

# print 2nd line
line2= f.readline()
print(line2)  #input and output

# NOTE: between a file open and file close part:
#  which part is read once, these part will not be read 2 time until you close and reopen the file.
# every time file will be read from the previous read files next txt character.

f.close()


# ==================================
# topic: writing to a file

# "w"  : overwrite mode: delete the previous txt.

f=open("demo.txt","w")
f.write(" i want to learn python oops today")
f.close()

# now , demo.txt file:  i want to learn python oops today

#============================
# topic:  "a"  mode,  ( add new txt with existing txt)

f= open("demo.txt","a")
f.write("\nnow i add append mode here.\n ok ")
f.close()

#=============================
# topic: create new  txt file
# if file not exist , automatic create that file

f=open("sample.txt","w")
f.close()
# when run program : automatic create sample.txt file.

f=open("append.txt","a")
f.close()

# o/p: create append.txt file if not exist.

# ===============================

# go to this line stack overflow for learn file handling: https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

# truncate:  means: delete( previous) data from file

# r+ : read and write.  ( **not truncate. override : means: replace the previous letter with new letter corresponding with index value)
# w+ : read and write.  ( truncate file: previous data delete.)

#============================================

f=open("demo.txt","r+")

# now demo.txt file has:
#  i want to learn python oops today
# now i add append mode here.
#  ok

f.write("abc ")
f.close()

# now , demo.txt file o.p:
# replace
# abc ant to learn python oops today
# now i add append mode here.
#  ok

# ================

f= open("demo.txt","w+") # it delete all data form file

print(f.read())
f.write("abcdef")
f.close()

#ans: in demo.txt:  abcdef  .

#=====================

f= open("demo.txt","a+")

# append new txt in demo.txt
print(f.read())
f.write("abcdef")
f.close()


# r+   = can read and override existing data, pointer from the start , ( no truncate)

# w+  =  read + override ,  ( truncate : delete all data from demo.txt file )

#  a+  = read + append data . ( pointer from end . not truncate. )

#============================

# with syntax :

# file open  and read data

with open("demo.txt","r") as f:
    data=f.read()
    print(data)

# NOTE: ** with syntax: automatically close the file .

#===========================

# open in write mode:  ( "w" mode : truncate file)

with open("demo.txt","w") as f:
    f.write("new data")

# ans: demo.txt: new data
#==============

# TOPIC: DELETE OPERATION

# FOR DELETE OPERATION : WE HAVE TO USE: OS MODULE
# what is module?
#ans: module ( like a code library) is a file written by another programmer that generally has a function we can use.

# module:  is code library.

import os

# import tensorflow   # it give error , we have to install this for use .

# for install transorflow we have to write:
# pip3 install tensorflow

os.remove("append.txt")

# delete this file .

#============================

#practice question

# qs1: create a new file "practice.txt" using python. add the following data in it: Hi everyone
# we are learning File I/o    using java  i like programming

with open ("practice.txt","w") as f:
    f.write(  "Hi everyone \nwe are learning File I/o\n    using java  \ni like programming\n")

# qs2: WAF that replace all occurance of "jave" with "python" in above file

# step 1: read the data and replace in data

with open("practice.txt","r") as f:
   data = f.read()
# data is string , so use replace method in string

   new_data = data.replace ( "java","python")
   print(new_data)

# step 02: write in file the new data

with open("practice.txt","w") as f:
    f.write(new_data)


# qs3: search if the word "searching" exists in file or not
# ans:

# step 1:  read all data

word="learning"
with open("practice.txt","r" ) as f:
    data= f.read()
    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")

#ans: found , because learning is exist .
#=============

# writing this using function :

def check_for_word ():
    word="learning"
    with open("practice.txt","r" ) as f:
        data= f.read()
    if (data.find(word) != -1):
    # if( word in data):   it also can write
        print("found")
    else:
        print("not found")

check_for_word()  # call the fnx.

#==========================

#qs1: "WAF " to find in which line of the file does the word "learning" occur first. print -1 if word not found.

# ans:

# now , we read line by line :

def check_for_line():
    word ="learning"
    data=True
    line_no=1

    with open("practice.txt","r") as f:

        while data:  # till data is exist or valid
            data = f.readline()
            if( word in data):
    # means: if word is exist in data ,
                    print(line_no)  # ans: 2
                    return
            line_no+=1

    return -1   # not exist .

print(check_for_line())

#=====================
# qs 2:  from a file containing numbers separated by comma, print the count of even numbers.

#ans:

# step 1:  practice.txt file : wrtei some data:
# 1,2,76,84,90,101


# step 02: open file and read



# step 3: indivisual number find : from string
# step 04: parse/ casting to int value

# we can use : split method : for: find indivisual number from a string.

with open("practice.txt","w") as f:
    f.write("1,2,76,84,90,101")

# without method
with open ("practice.txt","r") as f:
    data= f.read()
    print(data)

    num=""
    for i in range(len(data)):
        if(data[i]==","):
            # print(num)
            print(int(num))  # typecast
            num=""
        else:
            num+=data[i]

#ans: print all indivisual number using these basic code.

#with split

with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    #ans:1,2,76,84,90,101

    nums= data.split(",")
    # comma (,) is separator , on this basic we find all number .
    print(nums)
    #ans: ['1', '2', '76', '84', '90', '101']

    # now typecast in integer


# check odd or even

count =0

with open("practice.txt","r") as f:
    data=f.read()

    num= data.split(",")
    print(num)

    for val in num:
        if(int(val)% 2==0):
            count+=1
print(count)  # ans: 4

#===========================
