import unittest
from models import news
from flask import *

News = news.News

class NewsTest(unittest.TestCase):
    '''
    Class to test the behaviour of the news class
    '''
    
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        
        self.new_news = News(1,'bbc','This is our news','www.bbcnews.co.ke','sports','English','Kenya' )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        
if __name__ == '__main__':
    unittest.main()