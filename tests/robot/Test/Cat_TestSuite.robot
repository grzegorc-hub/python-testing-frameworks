*** Settings ***
Library        String
Library        ../Library/CatDetectorLibrary.py

*** Variables ***
${TEST_IMAGE}                         images/Girl_and_cat.jpg
${EXPECTED_NUMBER_OF_OBJECTS}         2
${EXPECTED_NUMBER_OF_CATS}            1
${EXPECTED_NUMBER_OF_PEOPLE}          1
${MINIMUM_CONFIDENCE_SCORE}           0.5


*** Test Cases ***
Cat Detection Test
    [Documentation]     Runs cats detector on given test image 
    ...                 and checks if number of detected cats and people is correct
    ${cat_detector}=    Get Cat Detector
    ${cat_count}    ${people_count}    ${objects_count}    ${confs}=       Run Cat Detector    ${cat_detector}    ${TEST_IMAGE}   
    Should Be Equal As Integers    ${cat_count}        ${EXPECTED_NUMBER_OF_CATS}
    Should Be Equal As Integers    ${people_count}     ${EXPECTED_NUMBER_OF_PEOPLE}
    Should Be Equal As Integers    ${objects_count}    ${EXPECTED_NUMBER_OF_OBJECTS}
    Validate Detection Confidence Scores     ${confs}    ${EXPECTED_NUMBER_OF_OBJECTS}     ${MINIMUM_CONFIDENCE_SCORE}     
