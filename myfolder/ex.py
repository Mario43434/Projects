# In an array 1-100 multiple numbers are duplicates, how do you find it?

# list1 = ["hii",1,1,3,4,5]
# list2 = [i for i in range(len(list1)) if  list1[i] == 1]
# print(list2)

# -------------------------------------------------------------------------------------------------------------------------------------
# Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.

# arr1 = [1,2,3,4,5]
# arr2 = [5,4,3,2]
# p = []

# for i in arr1:
#     if i not in arr2:
#         p.append(i)
         
# print(p)
        
        
# ---------------------------------------------------------------------------------------------------------------------------------------
# Write a program to reverse the array


# arr = [1,2,3,4]
# def rev(arr):
#     start = 0
#     end = len(arr)-1

#     while end > start:
#      arr[start],arr[end] = arr[end],arr[start]
#      start += 1
#      end -= 1


# rev(arr)
# print(arr)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Write a program to sort the given array

# arr = [1,5,4,2,3]
# for j in range(len(arr)-1):
#     for i in range(len(arr)-1):
#      if arr[i] > arr[i + 1]:
#         arr[i],arr[i+1] = arr[i + 1],arr[i]

# print(arr)
#----------------------------------------------------------------------------------------------------------------------------------  

# string = input("enter the sting : ")
# rev = string[::-1]
# if string == rev:
#     print("palindrom")
# else:
#     print("Not palindrom")


# num = int(input())
# str = str(num)
# rev = str[::-1]
# if str == rev:
#     print("Yes")
# else:
#     print("NO")

# ---------------------------------------------------------------------------------------------------------------------------------------
# prime or not 
# a = 50
# for i in range (2,int(a ** 0.5) + 1):
#     if a % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")
        
# ---------------------------------------------------------------------------------------------------------------------------------------
# Write a method which will remove any given character from a String?

# original = "hello, world"
# new_str = ''
# for char in original:
#     if char != ',':
#         new_str += char
# print(new_str)

# ---------------------------------------------------------------------------------------------------------------------------------------

# How to count the occurrence of a given character in a String?

# def countchars(string):
#     chars = {}
#     for char in string:
#         if char in chars:
#             chars[char] += 1
#         else:
#             chars[char] = 1
#     return chars

# string = "HELLO"
# chars = countchars(string)
# for char, count in countchars(string).items():
#     print(f"{char} : {count}")




# text = "hello"
# text.lower() == text.upper()
# target = "L"
# count = sum(1 for c in text if c.lower() == target.lower())
# print(count)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Write a program to find the longest word in a given sentence.


# def lengthOfWord(string):
#     l = 0
#     w = ' '
#     words = string.split()
#     for word in words:
#         if len(word) > l :
#             w = word
#             l = len(word)
#     return(w,l)


# string = input()
# w, l = lengthOfWord(string)
# print(w, l)

# ---------------------------------------------------------------------------------------------------------------------------------------
# How can you reverse a string?

# def reverse(s):
#     sr=s[::-1]
#     return sr

# def rev_words (s):
#     n = len(s)
#     if n==1:
#         return s
#     s2 = s.split(" ")
#     size = len(s2)
#     rev_all = ""
#     for i in range(size):
#         rev = reverse(s2[i])
#         rev_all = rev_all + rev + " "
#     print (reverse(rev_all))


# s= "i am manoj"
# ans = rev_words(s)
# print(ans)
  # ---------------------------------------------------------------------------------------------------------------------------------------
# How to calculate the number of vowels and consonants in a string?

# def calculate(sting):
#     sting = sting.lower()
#     Vowels_count = 0
#     consonants = 0
#     list = ["a","e","i","o","u"]
#     for i in sting:
#         if i in list:
#             Vowels_count += 1
            
#         else:
#             consonants += 1
#     return "Vowels: " + str(Vowels_count) + ", Consonants: " + str(consonants)
    

# sting = "invention"
# ans = calculate(sting)
# print(ans)
# ---------------------------------------------------------------------------------------------------------------------------------------

# sort the array

# arr = [2,3,4,1,5,9]

# for j in range(len(arr)-1):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
            

# print(arr)

# ----------------------------------------------------------------------------------------------------------------------------------------
# Binary orr not
def is_binary_number(n):
    
    if n < 0:
        return False
    while n > 0:
        digit = n % 10
        if digit > 1:
            return False
        n = n // 10
    return True

# Example array with one number
arr = [10,11] 

if len(arr) == 1 and is_binary_number(arr[0]):
    print("Binary")
else:
    print("Not Binary")