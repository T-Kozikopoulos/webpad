import pymongo


class Database(object):

    URI = 'mongodb://localhost:27017/'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.notes
        Database.COLLECTION = Database.DATABASE.notes

    @staticmethod
    def insert(data):
        Database.DATABASE['notes'].insert(data)

    @staticmethod
    def find(query):
        return Database.DATABASE['notes'].find(query)

    @staticmethod
    def purge():
        return Database.DATABASE['notes'].remove({})
