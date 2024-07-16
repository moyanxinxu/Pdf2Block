import os

import cv2 as cv
from ultralytics import YOLO

from hyper import hp


def is_text_wrapped_by_pic(text_box, obj_labels, obj_boxes):
    """
    inputs:
        text_box:  Tuple(xmin, ymin, xmax, ymax)
        pic_boxes: List[Tuple(xmin, ymin, xmax, ymax), ...]
    return:
        is_wrapped: bool
    """

    is_wrapped = False

    for index, label in enumerate(obj_labels):
        if label == "Picture":
            pic_xmin, pic_ymin, pic_xmax, pic_ymax = map(int, tuple(obj_boxes[index]))
            text_xmin, text_ymin, text_xmax, text_ymax = map(int, text_box)

            if (
                pic_xmin < text_xmin
                and pic_ymin < text_ymin
                and pic_xmax > text_xmax
                and pic_ymax > text_ymax
            ):
                is_wrapped = True
                break

    return is_wrapped


def delete_files_in_folder(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        os.remove(file_path)


def images2component(model, images):
    """
    inputs:
        model:
            YOLO model
        images:
            list of image paths
    """
    pred = model(
        images,
        show_labels=True,
        show_conf=True,
        show_boxes=True,
    )

    delete_files_in_folder(hp.component_path)
    delete_files_in_folder(hp.ploted_path)

    index = 0

    for page_num, page in enumerate(pred):
        obj_original_image = page.orig_img  # cv.Matrix
        ploted_image = obj_original_image.copy()

        obj_labels = [hp.id2label[int(cls)] for cls in page.boxes.cls]
        obj_confidences = page.boxes.conf.tolist()
        obj_boxes = [xyxy for xyxy in page.boxes.xyxy.tolist()]

        for label, confidence, box in zip(obj_labels, obj_confidences, obj_boxes):
            if is_text_wrapped_by_pic(box, obj_labels, obj_boxes):
                continue
            else:
                index += 1
                file_name = hp.component_path + f"{index}_{label}_{confidence:.2f}.png"

                xmin, ymin, xmax, ymax = map(int, tuple(box))
                component = obj_original_image[ymin:ymax, xmin:xmax]

                cv.imwrite(file_name, component)

                ploted_image = cv.rectangle(
                    ploted_image, (xmin, ymin), (xmax, ymax), hp.label2color[label], 2
                )

                ploted_image = cv.putText(
                    ploted_image,
                    f"{label}:{confidence:.2f}",
                    (xmin, ymin),
                    cv.FONT_HERSHEY_SIMPLEX,
                    1,
                    hp.label2color[label],
                    2,
                )

        cv.imwrite(hp.ploted_path + f"{page_num}.png", ploted_image)


model = YOLO(hp.layout_llm_name_or_path)

images = [
    "../images/original_images/page-1.png",
    "../images/original_images/page-2.png",
]

images2component(model, images)
