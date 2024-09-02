# Question_1: Is the following code legal?

# Answer: Yes it is. Though, if an exception was raised in the 'try' block, it would've been propagated after the
# 'finally' block is executed.

try:
    x = 1
finally:
    print("finally")

# Question_2: What exception types can be caught by the following handler? Except:

# Answer: 'AssertionError', 'AttributeError', 'EOFError', 'FloatingPointError', 'GeneratorExit', 'ImportError',
# 'IndexError', 'KeyError', 'KeyboardInterrupt', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError',
# 'OverflowError', 'ReferenceError', 'RuntimeError', 'StopIteration', 'SyntaxError', 'IndentationError', 'TabError',
# 'SystemError', 'SystemExit', 'TypeError', 'UnboundLocalError', 'UnicodeError', 'UnicodeEncodeError',
# 'UnicodeDecodeError', 'UnicodeTranslateError', 'ValueError', 'ZeroDivisionError', 'FileNotFoundError'

# Question_3: What is wrong with using the above type of exception handler?

# Answer: It lacks an associated 'except' handler block or any code within the 'try' block that could potentially raise
# an exception.

# Question_4: What exceptions can be caught by the following handlers? except IOError and except ZeroDivisionError

# Answer: 1. IOError - 'File not found or inaccessible', 'Insufficient permissions', 'Device or disk errors',
# 'File system issues'. 2. ZeroDivisionError - 'Integer Division', 'Floating-Point Division', 'Modulo Operation',
# 'Complex Numbers'
