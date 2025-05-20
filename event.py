from db import events_collection

class Event:
  def __init__(self, name, category_id, category_name, date, description, id = None):
    self.name = name
    self.category_id = category_id
    self.category_name = category_name
    self.date = date
    self.description = description
    self.id = id

  def __str__(self):
    return f"Name: {self.name}, Category: {self.category_name}, Date: {self.date}, Description: {self.description}"

  def save(self):
    if self.id:
      events_collection.update_one({"_id": self.id}, {"$set": self.__dict__})
    else:
      result = events_collection.insert_one(self.__dict__)
      self.id = result.inserted_id
