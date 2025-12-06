#cheapter: 6 part_2 recursion learning

# time: 6: 38:00 to 7:04:00 time

# defination: When a function calls itself repeatedly

# print n to 1 backword
def show(n):
    if(n==-1):
        return
    print(n)
    show(n-1)


show(4)  #ans: 4 3 2 1 0 (in diff line)
#==============

def show(n):
    if(n==-1):
        return
    print(n)
    show(n-1)
    print("end")

show(4)  #ans:
#ans: 4 3 2 1 0 end end end end end

#============================
# factorial recursion

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n *fact(n-1)

print(fact(4) ) # ans: 24

# fact(4)->fact(3)->fact(2)->fact(1)
# #==================================
# recursion practice
# qs1: print n to 1 using recursion

def cal_sum1(n):
    if(n==0):
     return 0
    return cal_sum1(n-1) + n

print(cal_sum1(5))  #ans: 15

#===============
#qs2: print all element in a list using recursive function
# hint: use list & index  as parameter

def print_list(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","litchi","apple","banana" ]

print_list(fruits)

#=====================================
