# Python Testing Frameworks Comparison

One, the same testcase written using following python testing frameworks: unittest, pytest, robot framwork, behave.

## SUT (system under test)

Simple application which aim is to detect cats and people on given picture.  
To run the app type:  
`python3 cat_detector.py`

## Running tests

Use the following commands (from root directory) for each testing framework to run the tests:

### Unitest

`python -m unittest tests/unittest/test_cat_detector.py`

### Pytest

`python -m pytest tests/pytest/test_cat_detector_pytest.py`

### Robot framework

`python -m robot tests/robot/Test/Cat_TestSuite.robot`

### Behave

`python -m behave tests/behave/cat_detection.feature`
