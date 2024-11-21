"""
Test for CatDetector class. It runs CatDetector on test image and checks if detection result is correct, 
that is e.g number of detected cats should be equal to actual number of cats on the image.
"""
import unittest
from demo_app.cat_detector import CatDetector


class TestCatDetector(unittest.TestCase):
    TEST_IMAGE_FILENAME = 'images/Girl_and_cat.jpg'
    EXPECTED_NUMBER_OF_CATS = 1
    EXPECTED_NUMBER_OF_PEOPLE = 1
    EXPECTED_NUMBER_OF_OBJECTS = EXPECTED_NUMBER_OF_CATS + EXPECTED_NUMBER_OF_PEOPLE
    MIN_CONFIDENCE = 0.5

    def setUp(self):
        self.cat_detector = CatDetector()

    def test_basic_yolo_detection(self):
        cat_count, people_count, boxes, _, confs, _ = self.cat_detector.run(self.TEST_IMAGE_FILENAME)
        
        self.assertEqual(cat_count, self.EXPECTED_NUMBER_OF_CATS, "Incorrect nubmer of detected cats!")
        self.assertEqual(people_count, self.EXPECTED_NUMBER_OF_PEOPLE, "Incorrect nubmer of detected people!")
        self.assertEqual(len(boxes), self.EXPECTED_NUMBER_OF_OBJECTS, "Incorrect number of bounding boxes!")
        for i in range(self.EXPECTED_NUMBER_OF_OBJECTS):
            self.assertGreaterEqual(confs[i], self.MIN_CONFIDENCE, f"Object no. {i} detected with too low confidence")

    def tearDown(self):
        ...

