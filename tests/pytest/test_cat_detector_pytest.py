"""

"""
import pytest
from demo_app.cat_detector import CatDetector
from tests.util import extractYoloResult

TEST_IMAGE_FILENAME = 'demo_app/Girl_and_cat.jpg' 
EXPECTED_NUMBER_OF_CATS = 1
EXPECTED_NUMBER_OF_PEOPLE = 1
EXPECTED_NUMBER_OF_OBJECTS = EXPECTED_NUMBER_OF_CATS + EXPECTED_NUMBER_OF_PEOPLE
EXPECTED_NUMBER_OF_OBJECT_TYPES = 2
MIN_CONFIDENCE = 0.5


@pytest.fixture
def cat_detector():
    return CatDetector()


def test_basic_cat_detection(cat_detector):
    result_data = cat_detector.run(TEST_IMAGE_FILENAME)
    boxes, names, clss, confs = extractYoloResult(result_data)
    cat_count = clss.count(15.0)
    people_count = clss.count(0.0)
    assert len(boxes) == EXPECTED_NUMBER_OF_OBJECTS, "Incorrect number of bounding boxes!"
    assert cat_count == EXPECTED_NUMBER_OF_CATS, "Incorrect nubmer of detected cats!"
    assert people_count == EXPECTED_NUMBER_OF_PEOPLE, "Incorrect nubmer of detected people!"
    for i in range(EXPECTED_NUMBER_OF_OBJECTS):
        assert confs[i] >= MIN_CONFIDENCE, f"Object no. {i} detected with too low confidence"
