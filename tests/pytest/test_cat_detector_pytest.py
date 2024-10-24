"""
Test for CatDetector class. It runs CatDetector on test image and checks if detection result is correct, 
that is e.g number of detected cats should be equal to actual number of cats on the image.
"""
import pytest
from demo_app.cat_detector import CatDetector

TEST_IMAGE_FILENAME = 'demo_app/Girl_and_cat.jpg' 
EXPECTED_NUMBER_OF_CATS = 1
EXPECTED_NUMBER_OF_PEOPLE = 1
EXPECTED_NUMBER_OF_OBJECTS = EXPECTED_NUMBER_OF_CATS + EXPECTED_NUMBER_OF_PEOPLE
MIN_CONFIDENCE = 0.5


@pytest.fixture
def cat_detector():
    return CatDetector()


def test_basic_cat_detection(cat_detector):
    cat_count, people_count, boxes, _, confs, _ = cat_detector.run(TEST_IMAGE_FILENAME)

    assert cat_count == EXPECTED_NUMBER_OF_CATS, "Incorrect nubmer of detected cats!"
    assert people_count == EXPECTED_NUMBER_OF_PEOPLE, "Incorrect nubmer of detected people!"
    assert len(boxes) == EXPECTED_NUMBER_OF_OBJECTS, "Incorrect number of bounding boxes!"
    for i in range(EXPECTED_NUMBER_OF_OBJECTS):
        assert confs[i] >= MIN_CONFIDENCE, f"Object no. {i} detected with too low confidence"
