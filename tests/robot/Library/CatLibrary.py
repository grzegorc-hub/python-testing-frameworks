from demo_app.cat_detector import CatDetector
from tests.util import extractYoloResult


def get_cat_detector():
    return CatDetector()


def run_cat_object_detection(cat_detector, image):
    result_data = cat_detector.run(image)
    return result_data


def extract_yolo_detection_data(data):
    boxes, names, clss, confs = extractYoloResult(data)
    cat_count = clss.count(15.0)
    people_count = clss.count(0.0)
    return cat_count, people_count, len(boxes)


def validate_detection_confidence_scores(data, objects_num, min_conf):
    confs = data[0].boxes.conf.cpu().tolist()
    for i in range(int(objects_num)):
        assert confs[i] >= float(min_conf), f"Object no. {i} detected with too low confidence"
