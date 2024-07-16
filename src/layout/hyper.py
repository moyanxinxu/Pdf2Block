class hp:
    layout_llm_name_or_path = "../model/layout/yolov10b-doclaynet.pt"
    component_path = "../images/component_images/"
    ploted_path = "../images/ploted_images/"
    confidence_threshold = 0.4

    """
    0: "Caption": 图片或表格的标题说明文字。
    1: "Footnote": 脚注，位于页面底部，对正文内容进行补充说明。
    2: "Formula": 数学公式。
    3: "List-item": 列表项，例如无序列表或有序列表中的项目。
    4: "Page-footer": 页脚，位于页面底部，通常包含页码、日期等信息。
    5: "Page-header": 页眉，位于页面顶部，通常包含文档标题、章节标题等信息。
    6: "Picture": 图片。
    7: "Section-header": 章节标题，用于划分文档的不同部分。
    8: "Table": 表格，以行列形式组织数据。
    9: "Text": 正文文本，不属于其他任何类别的文本内容。
    10: "Title": 文档标题，通常是文档中字体最大、最醒目的部分。
    """

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
        "Picture": (0, 0, 0),
        "Section-header": (255, 255, 255),
        "Table": (128, 128, 128),
        "Text": (128, 0, 0),
        "Title": (0, 128, 0),
    }
