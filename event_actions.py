from db import events_collection, category_collection
from event import Event
from datetime import datetime, timedelta

def create_event_object(event_data):
  return Event(event_data['name'], event_data['category_id'], event_data['category_name'], event_data['date'], event_data['description'], event_data['_id'])

def add_event():
  categories = category_collection.find()

  if category_collection.count_documents({}) == 0:
    print("No categories found, please add a category first.")
    return

  print("Available categories: " + ", ".join([f"{category['name']}" for category in categories]))
  category_name = input("Enter category name: ")
  category = category_collection.find_one({"name": category_name})

  if not category:
    print("Category not found")
    return

  name = input("Enter event name: ")
  date = input("Enter event date (YYYY-MM-DD): ")
  time = input("Enter event time (HH:MM): ")
  date_obj = datetime.strptime(date, "%Y-%m-%d").date()
  time_obj = datetime.strptime(time, "%H:%M").time()
  date_time = datetime.combine(date_obj, time_obj)

  description = input("Enter event description: ")

  event = Event(name, category['_id'], category['name'], date_time, description)
  event.save()

def delete_event(event_id=None):
  if not event_id:
      event_id = input("Enter the event ID to delete: ")

  events_collection.delete_one({"_id": event_id})

def print_events():
  events = events_collection.find()

  if events_collection.count_documents({}) == 0:
    print("No events found")
    return

  for event in events:
    event_obj = Event(event['name'], event['category_id'], event['category_name'], event['date'], event['description'], event['_id'])
    print(event_obj)

def event_details(event):
  print(event)
  action = input("1. Skip / 2. Delete / 3. Edit: ")
  if action == '1':
    return
  elif action == '2':
    delete_event(event.id)
  elif action == '3':
    event.name = input("Enter new event name: ")

    date = input("Enter new event date (YYYY-MM-DD): ")
    time = input("Enter new event time (HH:MM): ")
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    time_obj = datetime.strptime(time, "%H:%M").time()
    event.date = datetime.combine(date_obj, time_obj)

    event.description = input("Enter new event description: ")
    event.save()

def search_event_by_name(name):
  i = 1
  found_events = events_collection.find({"name": name})

  if events_collection.count_documents({}) == 0:
    print("No events found")
    return

  events = []

  for event in found_events:
    event_obj = create_event_object(event)
    events.append(event_obj)
    print(f"{i}. {event_obj}")
    i += 1

  event_choice = input("Select an event to view details (or 'q' to quit): ")
  if event_choice.lower() == 'q':
    return

  selected_event = events[int(event_choice) - 1]
  event_details(selected_event)

def search_event_by_date(date):
  print("Next 24h events:")
  date = datetime.strptime(date, "%Y-%m-%d")

  start_of_day = datetime(date.year, date.month, date.day)
  end_of_day = start_of_day + timedelta(days=1)

  events = events_collection.find({"date": {"$gte": start_of_day, "$lt": end_of_day}})

  if events_collection.count_documents({}) == 0:
    print("No events found")
    return

  for event in events:
    event_obj = create_event_object(event)
    print(event_obj)

def find_next_24h_events():
  start_of_day = datetime.now()
  end_of_day = start_of_day + timedelta(days=1)

  return search_event_by_date(end_of_day.strftime("%Y-%m-%d"))


def run():
  while True:
    print("1. Add Event")
    print("2. View Events")
    print("3. Find Event by Name")
    print("4. Find Event by Date")
    print("5. Find Next 24h Events")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
      add_event()
    elif choice == '2':
      print_events()
    elif choice == '3':
      name = input("Enter event name to search: ")
      search_event_by_name(name)
    elif choice == '4':
      date = input("Enter event date (YYYY-MM-DD): ")
      search_event_by_date(date)
    elif choice == '5':
      find_next_24h_events()
    elif choice == '6':
      break
    else:
      print("Invalid choice, please try again.")