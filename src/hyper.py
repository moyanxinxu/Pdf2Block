class hp:

    yolo_model_path = "./models/yolov10x_best.pt"
    layout_model_path = "./models/layout/"

    """pdf2images"""
    zoom_x = 4
    zoom_y = 4
    images_saved_path = "./images/splited/"

    """images2component"""
    component_path = "./images/component/"
    ploted_path = "./images/ploted/"

    id2label = {
        0: "Caption",
        1: "Footnote",
        2: "Formula",
        3: "List-item",
        4: "Page-footer",
        5: "Page-header",
        6: "Picture",
        7: "Section-header",
        8: "Table",
        9: "Text",
        10: "Title",
    }

    label2id = {
        "Caption": 0,
        "Footnote": 1,
        "Title": 10,
        "Formula": 2,
        "List-item": 3,
        "Page-footer": 4,
        "Page-header": 5,
        "Picture": 6,
        "Section-header": 7,
        "Table": 8,
        "Text": 9,
    }

    # 尽量使用优美的颜色
    label2color = {
        "Caption": (0, 0, 255),
        "Footnote": (0, 255, 0),
        "Formula": (255, 0, 0),
        "List-item": (0, 255, 255),
        "Page-footer": (255, 255, 0),
        "Page-header": (255, 0, 255),
        "Picture": (0, 0, 128),
        "Section-header": (255, 255, 255),
        "Table": (128, 128, 128),
        "Text": (128, 0, 0),
        "Title": (0, 128, 0),
    }

    """DataCollator"""
    max_length = 512
    cls_token_id = 0
    unk_token_id = 3
    eos_token_id = 2
