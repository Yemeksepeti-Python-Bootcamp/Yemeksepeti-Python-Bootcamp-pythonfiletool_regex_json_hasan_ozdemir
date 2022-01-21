"""
This script is created make CRUD operations on json files.
@Hasan Özdemir 01/18/2022
"""
from json import load
from helper import HelperJson

class JsonCrud(HelperJson):

    def __init__(self) -> None:
        """
        This constructor is used to initialize json_data list object
        """
        self.json_data:list=list()

    def read_json(self,json_path:str)->list:
        """
        This method is used to read data from json files
        :param json_path: <str> path of json file to read
        :return: <list> data fetched from given json file
        """
        with open(json_path) as json_file:
            json_data=load(json_file)
            # loop through json items
            for item in json_data:
                # check the each key is that existed 
                if item['id'] and item['email'] and item['username'] and item['profile']['name'] and item['profile']['dob'] and item['profile']['address'] and item['profile']['location']['lat'] and item['profile']['location']['long'] and item["apiKey"]:
                    # fetch all field from json seperately
                    data_seperated=self.fetch_dict(item)
                    # append to list
                    self.json_data.append(data_seperated)  
            # context manager with close automatically file but lets make it sure for closing file
            json_file.close()      
        return (self.json_data)
            

        
if __name__=='__main__':
    j_obj=JsonCrud()
    j_obj.read_json("dataregex.json")