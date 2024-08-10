# Question: Fix the following code without changing a or b:

# Solution: The problem was TypeError: unsupported operand type(s) for +: 'int' and 'str' as we try to summarize two
# different data types. I solved the problem by converting the variable b from string to integer.

a = 8
b = "123"

print(a + int(b))