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

    def is__valid_name_surname(self,name:str,surname:str)->bool:
        """
        This method is created to check name and surname are valid nor invalid
        :param name: <str> name to check is valid nor invalid
        :param surname: <str> surname to check is valid nor invalid
        :return: <bool> Valid or Invalid
        """
        # # A string between 3 and 20 characters, allowing only characters
        name_surname_pattern=r"^[a-zA-Z]{3,20}$"
        if match(name_surname_pattern,name) and match(name_surname_pattern,surname):
            return True
        else:
            return False
            
    #TODO 1
    def is_valid_username_email(self,username:str,mail:str)->bool:
        pass
    
    def is_valid_namesurname_username(self,name:str,surname:str,username:str)->bool:
        # create substring with name & surname
        sub_name=[name[i:i+4] for i in range(len(name)-4)]
        sub_surname=[surname[i:i+4] for i in range(len(surname)-4)]
        # check any part of substring is passing in username
        if (any([True if item in username else False for item in sub_name])) or (any([True if item in username else False for item in sub_surname])):
            return True
        else:
            return False
    #TODO 3
    def is_valid_birth_year(self,birth_year:str)->bool:
        pass

    #TODO 4
    def is_valid_birth_month(self,birth_month:str)->bool:
        pass

    #TODO 5
    def is_valid_birthday(self,birthday:str)->bool:
        pass

if __name__=='__main__':
    regex_obj=RegexOperations()
    # regex_obj.is__valid_name_surname(name='hasanasdagmaaaxxxxxa',surname='ozdemir')
    # regex_obj.is_valid_namesurname_username('hasan','ozdemir','cancancan')