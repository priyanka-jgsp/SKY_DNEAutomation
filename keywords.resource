*** Settings ***
Documentation   This is a resource file, that contains variables and keywords.
...             Keywords defined here can be used where this Keywords.resource in loaded.
Library         RequestsLibrary
Library         JSONLibrary
Library         Collections
Library         API_lib.py

*** Variables ***
${base_url}     https://gorest.co.in/
${token}        xxx

*** Keywords ***
Verify Pagination
    [Arguments]     ${data}
    should contain  ${data}.meta     pagination

Verify Valid Email
    [Arguments]     ${data}
    ${users}=       get value from json  ${data}      $.data
    FOR     ${user}     IN  @{users}[0]
        ${email}=       evaluate    ${user}.get("email"," ")
        ${resp}=        validate email     ${email}
        Run Keyword And Continue On Failure     should be equal     ${resp}     ${True}
    END

Verify Users Data
    [Arguments]  ${data}
    ${users}=           get value from json  ${data}      $.data
    ${users_count}=     get length  ${users}[0]
    ${user_keys}=       get dictionary keys  ${users}[0][0]
    Log to Console  ${user_keys}
    FOR     ${i}    IN RANGE        ${users_count}
        ${keys}=        get dictionary keys  ${users}[0][${i}]
        lists should be equal       ${user_keys}    ${keys}     ignore_order=True
    END
