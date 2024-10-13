from ultralytics import YOLO
# from ultralytics.utils.plotting import Annotator


class CatDetector:
    def __init__(self) -> None:
        self.model: YOLO = YOLO('yolov8n.pt')

    def run(self, image):
        result = self.model(image)
        return result


if __name__ == '__main__':
    detector = CatDetector()
    r = detector.run('demo_app/cats2.jpg')
    boxes = r[0].boxes.xyxy.cpu()
    # print(r)
    print(boxes)
