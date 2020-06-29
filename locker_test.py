import unittest 
from locker import User
from locker import Credentials
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Method to run before each user test cases.
        '''
        self.new_user = User("FeistyDory","210sda38")
