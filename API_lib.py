#!/bin/env python
###########################################################################################
#    Main Description:  This script used as lib file for API testing
###########################################################################################
import requests
import json
import datetime
import re
import sys
from time import time

def Testwrapper(func):
    def wrapper(*args, **kwargs):
        print("\n======================================================================\n")
        print(f'Starting execution of Testcase {func.__name__}')
        start = time()
        try:
            result = func(*args, **kwargs)
        except:
            print("Oops! Error ", sys.exc_info()[0], "occurred while executing Testcase")
            result = 0
        end = time()
        print(f'Completing execution of Testcase {func.__name__}')
        print(f'{func.__name__} Testcase execution time {end-start}')
        if result:
            print(f'{func.__name__} test Result : PASS')
        else:
            print(f'{func.__name__} test Result : FAIL')
        print("\n======================================================================\n")
    return wrapper

def get_request(url, **kwargs):
    if 'param' in kwargs:
        res = requests.get(url, params=kwargs['param'])
    else:
        res = requests.get(url)
    if res.ok:
        return res
    else:
        print("FAIL: API GET request failed")
        return None

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    match = re.match(pattern,email)
    if match:
        return 1
    else:
        return 0