"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from argparse import ArgumentParser
from sys import argv

class HelperJson:

    def fetch_dict(self,item)->list:
        """
        This method used to fetch each item of dir_json file
        :param item: <dict> Each item of dir_json
        """
        try:
            id=item['id']
            username=item['username']
            p_name=item['profile']['name']
            p_dob=item['profile']['dob']
            p_address=item['profile']['address']
            p_l_lat=item['profile']['location']['lat']
            p_l_long=item['profile']['location']['long']
            api_key=item['apiKey']
            # return fetched item as list
            return [id,username,p_name,p_dob,p_address,p_l_lat,p_l_long,api_key]
        except KeyError as error:
            # TODO 
            pass