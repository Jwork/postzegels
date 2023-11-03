class Catalog:
    #catalog is an object used to represent the data files used by the application and the user to store their collection

    file_url = None


    def __init__():
        #create the object
        pass

    def load(file_location:str)->self:
        #unpack a save and instance an object from it
        #after instance is created set file_url to file_location param
        pass

    def save(self):
        #copy the current database to the file_url
        #if file_url is empty call saveas
        pass

    def saveas(file_location:str, file_name:str):
        #copy the current database to a new file_url
        #should support overwriting on confirm
        pass



    def __isChanged(self)->bool:
        #Checks if the database is different from the original save file. 
