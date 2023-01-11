#!/bin/env python
*** Settings ***
Documentation    This script is used to test APIs for a given URL.
...              This script covers Verification of Functional and non functional test cases

Resource         keywords.resource

*** Test Cases ***

TC0_Create_HTTP_Session
    [Documentation]     This test case creates HTTP session with specified url
    Create Session      api_url     ${base_url}     verify=True
    Log                 HTTP session created successfully with ${base_url}

TC1_Verify_Pagination
    [Documentation]     This test case verifies API response has pagination
    ${response}=        GET On Session      api_url     public/v1/users
    ${data}=        Set Variable        ${response.json()}
    Verify Pagination   ${data}

TC2_Verify_Response_Json_Data
    [Documentation]     This test case validates get response data is valid json
    ${response}=        GET On Session      api_url     public/v1/users
    Log to Console      Verifying JSON data is valid or not
    #Store response json data to variable for validation
    ${json_obj}=        Set Variable        ${response.json()}
    Log to Console      GET response has valid JSON format ${json_obj}

TC3_Verify_User_Email
    [Documentation]     This test case will verify email address availability in user data
    ${response}=        GET On Session      api_url     public/v1/users
    Verify Valid Email  ${response.json()}

TC4_Verify_user_data
    [Documentation]     This test case will verify all users data attributes are similar
    ${response}=        GET On Session      api_url     public/v1/users
    verify users data   ${response.json()}

TC5_Verify_get_response
    [Documentation]     This test case is to verify get response code as 200
    ${response}=        GET On Session      api_url     public/v1/users     params=access-token=${token}
    Log to Console      ${response.status_code}
    ${status_code}=     Convert to String   ${response.status_code}
    should be equal     ${status_code}      200
