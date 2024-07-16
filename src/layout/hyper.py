class hp:
    layout_llm_name_or_path = "../model/layout/yolov10b-doclaynet.pt"

    id2label = {
        0: "Caption",
        1: "Footnote",
        10: "Title",
        2: "Formula",
        3: "List-item",
        4: "Page-footer",
        5: "Page-header",
        6: "Picture",
        7: "Section-header",
        8: "Table",
        9: "Text",
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
