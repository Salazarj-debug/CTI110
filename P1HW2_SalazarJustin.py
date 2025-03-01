#Justin Salazar
#2/28/25
#Travel Expenses
#Program that will calculate Remaining Balance of traveling to users location.

print('This program calculates and displays travel expenses')
Budget=int(input('Enter Budget:'))
Destination=input('Enter your travel destination:')
Gas=int(input('How much do you think you will spend on gas?'))
Accom=int(input('Approximately, how much will you need for accomodation/hotel?'))
Food=int(input('Last, how much do you need for food?'))
print('---------Travel Expenses---------')
print('Location:',Destination)
print('Initial Budget:',Budget)
print('Fuel:',Gas)
print('Accomodation:',Accom)
print('Food:',Food)
Remaining_Balance=(Budget-Gas-Accom-Food)
print('Remaining Balance:',Remaining_Balance)
    
    
