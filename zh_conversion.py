import jieba
from conversion_table import zh2cn


def to_cn(ori_text: str):
    """ Convert input text to simplified Chinese.

    Args:
        ori_text (str): Original data. (Chinese)

    Returns:
        str, str: Converted data. (Simplified Chinese)

    """
    res = []
    for text in jieba.cut(ori_text):
        if text in zh2cn:
            res.append(zh2cn[text])
        else:
            for char in text:
                res.append(zh2cn.get(char, char))
    return "".join(res)


def to_cn_force(ori_text: str):
    """ Convert input text to simplified Chinese without consider vocabulary.

    Args:
        ori_text (str): Original data. (Chinese)

    Returns:
        str, str: Converted data. (Simplified Chinese)

    """
    return "".join(zh2cn.get(char, char) for char in ori_text)
