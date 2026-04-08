#  BASIC CALCULATOR 



ip1= int(input("Enter first number: ")
)
op = input("Enter operator")
ip2 =int( input("Enter Second Number"))


if op == '+':
     print(ip1+ip2)

   
if op == '-':
    print(ip1-ip2)
elif op == '*':
    print(ip1*ip2)
elif op  == '/':
    if ip2 == 0:
        print("Error : Division By Zero ")
    else:
        print(ip1/ip2)
elif op == '%':
    if ip2 == 0:
        print("Error: Modulo  Zero")

    else:
     print(ip1%  ip2)
else:
    print("Check The Value You Gave")

