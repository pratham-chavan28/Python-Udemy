greeting = "Hello"
name = input("Enter a name ")
age = 24

print(age)
print("age: " + str(type(age)))

print(greeting, name)
print(type(name))

# # data type of variables can be changed at runtime
# age = "24 years"
# print("age now: " + str(type(age)))

# Concatenating str and int leads to type error
print(name + " is " + age + " years old")
