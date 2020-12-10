## Issue
Try to finish this project via Python:
Use below Wikipedia Simplified / Traditional Chinese conversion tables to create a Python converter.
https://phabricator.wikimedia.org/source/mediawiki/browse/master/languages/data/ZhConversion.php

Then you need to write a crawler which will get product title and price from the EC website and use the above-mentioned converter table to perform the conversion from traditional Chinese to simplified Chinese
https://shopee.tw/%E7%8E%A9%E5%85%B7-cat.75.2185?brands=5005&locations=-1&page=0&ratingFilter=4


      
## Environment setting
1. Required package  
   ```bash
   pip3 install requests
   pip3 install jieba
   pip3 install selenium
   pip3 install beautifulsoup4
   ```
   
2. Chrome Driver  
   This is required by selenium. Download the Chrome Driver [here](https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.88/)  
   Please replace the driver in the project root, i.e. /Shopee-Crawler/chromedriver  
   [pypi selenium](https://pypi.org/project/selenium/) for selenium information.  
   

## Usage
   1. Run the code:
   ```bash
   python3 crawler
   ```
   2. Get the result in /result.csv:
   ![](https://i.imgur.com/t5PapWU.png)


## Implement Note
1. **Current get only one page**  
   Currently I let the program read only one page, or demonstrate might cost too much time.  
   It's convenience to change query in url to get other pages.  
   

2. **Use table zh2Hans and table zh2CN**  
   There are several tables in the ZhConversion.php:    
   * zh2Hant: Simplified Chinese to Traditional Chinese  
   * zh2Hans: Traditional Chinese to Simplified Chinese  
   * zh2TW: Local vocabulary of Taiwan  
   * zh2HK: Local vocabulary of HongKong  
   * zh2CN: Local vocabulary of China  
   
   Since we are going to convert traditional Chinese to Simplified Chinese, we use zh2Hans and zh2CN.  
   We can find the usage [here](https://phabricator.wikimedia.org/source/mediawiki/browse/master/includes/language/converters/ZhConverter.php).  
   

3. **Split input string**  
   We can find that there is some mapping didn't change the word.  
   Take an example in the table zh2Hant, we can find rule `‘王后’ ＝> '王后'`.  
   The reason these rules exist is to prevent rule `'后' => '後'` since `'王后'` is correct and `'王後'` isn't.  
   Let me take some ideas to deal with this:  
   1. **Match as long as possible**  
      Find the maximum string from start of the input.  
   2. **Tokenize**  
      Use Tokenize library such as Jieba or tokenizer.  
      This is the way I implement.  
      