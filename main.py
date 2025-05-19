import uuid
import datetime

class Event:
  def __init__(self, name, category, date, description, location = None):
    self.name = name
    self.category = category
    self.date = date
    self.description = description
    self.location = location
    self.id = str(uuid.uuid4())

  def __str__(self):
    return f"Event({self.name}, {self.category}, {self.date}, {self.description}, {self.location})"

class NoteManager:
  def __init__(self):
    event1 = Event("Meeting", "Work", datetime.datetime(2023, 10, 10, 14, 0), "Project discussion", "Office")
    event2 = Event("Meeting", "Health", datetime.datetime(2025, 5, 5, 9, 30), "Annual check-up", "Clinic")
    event3 = Event("Birthday Party", "Personal", datetime.datetime(2023, 10, 10, 18, 0), "Celebrating with friends", "Home")
    event4 = Event("Conference", "Work", datetime.datetime(2023, 10, 15, 10, 0), "Tech conference", "Convention Center")
    self.events = {event1.id: event1, event2.id: event2, event3.id: event3, event4.id: event4}

  def run(self):
    while True:
      print("1. Add Event")
      print("2. View Events")
      print("3. Find Event by Name")
      print("4. Find Event by Date")
      print("5. Find Next 24h Events")
      print("6. Exit")

      choice = input("Choose an option: ")

      if choice == '1':
        self.add_event()
      elif choice == '2':
        self.print_events()
      elif choice == '3':
        name = input("Enter event name to search: ")
        event = self.search_event_by_name(name)
      elif choice == '4':
        date = input("Enter event date (YYYY-MM-DD): ")
        event = self.search_event_by_date(date)
      elif choice == '5':
        events = self.find_next_24h_events()
        if events:
          print("Next 24h events:")
          for event in events:
            print(event)
        else:
          print("No events found in the next 24 hours.")
      elif choice == '6':
        break
      else:
        print("Invalid choice, please try again.")

  def search_event_by_name(self, name):
    events = self.find_events_by_name(name)
    if events:
      print(f"Found {len(events)} events with name '{name}':")
      for i, event in enumerate(events):
        print(f"{i+1}. {event}")
      choice = input("Choose an event to view details: ")
      if choice.isdigit() and 1 <= int(choice) <= len(events):
        event = events[int(choice) - 1]
        self.event_details(event)

  def search_event_by_date(self, date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    events = []
    for event in self.events.values():
        if event.date.date() == date_obj:
            events.append(event)
    if events:
        print(f"Found {len(events)} events on '{date}':")
        for i, event in enumerate(events):
            print(f"{i+1}. {event}")
        choice = input("Choose an event to view details: ")
        if choice.isdigit() and 1 <= int(choice) <= len(events):
            event = events[int(choice) - 1]
            self.event_details(event)

  def event_details(self, event):
    print(event)
    action = input("1. Skip / 2. Delete / 3. Edit: ")
    if action == '1':
      return
    elif action == '2':
      self.delete_event(event.id)
    elif action == '3':
      event.name = input("Enter new event name: ")
      event.category = input("Enter new event category: ")

      date = input("Enter new event date (YYYY-MM-DD): ")
      time = input("Enter new event time (HH:MM): ")
      date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
      time_obj = datetime.datetime.strptime(time, "%H:%M").time()
      event.date = datetime.datetime.combine(date_obj, time_obj)

      event.description = input("Enter new event description: ")
      event.location = input("Enter new event location (optional): ")

  def add_event(self):
    name = input("Enter event name: ")
    category = input("Enter event category: ")

    date = input("Enter event date (YYYY-MM-DD): ")
    time = input("Enter event time (HH:MM): ")
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    time_obj = datetime.datetime.strptime(time, "%H:%M").time()
    date_time = datetime.datetime.combine(date_obj, time_obj)

    description = input("Enter event description: ")
    location = input("Enter event location (optional): ")

    event = Event(name, category, date_time, description, location)
    self.events[event.id] = event

  def print_events(self):
    for event_id, event in self.events.items():
      print(event)

  def find_events_by_name(self, name):
    events = []
    for event in self.events.values():
        if event.name.lower() == name.lower():
            events.append(event)
    return events

  def find_event_by_date(self, date):
    for event in self.events.values():
        if event.date.date() == date:
            return event
    return None

  def delete_event(self, event_id=None):
        if not event_id:
            event_id = input("Enter the event ID to delete: ")

        if event_id in self.events:
            del self.events[event_id]
            print("Event deleted.")
        else:
            print("Event not found.")

  def find_next_24h_events(self):
    now = datetime.datetime.now()
    next_24h_events = []
    for event in self.events.values():
        if now <= event.date <= now + datetime.timedelta(hours=24):
            next_24h_events.append(event)
    return next_24h_events

noteManager = NoteManager()
noteManager.run()
