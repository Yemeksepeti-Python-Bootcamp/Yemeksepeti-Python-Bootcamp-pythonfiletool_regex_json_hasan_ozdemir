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

