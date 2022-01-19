"""
This script is created to check for various input is valid or invalid with support of RegEx
@Hasan Özdemir 01/19/2022
"""

from re import match

class RegexOperations:

    def __init__(self) -> None:
        pass

    def is_valid_mail(self,email_address:str)->bool:
        """
        This method is created to check email is valid nor invalid
        :param email_address: <str> email address to check is valid nor invalid
        :return: <bool> Valid or Invalid
        """
        # Verify that there is an @ symbol with something before it
        email_pattern= r"^(.+)(\@)(\w+)(\.)(\w{3,4})$"
        if match(email_pattern,email_address):
            return True
        else:
            return False
    
    def is_valid_username(self,username:str)->bool:
        """
        This method is created to check username is valid nor invalid
        :param username: <str> username to check is valid nor invalid
        :return: <bool> Valid or Invalid
        """
        # A string between 3 and 20 characters, allowing alphanumeric characters and hyphens and underscores
        username_pattern=r"^[a-zA-Z0-9_-]{3,20}$"
        if match(username_pattern,username):
            return True
        else:
            return False

if __name__=='__main__':
    regex_obj=RegexOperations()
    regex_obj.is_valid_username(username='hasanasdagmaaaxxxxxa')