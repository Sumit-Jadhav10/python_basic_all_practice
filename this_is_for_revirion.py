# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the secound number:"))
# Sum =num1+num2
# print(f"The sum of {num1} and {num2} is {Sum}")


# simple calculater
# print(" chose one out of this '+,-,/,*'")
# operater = (input("inter the oprater:"))
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter secound number: "))

# if operater=="+":
#     print(f"{num1} +{num2} = {num1+num2}")
# elif operater =="-":
#     print(f"{num1} - {num2} = {num1-num2}")
# elif operater =="*":
#     print(f"{num1} * {num2} = {num1*num2}")
# elif operater =="/":
#     print(f"{num1} / {num2} = {num1/num2}")
# else:
#     print("invalid details")    


# side = int(input("Enter the side of square: "))
# print("the area of square of side  ", side,"is:",side*side)

# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the secound number:"))

# avg = print(f"the avrage of {num1} and {num2} is : {(num1+num2)/2}" )

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the secound number:"))

# git = num1>num1
# print(git)

# 
# #
# # #string
# #
# 

# string = "this is only fow trying some this , and my name is,sumit sumit sumitsaumit"
# # print(string.endswith("it"))
# # print(string.startswith("this"))
# # print(string.capitalize())
# # print(string.upper())
# # print(string.replace("sumit","amit"))

# print(string.find("sumit"))
# print(string.count("sumit"))
# print(len(string))

# string = "this is only fow trying some this , and my name is,sumit sumit sumitsaumit $$$$$$"

# print(string.count("$"))
# grade = 0
# marks = int(input("Enter the marks of students:"))
# if marks >= 90 :
#   grade = "A"
# elif 90 > marks >= 80:
#     grade = "B"
# elif 80 > marks >= 70:
#     grade = "C"
# elif 70 > marks >=50:
#     grade = "D"
# elif 50> marks and marks >=0:
#     grade = "F"    
# print(grade)
# if grade==0:
#     print("invalid details")

# num = int(input("Enter the  number:"))
# if num%2==0:
#     print("the number is even")
# elif num %2!=0:
#     print("the number is odd")    
# elif num ==0:
#     print("the number is zero")
# else:
#     print("invalid details")    


# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# num3 = int(input("Enter the third number:"))
# if num1>num2 and num3:
#     print( num1," is greater")
# elif num2>num3:
#     print(num2,"is greater")   
# else:
#     print(num3,"is greater")    

# num = int(input("Enter the  number:"))
# if num%7==0:
#     print("the number is multiple of 7")
# else:
#     print("the number is not multiple of 7 ")    

# 
# #
# # #list
# #
# 

# list = [14,897,67,34,7,87,367,976]
# # list.append(12)
# # print(list)
# # list.sort()
# print(list)
# list.sort(reverse=True)
# # print(list)
# list.reverse()
# list.insert(1,9)
# # print(list)
# list.remove(14)
# list.pop(3)
# print(list)
# by=list[1:4]
# print(list[1:4])
# print(by)

# 
# #
# # #tuple
# #
# 

# tupl=(23,678,98,9,1,875)
# ar=tupl.index(9)
# print(ar)
# print(tupl.count(9))

# a = input("Enter the first movie name:")
# b = input("Enter the secound movie name:")
# c = input("Enter the  third movie name:")
# list = []
# for i in 
# list.append(a)
# list.append(b)
# list.append(c)
# print(list)

# number =int(input("Enter the number of movie name  you wanted to enter : "))
# list=[]
# for i in range(1,number+1):
#     i = input("Enter the movie name:")
#     list.append(i)

# print(f"you enter {number} movie :{list} ")

# list = [1,2,3,4,4,3,2,1]
  
# if list== list.reverse(): 
#     print("it is pdram")
# else :
#     print("it is not pdram")  

# lst = [1,2,3,4,4,3,2,1]

# copied = lst.copy()
# copied.reverse()

# if lst == copied:
#     print("it is pdram")
# else:
#     print("it is not pdram")

