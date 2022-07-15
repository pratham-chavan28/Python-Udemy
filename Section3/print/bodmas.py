a = 12
b = 3

print(a + b // 3 - 4 * 12)
# the precedence is as follows:
print(a + (b // 3) - (4 * 12))

# to evaluate in the order it is written, use:
print(((a + b) // 3 - 4) * 12)

# other way is to break up in multiple expressions
print("multiple expressions")
c = a + b
d = c // 3
e = d - 4
print(e * 12)
