#original_code_for_mmt
#Salary, calculating gross,tax&take_home base on input.
def salary():
    #ask for rate
    rate = float(input("what is your hourly rate? $"))
    #ask for hours per week
    hours = float(input("how many hours do you work per week? "))
    #ask and calculate tax
    tax = float(input("What's your tax rate? "))
    tax_rate = tax/100
    #calculations start here. first is the gross_pay. which is rate * hourly_wage
    gross_pay = rate * hours
    #user wants to see gross pay
    display_gp = input("Would you like to see your gross pay? Y/N ")
    if display_gp == 'Y' or 'y':
        print("Here's how much you've earned without tax: $ "+str(gross_pay))
    #second is tax amount in $ according to the % 
    tax = gross_pay * (tax_rate/100)
    #that's how much you should take home
    take_home = gross_pay - tax
    print("You've earned $"+str(take_home)+" this week.")
    return take_home
def money_manager(take_home):
    #getting the saving percentage from the user
    print("it is recommended to save at least 20% of your salary.")
    saving_perc = float(input("How much you want to save? %"))
    saved_money = take_home * saving_perc/100
    #display the amount saved
    print("money saved $"+str(saved_money)) 
    #getting users spending info
    entertainement_spendings = float(input("How much do you spend on entertainement? "))
    necessary_spendings = float(input("How much do you spend on water, electricity,clothing, self-care & car"))
    #spending should be more detailed but I think that's enough.
    total_spending = entertainement_spendings + necessary_spendings
    #display total spending
    print("You usually spend $"+str(total_spending)+"per month")
    checking_balance = take_home - (total_spending + saved_money)
    print("Checking Balance: $" + str(checking_balance))
def mmt_manager():
    take_home = salary()
    money_manager(take_home)
mmt_manager()

    
