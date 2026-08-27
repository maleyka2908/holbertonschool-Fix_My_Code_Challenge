#!/usr/bin/python3
"""
3. User password
"""
import hashlib


class User:
    """ User class """
    def __init__(self):
        """: Initialization """
        self.__email = None
        self.__password = None

    @property
    def email(self):
        """ Email getter """
        return self.__email

    @email.setter
    def email(self, email):
        """ Email setter """
        if not isinstance(email, str):
            raise TypeError("email must be a string")
        self.__email = email

    @property
    def password(self):
        """ Password getter """
        return self.__password

    @password.setter
    def password(self, password):
        """ Password setter """
        if not isinstance(password, str):
            raise TypeError("password must be a string")
        self.__password = hashlib.md5(password.encode()).hexdigest()

    def is_valid_password(self, password):
        """ Validates password """
        if not isinstance(password, str):
            return False
        return hashlib.md5(password.encode()).hexdigest() == self.__password


if __name__ == "__main__":
    u = User()
    u.email = "bob@holbertonschool.com"
    u.password = "root"
    print(u.email)
    if u.is_valid_password("root"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("is_valid_password should return False if it's the wrong password")
