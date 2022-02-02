import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from env import EnvReader
from scraper import ProductScraper
        
class Command:
    """ Command line command execution  """
    
    def __init__(self):
        pass

    def runCommand(self):
        """ Run command """
        return ProductScraper.getContent(self)

     
""" Command line call """       
x = Command()
output = x.runCommand()
print(output)