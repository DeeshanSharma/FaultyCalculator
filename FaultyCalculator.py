#codewithharry
#Design a calculator which will correctly solve all the problems except the following ones:
#45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
#Your program should take operator and two numbers as input from the user and then return the result


op1 = int(input("Enter operator 1 = "))   # Operator no 1
op2 = int(input("Enter operator 2 = "))   # Operator no 2
op = input("Enter the operation (+, -, *, /)= ")    # Operation to be performed

exp = [op1, op, op2]    # Expression created using above to be matched with given problems

# Checking for first expression
if (exp == [45, '*', 3]):
    print(555)

# Checking for second expression
elif (exp == [56, '+', 9]):
    print(77)

# Checking for third expression
elif (exp == [56, '/', 6]):
    print("4")

# Correct calculations further :-
elif (op == '+'):
    print(op1 + op2)

elif (op == '-'):
    print(op1 - op2)

elif (op == '*'):
    print(op1 * op2)

else:
    print(op1 / op2)
