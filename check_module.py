from module_api import *
from template import template
import os
import time


def check():
   while True:
       template()
       print("")
       value_bitcoin()
       infos()
       time.sleep(59)
       os.system("clear")
