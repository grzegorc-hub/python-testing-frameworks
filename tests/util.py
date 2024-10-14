
def extractYoloResult(result_data):
    boxes = result_data[0].boxes.xyxy.cpu()
    names = result_data[0].names
    clss = result_data[0].boxes.cls.cpu().tolist()
    confs = result_data[0].boxes.conf.cpu().tolist()
    return boxes, names, clss, confs