#     lst = [1,2,3,4,4,3,2,1]

# if lst == lst[::-1]:
#     print("it is pdram")
# else:
#     print("it is not pdram")

# tub = ("A","A","D","F","D","A","B","B","C","D")
# print(tub.count("A"))

# tub = ["A","A","D","F","D","A","B","B","C","D"]
# tub.sort()
# print(tub)
# my_self={"name":"sumit","marks":{"maths":23,"science":29,"hindi":18}}
# # print(my_self.values())
# # my_self.update({"roll_number":18})
# # print(my_self)
# a=my_self.get("name")
# print(a)

# 
# #
# # #set
# #
# 

# die ={1,3,4,5,3,2,4,5,7,}
# number = {1,4,4,5,6,4,2,3,5,2,211}
# # die.add(25)
# # print(die)
# # die.remove(25)
# # print(die)
# # die.pop()
# # print(die)
# # die.clear()
# # print(die)
# sum =die.union(number)
# # print(die.union(number))
# print(sum)
# sume=die.intersection(number)
# print(sume)

# lists = {"table" : "a piece of furniture", "list of facts & figures"
# "cat ": "a small animal"}
# print(lists)

# sets ={"python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"}
# print(sets)

# subject = input("enter the subject:")
# marks =input("enter the marks:")
# subject2 = input("enter the subject:")
# marks2 =input("enter the marks:")
# subject3 = input("enter the subject:")
# marks3 =input("enter the marks:")
# des={}
# des.update({"subject":"marks"})
# des.update({"subject2":"marks2"})
# des.update({"subject3":"marks3"})
# print(des)

# subject1 = input("enter the subject: ")
# marks1 = input("enter the marks: ")

# subject2 = input("enter the subject: ")
# marks2 = input("enter the marks: ")

# subject3 = input("enter the subject: ")
# marks3 = input("enter the marks: ")

# des = {}

# des.update({subject1: marks1})
# des.update({subject2: marks2})
# des.update({subject3: marks3})

# print(des)

# s = {9, "9.0"}
# print(s)



# 
# #
# # #loops
# #
# 
# i=1
# while i<=100:
#     print(i)
#     i+=1
# print("The program is execute")

# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("The program is executed")

# num =int(input("enter the number you wanted:"))
# i =1
# while i <=10:
#     print(num*i)
#     i+=1
    

# i =1
# while i <=10:
#     print(i**2)
#     i+=1

# i =1
# while i<=100:
#     if (i**0.5).is_integer():
#         print(i)
#     i+=1    
 
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num=int(input("Enter the number you wanted:"))
# for i in nums:
#     if i==num:
#         print(" found it the tuple")
#         break
# else:
#     print("not found it the tuple")

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num =int(input("Enter the number you wanted:"))
# for i in nums:
#     if i==num:
#         print("found the number you wanted")
#         break
# else:
#     print("not found the number you wanted")

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int(input("Enter number to search: "))

# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("Found at index", i)
#         break
#     i += 1
# else:
#     print("Not Found")

# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)
# num  =int(input("Enter the value the multaple table you wanted:"))
# for i in range(1,11):
#     print(num*i)

# num  =int(input("Enter the value you wanted:"))
# sum =0
# i=1
# while i<=num:
#     sum +=i
#     i+=1
# print(f"the sum of  first{num} natural number is {sum}")    

# num = int(input("Enter the number you wanted :"))
# factorial = 1
# for i in range(1,num+1):
#     factorial*=i
# print(f"the  factorial of  {num}   is {factorial}")    

# count =0
# num = int(input("Enter the number you wanted :"))
# for i in range(1,num+1):
#     if num%2==0:
#         count +=0
#     elif num%i==0:
#         count +=0
#     else:
#         count +=1 
# if count ==0:
#     print(f"{num} is not a prime number ")  
# elif count==1:         
#     print(f"{num} is  a prime number ")        

# count = 0
# num = int(input("Enter the number: "))

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
# num = int(input("Enter a number: "))

# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reversed number:", rev)

num = int(input("Enter number: "))

original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")