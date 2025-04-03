import math
import random
import string

# 1. Hello World
print("Hello, World!")

# 2. Add Two Numbers
a = 5
b = 10
print("Sum:", a + b)

# 3. Check Even or Odd
num = 4
print("Even" if num % 2 == 0 else "Odd")

# 4. Find Largest Number
print("Largest:", max(3, 7, 2))

# 5. Swap Two Numbers
a, b = 5, 10
a, b = b, a
print(a, b)

# 6. Print Numbers from 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()

# 7. Sum of First N Natural Numbers
n = 5
print("Sum:", sum(range(1, n + 1)))

# 8. Factorial of a Number
fact = 1
for i in range(1, 6):
    fact *= i
print("Factorial:", fact)

# 9. Multiplication Table
n = 3
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 10. Reverse a Number
num = 1234
print("Reversed:", str(num)[::-1])

# 11. Palindrome Check
s = "madam"
print("Palindrome" if s == s[::-1] else "Not a palindrome")

# 12. Count Vowels in a String
s = "hello"
vowels = "aeiou"
print("Vowel count:", sum(1 for char in s if char in vowels))

# 13. Find Largest in a List
numbers = [3, 8, 2, 9]
print("Largest:", max(numbers))

# 14. Sort a List
lst = [4, 1, 7, 3]
print("Sorted List:", sorted(lst))

# 15. Remove Duplicates from a List
lst = [1, 2, 2, 3, 4, 4, 5]
print("Unique List:", list(set(lst)))

# 16. Print Star Pattern
n = 4
for i in range(1, n+1):
    print("*" * i)

# 17. Print Inverted Star Pattern
for i in range(n, 0, -1):
    print("*" * i)

# 18. Number Pyramid
for i in range(1, n+1):
    print(" ".join(str(i) for _ in range(i)))

# 19. Simple Calculator
a, op, b = 5, '+', 3
print(eval(f"{a}{op}{b}"))

# 20. Fibonacci Series
a, b = 0, 1
for _ in range(5):
    print(a, end=" ")
    a, b = b, a + b
print()

# 21. Armstrong Number Check
num = 153
print("Armstrong" if num == sum(int(digit) ** 3 for digit in str(num)) else "Not Armstrong")

# 22. Reverse a String
s = "Python"
print("Reversed:", s[::-1])

# 23. Check Prime Number
num = 11
print("Prime" if num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)) else "Not Prime")

# 24. Guess the Number Game
num = random.randint(1, 10)
guess = 5
print("Correct!" if guess == num else f"Wrong! It was {num}")

# 25. Check Leap Year
year = 2024
print("Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year")

# 26. Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# 27. Convert Kilometers to Miles
km = 5
miles = km * 0.621371
print("Miles:", miles)

# 28. Find Square Root
num = 16
print("Square Root:", math.sqrt(num))

# 29. Find Cube of a Number
num = 3
print("Cube:", num ** 3)

# 30. Calculate Simple Interest
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print("Simple Interest:", si)

# 31. Find ASCII Value of a Character
char = 'A'
print("ASCII Value:", ord(char))

# 32. Generate Random Number
print("Random Number:", random.randint(1, 100))

# 33. Find Length of a String
s = "Python"
print("Length:", len(s))

# 34. Reverse a List
lst = [1, 2, 3, 4, 5]
print("Reversed List:", lst[::-1])

# 35. Merge Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Merged List:", list1 + list2)

# 36. Convert String to Uppercase
s = "hello"
print("Uppercase:", s.upper())

# 37. Convert String to Lowercase
s = "HELLO"
print("Lowercase:", s.lower())

# 38. Count Occurrences of an Element in List
lst = [1, 2, 2, 3, 3, 3]
print("Count of 3:", lst.count(3))

# 39. Check if Number is Positive, Negative, or Zero
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 40. Find Sum of Digits of a Number
num = 1234
print("Sum of Digits:", sum(int(digit) for digit in str(num)))

# 41. Convert Decimal to Binary
num = 10
print("Binary:", bin(num)[2:])

# 42. Convert Decimal to Hexadecimal
print("Hexadecimal:", hex(num)[2:])

# 43. Convert Decimal to Octal
print("Octal:", oct(num)[2:])

# 44. Find Maximum and Minimum in a List
lst = [4, 7, 1, 9]
print("Max:", max(lst), "Min:", min(lst))

# 45. Remove a Specific Element from a List
lst.remove(7)
print("List after removal:", lst)

# 46. Find Area of a Circle
radius = 5
area = math.pi * radius ** 2
print("Area of Circle:", area)

# 47. Find Area of a Rectangle
length, width = 10, 5
print("Area of Rectangle:", length * width)

# 48. Find Area of a Triangle
base, height = 10, 5
print("Area of Triangle:", (base * height) / 2)

# 49. Check if a Number is Divisible by Another
a, b = 10, 2
print("Divisible" if a % b == 0 else "Not Divisible")

# 50. Count Words in a Sentence
sentence = "Hello world, welcome to Python!"
print("Word Count:", len(sentence.split()))
