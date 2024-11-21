Feature: Cat Detector Test
  Runs cats detector on given test image and checks if number of detected cats and people is correct
  
  Scenario: Cat and people detection
    Given we have cat detector
    When we perform cat detection on test image "images/Girl_and_cat.jpg" 
    Then we check if detection data is correct
        | property                  | value  |
        | number_of_objects         | 2      |
        | number_of_cats            | 1      |
        | number_of_people          | 1      |
    And we check if all detections confidence is above "0.5"
