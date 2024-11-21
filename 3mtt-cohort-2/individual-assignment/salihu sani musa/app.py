def calculator():
    print('calculator')
    num1=float(input('input first number:'))
    operator=input('input opertor +,-,*,/12:')
    num2=float(input('input second number:'))
    if operator=='+':
        result=num1+num2
    elif operator=='-':
        result=num1-num2=
    elif operator=='*':
        result=num1*num2
    elif operator=='/':
        if num2!=0:
           result=num1/num2
        else :
            return 'error: num2 must be greater than 0'
    else :
        return 'operator not defined'
    return f'answer: {result}'
print(calculator()) 
        
    
        