a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # floating point division
print(a // b)   # integer division, rounds toward -ve infinity
print(a % b)    # modulo operator, returns remainder of a÷b
print()

# range takes int as arguments, so floating division is not applicable
print("range: ")
for i in range(1, a//b):
    print(i)
