class Helper:

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
