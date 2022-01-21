"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from argparse import ArgumentParser
from sys import argv

class HelperRegex:

    def is_leap_year(self,year:int)->bool:
        """
        This method is created to check year whether is leap nor not leap
        :param year: <int> year
        :return: <bool> Leap  or Not Leap
        """
        if (year%400==0) or ((year%100==0) and (year%4==0)):
            return True

        else:
            return False


class HelperDb:

    def __init__(self) -> None:
        """
        This constructor is created to get named command line args.
        return : None
        """
        # initialize Argument parser
        parser=ArgumentParser()
        # prepare named arguments
        parser.add_argument('--file',help='Json file path',type=str)
        parser.add_argument('--db',help='Database file path',type=str)
        # get the named command line arguments
        self.json_path=parser.parse_args().file
        self.db_path=parser.parse_args().db


class HelperJson:


    def fetch_dict(self,item)->list:
        """
        This method used to fetch each item of json file
        :param item: <dict> Each item of json
        """
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