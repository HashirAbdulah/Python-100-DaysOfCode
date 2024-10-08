list = [1,2,3,4]
print(list)
print(type(list))

# list Comprehension\
# Question 1
# Create a list of the first 10 odd numbers using list comprehension.
oddList = [x for x in range(10) if x % 2 != 0]
print(oddList)

# Create a list of numbers from 1 to 10 that are divisible by 5.
divisibleByFive = [x for x in range(10) if x % 5 == 0]
print(divisibleByFive)


# Given a list of strings, create a new list with the length of each string.
fruits = ["apple", "banana", "cherry", "date"]
# Result should be [5, 6, 6, 4]
result = [len(fruit) for fruit in fruits]
print(result)

# Create a list of all the vowels in the given string.
sentence = "List comprehensions are cool!"
# Result should be ['i', 'o', 'e', 'e', 'i', 'o', 'a', 'e', 'o', 'o']
vowels = "aeiouAEIOU"
res = [char for char in sentence if char in vowels]
print(res)

#list creation with users values:
n = int(input("Enter the size of the list: "))

my_list = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

print("Your list is:", my_list)