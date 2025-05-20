from event_actions import run as event_run
from category_actions import run as category_run

while(True):
  print("1. Category Actions")
  print("2. Event Actions")
  print("3. Exit")

  choice = input("Choose an option: ")

  if choice == '1':
    category_run()
  elif choice == '2':
    event_run()
  elif choice == '3':
    break
  else:
    print("Invalid choice, please try again.")