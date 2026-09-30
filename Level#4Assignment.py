expense_list = []
expense = None
#Ask user to enter expense until they answer 0 to indinicate they are done
while expense != 0:
    expense = float(input("Enter an expense (or type '0' to finish): "))
#make sure the expenses entered are valid
    if expense < 0:
        print ("Invalid input, Please Enter a positive number")
    elif expense == 0:
            print("\nThank you. \nHere is your Travel Summary\n")
    else:
         expense_list.append(expense)

#end loop 

small_expense = 0
moderate_expense = 0
large_expense = 0
#classify expesenses
for expense in expense_list:
    if expense < 25:
        small_expense += 1
    elif expense <= 100:
        moderate_expense += 1
    else:
        large_expense += 1


#less than $25 - small expense
#25 through $100 moderate expense
# greater than 100 - large expense

#Print out expense summary 

#total number of expenses
count_expense = len(expense_list)
print(f"Total number of expenses:  {count_expense}")
#total expenses (sum of all them, with proper formatting)
total_expenses = f"${sum(expense_list):,.2f}"
print(f"Total: {total_expenses}")
#average expense (with proper formatting)
import statistics
average = f"${statistics.mean(expense_list):,.2f}"
print(f"Average: {average}")
#smallest expense (with proper formatting)
min_expense = f"${min(expense_list):,.2f}"
print(f"Smallest expense: {min_expense}")
#largest expense (with proper formatting)
max_expense = f"${max(expense_list):,.2f}"
print(f"Largest expense:  {max_expense}")
#number of small, meidum and large expenses 
print(f"\nSmall expenses: {small_expense}")
print(f"Moderate expenses: {moderate_expense}")
print(f"Large expenses: {large_expense}")