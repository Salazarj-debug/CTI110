print('-----Calculating Exponetns------')

print('Enter integer as the base value:', end='')
base_value=int(input())
print('Enter integer as the exponent:', end='')
Exponent_value=int(input())
End_result=base_value**Exponent_value

print(base_value,'Raised by the Power of', Exponent_value,'is',End_result,'!!')

print('-----Addition and subtraction-----')
integer=int(input('Enter a starting integer:'))
add=int(input('Enter an integer to add:'))
subtract=int(input('Enter an integer to subtract:'))
Ending_result=integer+add-subtract
print(integer,'+',add,'-',subtract,'is equal to', Ending_result,end='')