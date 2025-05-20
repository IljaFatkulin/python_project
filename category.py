from db import category_collection

class Category:
  def __init__(self, name, id=None):
    self.name = name
    self.id = id

  def __str__(self):
    return f"Category({self.name})"

  def save(self):
    if self.id:
      category_collection.update_one({"_id": self.id}, {"$set": self.__dict__})
    else:
      result = category_collection.insert_one(self.__dict__)
      self.id = result.inserted_id