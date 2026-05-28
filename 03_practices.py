# number = [1,2,3,4,5,3223,-123,9874]
# sum = max(number)
# print(sum)
# sum = min(number)
# print(sum)
# number.reverse()
# print(number)
# # number.count(5)
# print(number)



# for i in number :
#    if  i%2==0:
#     print(i)

# number.append(234)
# print(number)
# print(number)
# number.remove(1)
# print(number)

# factorial 
# n = int(input("enter the number:"))
# facter = 1
# square = []

# for i in range(1,n+1):
#    facter = facter*i
#    square.append(facter)  
# print(f"The list of factorial  through {n} is {square} ") 
# square.append(facter)   
# print(f"And the factorial of {n} is : {facter}")

# sum
# n = int(input("enter the number:"))
# sume = 0
# list = []

# for i in range(1,n+1):
#    sume = sume+i
#    list.append(sume)  
# print(f"The list of factorial  through {n} is {list} ") 
# list.append(sume)   
# print(f"And the factorial of {n} is : {sume}")
# tuple = (1,2,43,55,6,6,77,6,55,4,4,44,33,5,634,44,3,4,4,6,5,4,4)

# if len(tuple) == 23 :
#     print(tuple)
#     print(len(tuple))
#     print(tuple.index(43))
#     print(tuple.count(4))
#     print(tuple[3])
# tuple_list = list(tuple)
# print(tuple_list)
# print(max(tuple))    
# print(min(tuple))    
# marks = {"sumit":98,"amit":30,"subham":99,"dipak":67}
# for name,mark in marks.items():
#    if mark >=90:
#     print(name,mark)
#     # a = marks.update["mit":43]
# marks["amitt"]=78
# print(marks)

# school = {"amity":58,"sujmit":87,"jit":63,"anushak":74,"pippo":35,}
# school["kol"]=99
# print(school)

# word = input("ENTER THE CHARACTER")
# freq = {}

# for ch in word:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)
# word = input("ENTER THE CHARACTER")
# freq ={}
# for ch in word:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch] =1
#         print(freq)


# countries = {
#     "India": "New Delhi",
#     "USA": "Washington",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Germany": "Berlin"
# }

# for country in countries:
#     print(country)
# print(list(countries.keys()))
# print(list(countries.values()))
# print(list(countries.items()))
# # countries.update["amit":8]
# print(countries)
# amit ={"amit":"new"}
# countries.update(amit)
# print(countries)


# set = {1,2,3,4,5}
# print(set)
# print(type(set))
# print(type(list(set)))
# set.add(45)
# print(set)


# list1 = [1, 2, 2, 3, 4, 4, 5]
# unique = set(list1)
# print(unique)
# even = set()

# for i in range(1, 21):
#     if i % 2 == 0:
#         even.add(i)

# print(even)



# for i in range(1,11):
#     print(i)
# i = 1
# while i<=10:
#     print(i)
#     i+=1

# for i in range(10,0,-1):
#     print(i)
#     i = 10
# while i>=0:
#     print(i)
#     i -=1

# for i in range(1,21):
#     if i %2==0:
#         print(i)
# i = 0
# while i <=20:
#     if i%2==0:
#        print(i)
#     i +=1  


# for i in range(1,21):
#     if i %2!=0:
#         print(i)     
# i = 0
# while i <=20:
#     if i%2!=0:
#        print(i)
#     i +=1    
   
# n = int(input("Enter the number:"))
# for i in range(1,11):
#     print(i*n)

# n = int(input("Enter the number:"))
# i = 1
# while i <=10:
#     print(i*n)
#     i +=1

# n = int(input("Enter the number :"))
# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)

# for i in range(1,51):
#     if i %5==0:
#         print(i)

# i = 1
# while i <=50:
#     if i %5==0:
#         print(i)
#     i +=1 

# n =int(input("enter the numbe:"))
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

# i = 1
# factorial =1
# n = int(input("Enter the number:"))
# while i <=n:
#     factorial*=i
#     i +=1
# print(factorial)
# n = int(input("Enter the number:"))
# count = 0
# while n !=0:
#     n= n //10
#     count+=1

# print(count)

# n = int(input("Enter the number:"))
# reverce = 0
# while n !=0:
#      digit = n%10
#      reverce =reverce*10 + digit 
#      n = n//10
# print(reverce)

# num = int(input("Enter a number: "))
# temp = num
# rev = 0

# while num != 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# n = int(input("Enter the number:"))
# temp = n
# reverce = 0
# while n !=0:
#     digit = n%10
#     reverce=reverce*10 + digit
#     n=n//10
# if temp == reverce:
#     print(f" {temp} is a palidrome")
# else:
#      print(f" {temp} is not palidrome")



# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c
# for i in range (1,6):
#     print("*"*i)

# for i in range (5,0,-1):
#     print("*"*i)


# for i in range (1,6):
#     print("*"*i)

# for j in range (4,0,-1):
#     print("*"*j)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()    