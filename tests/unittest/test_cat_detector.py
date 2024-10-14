"""
Module test for CatDetector class.
It runs CatDetector on predefined test image and then it checks if detection output is as expected, that is e.g
number of detected cats by CatDetector should be equal to actual number of cats on the image
"""
import unittest
from demo_app.cat_detector import CatDetector
from tests.util import extractYoloResult


class TestCatDetector(unittest.TestCase):
    TEST_IMAGE_FILENAME = 'demo_app/Girl_and_cat.jpg' 
    EXPECTED_NUMBER_OF_CATS = 1
    EXPECTED_NUMBER_OF_PEOPLE = 1
    EXPECTED_NUMBER_OF_OBJECTS = EXPECTED_NUMBER_OF_CATS + EXPECTED_NUMBER_OF_PEOPLE
    EXPECTED_NUMBER_OF_OBJECT_TYPES = 2
    MIN_CONFIDENCE = 0.5

    def setUp(self):
        self.cat_detector = CatDetector()

    def test_basic_yolo_detection(self):
        result_data = self.cat_detector.run(self.TEST_IMAGE_FILENAME)
        boxes, names, clss, confs = extractYoloResult(result_data)
        cat_count = clss.count(15.0)
        people_count = clss.count(0.0)
        self.assertEqual(len(boxes), self.EXPECTED_NUMBER_OF_OBJECTS, "Incorrect number of bounding boxes!")
        self.assertEqual(cat_count, self.EXPECTED_NUMBER_OF_CATS, "Incorrect nubmer of detected cats!")
        self.assertEqual(people_count, self.EXPECTED_NUMBER_OF_PEOPLE, "Incorrect nubmer of detected people!")
        for i in range(self.EXPECTED_NUMBER_OF_OBJECTS):
            self.assertGreaterEqual(confs[i], self.MIN_CONFIDENCE, f"Object no. {i} detected with too low confidence")

    def tearDown(self):
        ...

