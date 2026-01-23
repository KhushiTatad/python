# Static Vs Dynamic Typing
# Static Vs Dynamic Binding
# stylish declaration techniques

name = 'nitish'
print(name)

a = 5
b = 6

name = 'khushi'
print(name)

a =98
b = 78
print(a + b)

# Dynamic Typing
a = 5
# Static Typing
# ??? int a = 5  File "/tmp/ipython-input-1639363930.py", line 4
#     int a = 5
#         ^
# SyntaxError: invalid syntax

# Dynamic Binding
a = 5
print(a)
a = 'nitish'
print(a)

# Static Binding
# int a = 5
#   File "/tmp/ipython-input-1631536935.py", line 8
#     int a = 5
#         ^
# SyntaxError: invalid syntax



a = 1
b = 2
c = 3
print(a,b,c)

khushi = 23
heena = 22
saumya = 34 
print(khushi, heena, saumya)

a,b,c = 1,2,3
print(a,b,c)

a=b=c= 5
print(a,b,c)


name1 = 'Nitish'
# What is compilation = COnvert to binary and binary to Native Language 
# WHO Does Complilation = interpreter/compiler 
print(name1)


# Identifiers
# You can't start with a digit
name1 = 'Nitish'
print(name1)
# You can use special chars -> _
_ = 'ntiish'
print(_)
# identiers can not be keyword







# Implicit Vs Explicit
print(5+5.6)
print(type(5),type(5.6))

# print(4 + '4')



# Explicit
# str -> int
# int(4+5j)

# int to str
str(5)


# float
float(4)




a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)


#   OUTPUT
# 10 100 200 300
# 10.5 150.0 0.0015
# 3.14j 3.14 0.0




string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
# raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


uni = "\U0001f600"

print(uni)

    #    OUTPUT
# This is Python
# This is Python
# C
# This is a multiline string with more than one line code.
# 😀😆🤣
# raw \n string
# 😀

k = None
a = 5
b = 6
print('Program exe')
# OUTPUT
# Program exe