# a = input("enter the name ")
# b = a.upper()
# print(a.count("A","E","I","O","U"))
# print(len(a))


# Input string from user
text = input("Enter a string: ")
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count = count + 1

print("Number of vowels:", count)

name = input("enter your name :")
print(name.startswith("A"))

# name = input("enter your name :")
# # name_upper = name.upper()
# # names = name_upper.startswith("A")
# for char in name:
#     if char in "aA":
#          print("its start witrh A ")
#          break

#     else :
#          print("it not start with A ")
#          break
#

# text = input("Enter a string: ")
# reverse = text[::-1]
# le  = text[1:4]
# print(le)
# print("Reversed string:", reverse)

# text = input("Enter a string: ")
# word = text.find("python")
# print(word)

# text = input("enter the text:")
# words = len(text)
# if words > 10:
#     print("it contain more than 10 words")
# else:
#     print("it did not  contain more than 10 words")    


# passwords = input("Enter the password :")
# words = len(passwords)
# if words > 8:
#     print("the passwords is strong")
# else:
#     print("the passwords is weak ") 


# word = input("Enter the word :")
# words = len(word)
# if words > 0:
#     print("the input is not  empty")
# else:
#     print("the input is  empty ") 

# text = input("Enter the email :")

# if text.endswith("sumit")  == text.startswith("sumit"):
#     print("ends and start is same")
# else :
#     print("ends and start is not  same")
        
# text =  input("enter the words")
# works = text.count("$")
# print(works)

# text =  input("enter the words:")
# works = text.isdigit()
# print(works)

# text =  input("Enter the words : ")
# if text  == text.upper():
#     print("in contain uppercase")
# else:
#     print("it did not contain upper case")    

# text =  input("Enter the words : ")
# reverce = text[::-1]
# if text  == reverce:
#     print("this works is palindrome")
# else:
#     print("this works is not  palindrome") 













