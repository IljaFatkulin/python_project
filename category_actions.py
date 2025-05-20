from db import category_collection, events_collection
from category import Category
from event import Event

def view_categories():
  categories = category_collection.find()

  if category_collection.count_documents({}) == 0:
    print("No categories found")
    return

  for category in categories:
    print(f"Name: {category['name']}")

def add_category():
  name = input("Enter category name: ")

  if category_collection.find_one({"name": name}):
    print("Category already exists")
    return

  new_category = Category(name)
  new_category.save()
  print(f"Category added with ID: {new_category.id}")

def delete_category():
  name = input("Enter category name to delete: ")

  if not category_collection.find_one({"name": name}):
    print("Category not found")
    return

  category_collection.delete_one({"name": name})
  print(f"Category '{name}' deleted successfully")

def edit_category():
  name = input("Enter category name to edit: ")

  if not category_collection.find_one({"name": name}):
    print("Category not found")
    return

  new_name = input("Enter new category name: ")

  if category_collection.find_one({"name": new_name}):
    print("Category already exists")
    return

  category_collection.update_one({"name": name}, {"$set": {"name": new_name}})
  print(f"Category '{name}' updated to '{new_name}' successfully")

def search_category():
  name = input("Enter category name to search: ")

  category = category_collection.find_one({"name": name})

  if not category:
    print("Category not found")
    return

  print(f"Category found: {category['name']}")

def view_category_events():
  name = input("Enter category name to view events: ")
  category = category_collection.find_one({"name": name})
  if not category:
    print("Category not found")
    return

  if events_collection.count_documents({"category_id": category['_id']}) == 0:
    print("No events found for this category")
    return

  for event in events_collection.find({"category_id": category['_id']}):
    event = Event(event['name'], event['category_id'], event['category_name'], event['date'], event['description'], event['_id'])
    print(event)


  return

def run():
  while (True):
    print("1. View Categories")
    print("2. Add Category")
    print("3. Delete Category")
    print("4. Edit Category")
    print("5. Search Category")
    print("6. View Category Events")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
      view_categories()
    elif choice == '2':
      add_category()
    elif choice == '3':
      delete_category()
    elif choice == '4':
      edit_category()
    elif choice == '5':
      search_category()
    elif choice == '6':
      view_category_events()
    elif choice == '7':
      break
    else:
      print("Invalid choice, please try again.")