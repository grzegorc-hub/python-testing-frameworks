Feature: Yolo Basic Detection Test
   Runs yolo object detection on given test image and checks detection result

  Scenario: Basic Yolo detection

    Given we have yolo detector

    When we perform yolo object detection on test image

    Then we check if detection data is correct
        | property                  | value  |
        | number_of_objects         | 2      |
        | number_of_cats            | 1      |
        | number_of_people          | 1      |
    And we check if all detections confidence is above "0.8"
