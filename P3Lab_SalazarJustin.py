#justin Salazar
#3/22/25
#P3Lab
#user input number for change
def calculate_coins():
    # Input money as a float
    money = float(input("Enter the amount of money (e.g., 5.99): "))
    
    # Convert to cents
    cents = int(round(money * 100))
    
    # Initialize coin values
    dollars = cents // 100
    cents %= 100
    
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents  # Remaining cents are all pennies
    
    # Display results
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

# Run the function
calculate_coins()