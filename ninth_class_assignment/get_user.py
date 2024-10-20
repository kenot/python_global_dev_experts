import os
import getpass
import pwd

print(os.path.expanduser('~'))
print(os.environ.get('USER'))
print(getpass.getuser())
print(pwd.getpwuid(os.getuid())[0])
