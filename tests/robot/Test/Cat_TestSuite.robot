*** Settings ***
Library        String
Library        ../Library/CatLibrary.py

*** Variables ***
${TEST_IMAGE}                         demo_app/Girl_and_cat.jpg
${EXPECTED_NUMBER_OF_OBJECTS}         2
${EXPECTED_NUMBER_OF_CATS}            1
${EXPECTED_NUMBER_OF_PEOPLE}          1
${MINIMUM_CONFIDENCE_SCORE}           0.5



*** Test Cases ***
Yolo Basic Detection Test
    [Documentation]           Runs yolo object detection on given test image and checks detection result
    ${cat_detector}=          Get Cat Detector
    ${detection_data}=        Run Cat Object Detection    ${cat_detector}    ${TEST_IMAGE}   
    ${cat_count}    ${people_count}    ${objects_count}=    Extract Yolo Detection Data     ${detection_data} 
    Should Be Equal As Integers    ${cat_count}        ${EXPECTED_NUMBER_OF_CATS}
    Should Be Equal As Integers    ${people_count}     ${EXPECTED_NUMBER_OF_PEOPLE}
    Should Be Equal As Integers    ${objects_count}    ${EXPECTED_NUMBER_OF_OBJECTS}
    Validate Detection Confidence Scores     ${detection_data}    ${EXPECTED_NUMBER_OF_OBJECTS}     ${MINIMUM_CONFIDENCE_SCORE}     
