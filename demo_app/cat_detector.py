import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors


class CatDetector:
    """ Class for detecting cats and people on the image using YOLO model. """
    
    def __init__(self) -> None:
        self.model: YOLO = YOLO('yolov8m.pt')

    def run(self, image):
        results = self.model(image, device='cpu', conf=0.6)
        
        boxes = results[0].boxes.xyxy.cpu()
        clss = results[0].boxes.cls.cpu().tolist()
        confs = results[0].boxes.conf.cpu().tolist()
        names = results[0].names
        cat_count = clss.count(15.0)    # 15.0 is class id for cat
        people_count = clss.count(0.0)  # 0.0 is class id for person

        return cat_count, people_count, boxes, clss, confs, names



if __name__ == '__main__':  # just a demo of CatDetector
    cat_detector = CatDetector()
    image_path = 'demo_app/Girl_and_cat.jpg'

    *_, boxes, clss, confs, names = cat_detector.run(image_path)

    def annotate_image(img, boxes, clss, confs, names):
        annotator = Annotator(img, line_width=3)
        for box, cls, conf in zip(boxes, clss, confs):
            label = f"{names[int(cls)]}: {int(conf*100)}%"
            annotator.box_label(box, label=label, color=colors(int(cls), True))
        return annotator.result()

    img = cv2.imread(image_path)
    annotated_img = annotate_image(img, boxes, clss, confs, names)
    cv2.imshow('Cats & People', annotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
