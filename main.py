# print ("Hello, Darinka")

# name = "Марія"  # str
# age = 25  # int
# weight = 60.5  # float
# is_student = True  # bool

# print(name, age, weight, is_student)
# print (name)


# my_list = ["apple", "banana", "cherry"]
# my_list[1] = "blueberry"
# print(my_list)  

# prosto= {"name":1, "age": 2}
# print (prosto)
# prosto["email"]= "w@gmail.com"
# print(prosto)
# del prosto["age"]
# print (prosto)
# # Apple

# prosto= {"name":1, "age": 2}
# if prosto ["age"] >=1:
#      print ("Apple")


# my_dict = {"name": "Олексій", "age": 16}
# if my_dict["age"] >= 18:
#     print("Ви повнолітній")
# else:
#     print("No")    

# fruits = ["яблуко", "банан", "вишня"]
# for fruit in fruits:
#     print(fruit)


# for letter in "Python":
#     print(letter)


# sentence = "The quick brown fox jumps over the lazy dog"
# length = 0
# for i in sentence:
#     if i != " ":
#         length += 1
#         print (i)




# N = 10 # Задаємо N  Start!!!

# # Ініціалізуємо змінні
# sum_squares = 0  # Сума квадратів
# i = 1            # Поточне число

# # Цикл while
# while i <= N:  # Умова для ітерацій від 1 до N
#     sum_squares += i * i  # Додаємо квадрат поточного числа до суми
#     i += 1                # Збільшуємо лічильник на 1

# # Виведення результату
# print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}.")


# first_name = "Олексій"
# last_name = "Гупало"
# full_name = first_name + " " + last_name
# print(len(full_name))


# first_name = "John"
# last_name = "Doe"


# def get_initials(first_name, last_name):
#     return f"{last_name} {first_name[0]}."
    
# formatted_name  = get_initials(first_name, last_name)
# print(formatted_name)

# first = "Python"
# second = "python"


# def compare(first, second):
#     return first.lower() == second.lower()
    
    
# result = compare(first, second)

# print (result)

# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")

# num = int(input("Введіть число: "))

# length = len(str(num))
# print(length)

# # Задаємо конкретне число
# num = int(input())

# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x
# print(result)


# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1


# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break



# numbers = {
#     1: "one",   #key : value
#     2: "two",
#     3: "three"
# }

# for key in numbers:
#     print (key)


# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")


# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")


# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 11)
# print(result)  # Виведе: 15


# def my_function() -> ReturnType:
#     # виконати дії
#     return result
