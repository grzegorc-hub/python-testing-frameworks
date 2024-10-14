from behave import *
from demo_app.cat_detector import CatDetector
from tests.util import extractYoloResult


TEST_IMAGE_FILENAME = 'demo_app/Girl_and_cat.jpg' 


@given('we have yolo detector')
def step_given_yolo_detector(context):
    context.cat_detector = CatDetector()


@when('we perform yolo object detection on test image')
def step_perform_yolo_detection(context):
    result_data = context.cat_detector.run(TEST_IMAGE_FILENAME)
    context.detection_data = result_data


@then('we check if detection data is correct')
def step_check_detection_data(context):
    boxes, names, clss, confs = extractYoloResult(context.detection_data)
    cat_count = clss.count(15.0)
    people_count = clss.count(0.0)
    assert int(context.table[0]['value']) == len(boxes), \
        f"Incorrect number of bounding boxes! Expected: {context.table[0]['value']}, but got {len(boxes)}"
    assert int(context.table[1]['value']) == cat_count, \
        f"Incorrect number of detected robots! Expected: {context.table[2]['value']}, but got {cat_count}"
    assert int(context.table[2]['value']) == people_count, \
        f"Incorrect number of detected obstacles! Expected: {context.table[3]['value']}, but got {people_count}"
    assert int(context.table[0]['value']) == len(confs), \
        f"Incorrect size of confidence table! Expected: {context.table[0]['value']}, but got {len(confs)}"


@then(u'we check if all detections confidence is above "{min_conf}"')
def step_check_all_confidence(context, min_conf):
    confs = context.detection_data[0].boxes.conf.cpu().tolist()
    for i in range(len(confs)):
        assert confs[i] >= float(min_conf), f"Object no. {i} detected with too low confidence"
