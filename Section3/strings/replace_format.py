age = 24
print("my age is " + str(age) + "years")
print()
print("-- using replacement field")
print("my age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Number of days in Jan: {2}, Feb: {0}, Mar:{1}"
      .format(28, 30, 31))
print()
print("-- Multi-line")
print("""Number of days in 
Jan: {2} 
Feb: {0} 
Mar: {1}""".format(28, 30, 31))

print("\n-- f-string")
print(f"Tim is {age} years old")
print(f"pi is approximately {22/7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:53.50f}")
