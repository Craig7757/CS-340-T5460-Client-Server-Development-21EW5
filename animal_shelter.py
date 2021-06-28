from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:53044' % ("User1", 7757))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self,animal):
        if animal is not None:
            if animal:
                self.database.animals.insert_one(animal)  # data should be dictionary
                return True   
            else:
                return False         
        else:
            return False
            
 # Create method to implement the R in CRUD.
    def read(self,search):

        #if search isn't null it will return all rows of data
        if search is not None:
            result = self.database.animals.find_one(search)
            return result
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
  # Create method to ReadAll.
    def readAll(self,search):

        #if search isn't null it will return all rows of data
        if search is None:
            result = self.database.animals.find()
            return result
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
# Create method to implement the U in CRUD.
    def update(self,update,change):

        #if search isn't null it will return all rows of data
        if update is not None:
            result = self.database.animals.update(update,{"$set": change)
            return True
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
# Create method to implement the D in CRUD.
    def delete(self,remove):

        #if search isn't null it will return all rows of data
        if remove is not None:
            result = self.database.animals.delete_one(remove)
            return True
        else:
            raise Exception("Nothing to find, because data parameter is empty")