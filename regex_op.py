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
        email_pattern= r"^(.+)(\@)(\w+)(\.)(\w{3,4})$"
        if match(email_pattern,email_address):
            return True
        else:
            return False


if __name__=='__main__':
    regex_obj=RegexOperations()
    regex_obj.validate_username(email_address='hasanasd@agmailcom.xyz')