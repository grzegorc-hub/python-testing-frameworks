from demo_app.cat_detector import CatDetector


def get_cat_detector():
    return CatDetector()


def run_cat_detector(cat_detector, image):
    cat_count, people_count, boxes, _, confs, _ = cat_detector.run(image)
    return cat_count, people_count, len(boxes), confs


def validate_detection_confidence_scores(confs, objects_num, min_conf):
    for i in range(int(objects_num)):
        assert confs[i] >= float(min_conf), f"Object no. {i} detected with too low confidence"
