a = float(input('Write the first number:'))

o = input('Select the operator (/ * - +):')

b = float(input('Write the second nomber:'))



if o == '/':
    print(a/b)
elif o == '*':
    print(a*b)
elif o == '-':
    print(a-b)
elif o == '+':
    print(a+b)
else:
    print('Error')