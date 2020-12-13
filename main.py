print('Welcome to calculator\n\n+ for addition\n- for subtration\n/ for division\n* for multiplication\n** for power of\n% for remainder of division\n')

def calculator():
    opp = print('Enter your choice:')
    opp = input()

    num1 = print('Enter first number:')
    num1 = float(input())

    num2 = print('Enter second number:')
    num2 = float(input())

    if opp == '+' :
        print(str(num1)+" + "+str(num2)+ " =", num1+num2)

    elif opp == '-':
        print(str(num1)+" - "+str(num2)+ " =", num1-num2)

    elif opp == '/':
        print(str(num1)+" / "+str(num2)+ " =", num1/num2)

    elif opp == '*':
        print(str(num1)+" * "+str(num2)+ " =", num1*num2)

    elif opp == '**':
        print(str(num1)+" ** "+str(num2)+ " =", num1**num2)

    elif opp == '%':
        print(str(num1)+" % "+str(num2)+ " =", num1**num2)   
    
    else:
        print('Wrong input')

def again():
    z1 = print('\nIf you want to use again calculator press y if not press n')
    z1 = input()

    if z1 == 'y':
        calculator()

    else:
        print('Ok , see you later')

if __name__ == "__main__":
    calculator()
    again()
