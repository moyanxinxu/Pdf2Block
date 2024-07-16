from ultralytics import YOLO

from hyper import hp


def images2layout(model, images):
    """
    inputs:
        model:
            YOLO model
        images:
            list of image paths
    returns:
        results:
            list of dict
            {
                "labels": list of str,
                "confidences": list of float,
                "boxes": list of list of float
            }
    """
    results = []
    pred = model(
        images,
        show_labels=True,
        show_conf=True,
        show_boxes=True,
    )
    for entry in pred:
        result = {}
        # print(entry.boxes)

        obj_labels = [hp.id2label[int(cls)] for cls in entry.boxes.cls]
        obj_confidences = entry.boxes.conf.tolist()
        obj_boxes = [xyxy for xyxy in entry.boxes.xyxy.tolist()]

        result["labels"] = obj_labels
        result["confidences"] = obj_confidences
        result["boxes"] = obj_boxes

        results.append(result)
    return results