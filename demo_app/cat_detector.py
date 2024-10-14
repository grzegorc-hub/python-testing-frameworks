from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import cv2


class CatDetector:
    def __init__(self) -> None:
        self.model: YOLO = YOLO('yolov8m.pt')

    def run(self, image):
        return self.model(image, device='cpu', conf=0.6)


def annotate_image(img, results):
    boxes = results[0].boxes.xyxy.cpu()
    clss = results[0].boxes.cls.cpu().tolist()
    confs = results[0].boxes.conf.cpu().tolist()
    names = results[0].names
    annotator = Annotator(img, line_width=3)
    for box, cls, conf in zip(boxes, clss, confs):
        label = f"{names[int(cls)]}: {int(conf*100)}%"
        annotator.box_label(box, label=label, color=colors(int(cls), True))
    return annotator.result()


if __name__ == '__main__':
    detector = CatDetector()
    image_path = 'demo_app/Girl_and_cat.jpg'

    results = detector.run(image_path)

    img = cv2.imread(image_path)
    annotated_img = annotate_image(img, results)
    cv2.imshow('Annotated Image', annotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
