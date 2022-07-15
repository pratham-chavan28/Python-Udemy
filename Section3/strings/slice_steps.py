parrot = "Norwegian Blue"

print(parrot)
print(parrot[:6:2])
print(parrot[::3])
print()

print("-- slicing backwards")
print(parrot[::-1])
print()

alphabets = "abcdefghijklmnopqrstuvwxyz"
print("-- Assignment")
# print qpo
print(alphabets[16:13:-1])
# print edcba
print(alphabets[4::-1])
# print last 8 characters in reverse order
print(alphabets[26:17:-1])
print(alphabets[:-9:-1])

print(alphabets[-1::-1])
print(alphabets[:1])    # code does not crash when string is empty5
