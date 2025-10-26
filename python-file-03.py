"""
chapter5 = "welcome to chapter 3"
print(chapter5)
"""

#Chapter .5️⃣
#LOOPS 
"""
i = 1 
while i <= 5:
    print(i,"rashuu bhatt")
    i += 1
"""

#Print no.s from 5 to 1
"""
i = 5
while i >= 1:

    print(i)
    i -= 1

print("loop ended")
"""

#h/w Q: 
"""
nums =[1,2,9,16,25,36,49,64,81,100]
idx = 6
while idx < len(nums):
    print(nums[idx])
    idx += 1
"""

#Q.print the nultiplication table of any no. n ?
"""
n = int(input("enter number :"))
i = 1 
while i <= 10:
    print(n*i)
    i += 1 
""" 

#Q.print the elements in the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
"""
i = 1
while i <= 10:
    print(i*i)
    i += 1
"""
#initiallisation 
"""
nums = (1,4,9,16,25,36,49,64,81,100)  #tupple
x = 25
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx",i)
        break
    else:
        print("finding...")
    i += 1
"""

#BRAEAK AND CONTINUE...
#Break ...
"""
i = 1
while i <= 10:
  print(i)
  if(i == 3):
   break
  i += 1
print("end of the loop")
"""
#continue ...
"""
i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue   #skip
    print(i)
    i += 1
"""
#for looop 
"""
str = "rashubhatt"
for char in str:
    if(char == 'b'):
        print("found b")
        break
    print(char)
"""

#print el of the following list using loop ??
"""
nums = [1,4,9,16,25,36,49,64,81,100]
for el in nums:
  print(el)
"""  

#Search a no. x in this tupple using loop??
"""
nums = (4, 9, 16, 25, 36, 49, 64, 81, 100,49)
x = 49
idx = 0      
for el in nums:
 if(el == x):
     print("number is found at idx", idx)
     break
 idx += 1
"""

#range function 

# for i in range(5):  #but no. khud include nahi hoga
#     print(i)

# for i in range(2, 5): # first include, last not 
#  print(i)

# for i in range(2, 10, 2): #(start, stop, step)
#  print(i)


#Q. print all even no.s upto 20?

#for i in range(2, 20, 2):    #if we start from 1 we get odd no's
#print(i)

#print no. from 100 to 1??
"""
for i in range(100, 0, -1):
    print(i)
"""

#multiplication table of any no. ?
"""
n = int(input("enter number :"))
for i in range(1, 11):
    print(n * i)
"""

#PASS STATEMENT ...
"""
for i in range(5):
    pass                   #if u doesn't want to write something 
print("some usful work ")  #inside for loop u can use pass st. 
"""                           #this means skip (if not use this , we got error)
                           #hum bad mein ja k pass ke jhaga code likh sakthe hai ...

#Q.WAP to find the sum of first n no.s(using for or while loop )?
#Q.WAP to find the factorial of first n numbers(using while loop)?

#CHAPTER : 6
#FUNCTIONS & RECURISION 

#(1).FUNCTIONS 
"""
def calc_sum(a , b):
    sum = a+b
    print(sum)
    return sum

calc_sum(10 , 5)
calc_sum(28 , 30)
"""
#calculate the avg of 3 no.s ?
"""
def calc_avg(a ,b ,c):
    avg = (a+b+c)/3    
    print(avg)
    return(avg)

calc_avg(10,20,25)
calc_avg(1,2,3)
"""
"""
def cal_product(a ,b=3):   #non default value huumseha bas mein ayega 
    print(a*b)
    return a*b
cal_product(2)
"""
#Using functions...
#Q.1:WAP to print length of a list.(list in parameter)
"""
cities = ["srg", "del", "bho", "hr","bng"]
heroes = ["ronaldo", "Shoaib akther", "waseem akram","sachin tandulkar"]

print(heroes[0])
print(heroes[2])

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
    

print_len(cities)
print_len(heroes)
"""
#Q.2:WAP to print the elements of a list in a single line.(list in paramwter)?
"""
list1 = [12,23,34,11,46,56,75,20]
def print_list(list1):
    for item in list1:
     print(item , end=" ")

print_list(list1)
"""
#Q.3: WAP to find the factorial of n (n is the parmeter)
"""
def cal_fact(n):
    fact = 1 
    for i in range(1 , n+1):
        fact *= i
    print(fact)

cal_fact(5)
"""
#Q.4: WAP to convert USD in INR ??
"""
def cal_usd(usd_val):
    inr_val = usd_val*83 
    print(usd_val, "USD =", inr_val, "INR")

cal_usd(2)    
"""
#Q.H/W :-take input from user to show a no. is even or odd??


#RECURSION...
#recursive function:no.s from n to 1 ??
"""
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)
"""
#WAP to find the factorial of n by using recursions ??
"""
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1)*n     # n*(n-1)!

print(fact(5)) 
"""
#LET'S PRSCTICE...
#Q. write a recursive function to cal sum of first n nstural no.s?
"""
def cal_sum(n): 
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(5)
print(sum)
"""
#Q. write a recursive fun to print all the elements in a list?