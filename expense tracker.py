#Combining the features into application
from Features import search_by_date_linear,sort_amount,add_data,delete_data_date,sum_amount
transactions=[{'date': '2024-8-21', 'amount': 50, 'description': 'Banana'},
 {'date': '2024-8-22', 'amount': 70, 'description': 'Orange'},
 {'date': '2024-8-24', 'amount': 60, 'description': 'Apple'},
 {'date': '2024-8-25', 'amount': 100, 'description': 'grapes'},
 {'date': '2024-8-21', 'amount': 120, 'description': 'Guva'},
 {'date': '2024-8-29', 'amount': 585, 'description': 'kgh'}]


flag=True
while flag:
  print("Expense Tracker App")
  print("1. Add Transaction")
  print("2. Search Transaction")
  print("3. Sort Transaction")
  print("4. Delete Transaction")
  print("5. Display")
  print("6. Exit")
  print("7.amount")
  choice=int(input("Enter your choice: "))
  if choice == 1:
    print("-"*50)
    print("Adding Data")
    print("-"*50)
    transactions=add_data(transactions)
    print("-"*50)
  elif choice == 2:
    print("-"*50)
    print("Searching Data")
    print("-"*50)
    print(search_by_date_linear(transactions))
    print("-"*50)
  elif choice == 3:
    print("-"*50)
    print("Sorting Data")
    print("-"*50)
    transactions=sort_amount(transactions)
    print("-"*50)
  elif choice == 4:
    print("-"*50)
    print("Deleting Data")
    print("-"*50)
    transactions=delete_data_date(transactions)
    print("-"*50)
  elif choice == 5:
    print("-"*50)
    print("Displaying Transactions")
    print("-"*50)
    print(transactions)
    print("-"*50)
  elif choice == 6:
    print("-"*50)
    print("Exiting Application")
    flag=False
    print("-"*50)
  elif choice==7:
      print("-"*50)
      print("sum of amount of a given year")
      print(sum_amount(transactions))
      print("-"*50)
  else:
      print("-"*50)
      print("Please enter the correct choice")
      print("-"*50)
