import sys

print ('Im G, how can I help You?')

while True:
    operator = input ('enter your operator: ')
    num1 = float (input ('enter the 1st number: '))
    num2 = float (input ('enter the 2nd number: '))

    if operator == "+":
        result = num1 + num2 
        print (result)
    elif operator == "-":
        result = num1 - num2
        print (result)
    elif operator == "*":
        result = num1 * num2
        print (result)

    if operator == "/" and num1 == 0 or num2 == 0:
        print ('zjeb')
    else:
        result = num1 / num2
        print (result)  

    print ('anytning else? (y/n)')
    if input().lower() == 'n':
        print ('see you soon') 

        sys.exit()