split_string = "This string is\nsplit into\nseveral lines"
tab_escape = "1\t2\t3\t4\t5"
single_quotes = 'He said, "No, that\'s not possible".'
double_quotes = "He said, \"No, that's not possible\"."
triple_quotes = """He said, "No, that's not possible"."""
escape_eol = """This line is \
coded in multiple \
but prints in \
a single line"""
escaping_the_escape_character = "escape character '\\' (called slash)"
raw = r"escape character '\' (called slash)"
print(split_string)
print(tab_escape)
print(single_quotes)
print(double_quotes)
print(triple_quotes)
print()
print(escape_eol)
print(escaping_the_escape_character)
print(raw)
