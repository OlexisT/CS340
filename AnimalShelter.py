from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """Crud operations for Animal collection in MongoDB """
    
    def __init__(self, user, passw):
        # Initalizing the MongoClient. This helps to 
        # access the MongoDB databases and collection. 
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user. 
        # Definitions of the connection string variables are 
        # unique to the individual Apporto environment. 
        #
        # Your must edit the connection variables below to reflect
        # your own instance of MongoDB! 
        # 
        # Connection Variables
        #  
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32871
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        # 
        print('mongodb://%s:%s@%s:%d' % (user,passw,HOST,PORT))
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,passw,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            success = self.collection.insert_one(data) # data should be dictionary
            # Returns success status of the query
            return success.acknowledged
        else:
            
            raise Exception("Nothing to save, because data parameter is empty")
        
        
# Create method to implement the R in CRUD
    def read(self, findData):
        if findData is not None:
            data = self.collection.find(findData, {"id_": False})
        else:
            data = self.collection.find({}, {"id_": False})
            # Returns dataset, else, empty list
        return data
    
    
# Create method to implement the U in CRUD
    def update(self, findData, updateData):
        if findData is not None:
            result = self.collection.update_one(findData, { "$set": updateData})
            # Returns number of updated entries
            return result.modified_count
        else:
            return 0
        
        
# Create method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.collection.delete_one(deleteData)
            # Returns the number of deleted entried
            return result.deleted_count
        else:
            return 0
        