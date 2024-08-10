# Question: Is there a difference between the two lines below? Why?

# Answer: Use single-quotes for string literals, e.g. 'my-identifier', but use double-quotes for strings that are likely
# to contain single-quote characters as part of the string itself (such as error messages, or any strings containing
# natural language), e.g. "You've got an error!".

name = "john"
name = 'john'

# Question: What is the issue with the code below?

# Answer: TypeError: can only concatenate str (not "set") to str

# Solution: I used F-String for String Interpolation

my_number = 5 + 5
print(f'result is: {my_number}')
