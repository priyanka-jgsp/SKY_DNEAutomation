#!/bin/env python
###########################################################################################
#    Main Description:  This script used to test an API
#
#    Details:  Verification of Functional and non functional test cases
#
###########################################################################################

import json
import os
import sys
import requests
import re
import inspect
from Lib.API_lib import *


class Test_API:
    """
    This Class verifies all functional and Non functional test cases of API testing
    """

    def __init__(self, url):
        self.url = url

    @Testwrapper
    def TC5_Verify_get_response(self):
        """
        This method used to verify get response code as 200
        :return: 1 if pass else return 0
        """
        resp = get_request(self.url)
        if resp.status_code == 200:
            print('HTTP GET response successful')
            return 1
        else:
            print('HTTP GET response failed')
            return 0
        pass

    @Testwrapper
    def TC2_Verify_response_data(self):
        """
        This method validates get response data is valid json
        :return: 1 if pass else return 0
        """
        resp = get_request(self.url)
        try:
            valid_data = resp.json()
            print('PASS: API response has valid JSON data')
            return 1
        except:
            print('FAIL: API response has invalid JSON data')
            return 0
        pass

    @Testwrapper
    def TC1_Verify_pagination(self):
        """
        This test case verifies API response has pagination
        :return: 1 if pass else return 0
        """
        response = get_request(self.url)
        res = response.json()
        print(f'Response data from {self.url} : {res}')
        if 'pagination' in res['meta'].keys():
            print(f'PASS: {self.url} API response has pagination')
            return 1
        else:
            print(f'FAIL: {self.url} API response doesn\'t have pagination')
            return 0
        pass

    @Testwrapper
    def TC3_Verify_user_email(self):
        """
        This test case will verify email address availability in user data
        :return: 1 if pass else return 0
        """
        response = get_request(self.url)
        res = response.json()
        result = 1
        print('Verify email in user data')
        for user in res['data']:
            if not validate_email(user.setdefault('email', '')):
                print('FAIL: %s has invalid email' % user['name'])
                result = 0
        print('PASS: All users have valid email address')
        return result

    @Testwrapper
    def TC4_Verify_user_data(self):
        """
        This test case will verify all users data attributes are similar
        :return: 1 if pass else return 0
        """
        response = get_request(self.url)
        res = response.json()
        result = 1
        print('Verify user data attributes')
        for i in range(len(res['data'])):
            if set(res['data'][0]) != set(res['data'][i]):
                print('FAIL: Users not having similar data attributes')
                return 0
        else:
            print('PASS: Users have similar data attributes')
            return 1
        pass


if __name__ == "__main__":
    input_file = os.path.join(sys.path[0], 'input_data.json')
    with open(input_file) as f:
        params = json.load(f)
    api_under_test = Test_API(params['url'])
    attrs = (getattr(api_under_test, name) for name in dir(api_under_test))
    methods = filter(inspect.ismethod, attrs)
    for testcase in methods:
        if not testcase.__name__ == "__init__":
            testcase()