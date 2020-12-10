from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from zh_conversion import to_cn
import time

url = 'https://shopee.tw/%E7%8E%A9%E5%85%B7-cat.75.2185?brands=5005&locations=-1&page=0&ratingFilter=4'
output = 'result.csv'

if __name__ == '__main__':
    # Disable pop out ads / screen
    options = Options()
    options.add_argument("--disable-notifications")

    # Launch the page and simulate scroll down for js loading
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get(url)
    for x in range(0, 4001, 400):
        chrome.execute_script("window.scrollTo(0,{})".format(x))
        time.sleep(1)

    # Extract item list
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    items = soup.find_all('div', {'class': '_3eufr2'})

    # Extract title and price, write to output.csv
    # Price might have two values, so I extract the total string
    # Price have ',' to divide value in three digits, remove them
    with open(output, 'w') as file:
        for item in items:
            try:
                title = item.find(class_='_1NoI8_ _16BAGk').get_text()
                price = item.find(class_='_1w9jLI _37ge-4 _2ZYSiu').get_text()
                file.write("{}, {}\n".format(to_cn(title), price.replace(',', '')))
            except BaseException:
                pass
