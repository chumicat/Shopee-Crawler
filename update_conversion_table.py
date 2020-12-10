""" Run the script to update zh_conversion.py """
import requests
import re


def __get_data_between(st_text: str, ed_text: str, ori_text: str):
    """ Get the data between specific text in string. Begin and end text not included.

    Args:
        st_text (str): Begin of the text. (Not included)
        ed_text (str): End of the text. (Not included)
        ori_text (str): Original data.

    Yields:
        (str, str): Pairs of Chinese. (Traditional, Simplified)

    Note: Though it is possible to format string in the function,
        I choose deal it in main and keep function clean.
        Also note that duplicate key might occur and will be update by new one when used.

    """
    st = ori_text.find(st_text) + len(st_text) + 1
    ed = ori_text.find(ed_text, st) - 1
    for line in ori_text[st:ed].split('\n'):
        a = re.match(r"'(.*)' => '(.*)',", line)
        yield a.group(1), a.group(2)


if __name__ == '__main__':
    # Download ZhConversion.php to text
    url = 'https://phabricator.wikimedia.org/source/mediawiki/browse/master/languages/data/ZhConversion.php?view=raw'
    r = requests.get(url, allow_redirects=True)
    text = r.text

    # Create zh_conversion.py
    with open('conversion_table.py', 'w') as file:
        file.write("zh2cn = {\n")
        for target in ['public static $zh2Hans = [', 'public static $zh2CN = [']:
            for t, s in __get_data_between(target, '];', text):
                file.write("    '{}': '{}',\n".format(t, s))
        file.write("}\n")