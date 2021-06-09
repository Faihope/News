import unittest
from app.models import Source
# from app import app



# Source = source.Source

class NewsTest(unittest.TestCase):
    '''
    Class to test the behaviour of the news class
    '''
    
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        
        self.new_source = Source(1,'bbc','This is our news','www.bbcnews.co.ke','sports','English','Kenya' )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
        
