"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from argparse import ArgumentParser
from sys import argv,path


class HelperRegex:

    def is_leap_year(self,year:str)->bool:
        """
        This method is created to check year whether is leap nor not leap
        :param year: <int> year
        :return: <bool> Leap  or Not Leap
        """
        try:
            year=int(year)
            if (year%400==0) or ((year%100==0) and (year%4==0)) and year:
                return True
            else:
                return False
        except ValueError as error:
            #TODO value error log tbd
            pass



if __name__=='__main__':
    try:
        # object initialization
        regex_obj=HelperRegex()
        # method calling
        regex_obj.is_leap_year('100')
    except Exception as error:
        #TODO missing argument log tbd
        pass
