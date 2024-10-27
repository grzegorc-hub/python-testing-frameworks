from behave import *
from demo_app.cat_detector import CatDetector


@given('we have cat detector')
def step_given_cat_detector(context):
    context.cat_detector = CatDetector()


@when('we perform cat detection on test image "{test_image_path}"')
def step_perform_yolo_detection(context, test_image_path):
    cat_count, people_count, boxes, _, confs, _ = context.cat_detector.run(test_image_path)
    context.cat_count = cat_count
    context.people_count = people_count
    context.object_count = len(boxes)
    context.confs = confs


@then('we check if detection data is correct')
def step_check_detection_data(context):
    assert int(context.table[0]['value']) == context.object_count, \
        f"Incorrect number of bounding boxes! Expected: {context.table[0]['value']}, but got {context.object_count}"
    assert int(context.table[1]['value']) == context.cat_count, \
        f"Incorrect number of detected robots! Expected: {context.table[2]['value']}, but got {context.cat_count}"
    assert int(context.table[2]['value']) == context.people_count, \
        f"Incorrect number of detected obstacles! Expected: {context.table[3]['value']}, but got {context.people_count}"
    assert int(context.table[0]['value']) == len(context.confs), \
        f"Incorrect size of confidence table! Expected: {context.table[0]['value']}, but got {len(context.confs)}"


@then(u'we check if all detections confidence is above "{min_conf}"')
def step_check_all_confidence(context, min_conf):
    for i in range(len(context.confs)):
        assert context.confs[i] >= float(min_conf), f"Object no. {i} detected with too low confidence"
