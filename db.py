import pymongo

class MongoDB:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(
            "mongodb+srv://root:root@cluster0.4jlnc41.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        )
        self.db = self.mongo_client["python_project"]
        self.events_collection = self.db["events"]
        self.category_collection = self.db["category"]

mongo_instance = MongoDB()

events_collection = mongo_instance.events_collection
category_collection = mongo_instance.category_collection
