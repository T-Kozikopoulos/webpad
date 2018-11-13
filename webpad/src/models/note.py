from src.common.database import Database
from uuid import uuid4


class Note(object):

    def __init__(self, title, description, _id=None):
        self.title = title
        self.description = description
        self._id = uuid4().hex

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find({})]

    def save_to_mongo(self):
        Database.insert(self.json())

    def json(self):
        return {"title": self.title,
                "description": self.description,
                "_id": self._id}
