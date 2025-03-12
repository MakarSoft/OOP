import sys

from _lib import print_line

    
string1: str = '1'
string2: str = '1'
str_res = string1 + string2 # конкатенация

print(type(string1), type(string2), type(str_res))
print(sys.getsizeof(string1), sys.getsizeof(string2), sys.getsizeof(str_res))
print(str_res)  # '11'
print_line()

i: int = 1
j: int = 1
int_res = 1 + 1

print(type(i), type(j), type(int_res))
print(sys.getsizeof(i), sys.getsizeof(j), sys.getsizeof(int_res))
print(int_res)  # 2'
print_line()


