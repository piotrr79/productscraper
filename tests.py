# -*- coding: utf-8 -*-
import os
import unittest
import json
from scraper import ProductScraper

class ProductScraperTest(unittest.TestCase):
    """ Unit tests """
    
    @classmethod
    def setUpClass(self):
        """ Set test env variables """
        tests_file = 'testsPayload/VidexHomePageEnglish.html'
        full_path = os.path.abspath(tests_file)
        os.environ['PRODUCT_PAGE_URL'] = 'file:///' + full_path

    def testPageScrapeCountResults(self):
        """ Test for scraper response
            Script return success, result count is 6
        """
        product = ProductScraper()
        result = product.getContent()
        # Transform string response to proper json and next to dictionary
        json_string = result.replace("'", "\"")
        response_dict = json.loads(json_string)
        self.assertEqual(len(response_dict.keys()), 6)

    def testPageScrapeCountResultsError(self):
        """ Test for scraper response
            Script return success, result count is not 4
        """
        product = ProductScraper()
        result = product.getContent()
        # Transform string response to proper json and next to dictionary
        json_string = result.replace("'", "\"")
        response_dict = json.loads(json_string)
        self.assertNotEqual(len(response_dict.keys()), 4)

    def testPageScrapeCompareResults(self):
        """ Test for scraper response
            Script return success, response is like asserts
        """
        product = ProductScraper()
        result = product.getContent()
        # Transform string response to proper json and next to dictionary
        json_string = result.replace("'", "\"")
        response_dict = json.loads(json_string)

        # Check response dictionary by keys against option names
        self.assertEqual(response_dict.get('0').get('Option title'), 'Option 40 Mins')
        self.assertEqual(response_dict.get('1').get('Option title'), 'Option 160 Mins')
        self.assertEqual(response_dict.get('2').get('Option title'), 'Option 300 Mins')
        self.assertEqual(response_dict.get('3').get('Option title'), 'Option 480 Mins')
        self.assertEqual(response_dict.get('4').get('Option title'), 'Option 2000 Mins')
        self.assertEqual(response_dict.get('5').get('Option title'), 'Option 3600 Mins')

    @classmethod
    def tearDownClass(self):
        """ Clear env variable after tests """
        os.environ['PRODUCT_PAGE_URL'] = ''
        
if __name__ == '__main__':
    unittest.main()