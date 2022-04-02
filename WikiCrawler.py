import time

from selenium.webdriver.support.wait import WebDriverWait

import AlignmentNews
import ChromeDriver
from bs4 import BeautifulSoup

import SeparateDocumentToSentences
import Utility
import re
import json
import pdb
"""
    Zero
"""
def getWikiPostLinks(language):
    driver = ChromeDriver.getChromeDriver()

    if language == "vi":
        driver.get("https://vi.wikipedia.org/wiki/Trang_Ch%C3%ADnh")
        baseUrl = "https://vi.wikipedia.org"
    if language == "zh":
        driver.get("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")
        baseUrl = "https://zh.wikipedia.org"
    if language == "lo":
        driver.get("https://lo.wikipedia.org/wiki/%E0%BB%9C%E0%BB%89%E0%BA%B2%E0%BA%AB%E0%BA%BC%E0%BA%B1%E0%BA%81")
        baseUrl = "https://lo.wikipedia.org"
    if language == "km":
        driver.get("https://km.wikipedia.org/wiki/%E1%9E%91%E1%9F%86%E1%9E%96%E1%9F%90%E1%9E%9A%E1%9E%8A%E1%9E%BE%E1%9E%98")
        baseUrl = "https://km.wikipedia.org"

    html = driver.page_source
    html = BeautifulSoup(html,"xml")
    div = html.find("div", {"id": "bodyContent"})
    list_link = div.findAll("a")

    list_link = list(x for x in list_link for k, v in x.attrs.items() if k == "href")
    list_link = list(x["href"] for x in list_link if x["href"].startswith("/wiki/"))

    list_link = list(dict.fromkeys(list_link))
    vi_punctuation = list(SeparateDocumentToSentences.getPunctuationForLanguage("en").keys())

    start  = 0
    lim = len(list_link)
    while (start < lim):
        driver.get(baseUrl+list_link[start])
        

        html = driver.page_source
        html = BeautifulSoup(html, "xml")
        div = html.find("div", {"id": "bodyContent"})

        if not div:
            start = start + 1
            continue

        p_tags = div.findAll('p')

        aTags = div.findAll("a")
        aTags = list(x for x in aTags for k, v in x.attrs.items() if k == "href")
        aTags = list(x["href"] for x in aTags if x["href"].startswith("/wiki/"))
        aTags = list(dict.fromkeys(aTags))

        for aTag in aTags:
            if(aTag not in list_link):
                list_link.append(aTag)

        document = ""

        for p_tag in p_tags:
            document += p_tag.text+"\n"

        document = Utility.formatSentence(document)
        document = SeparateDocumentToSentences.slpit_text(document, vi_punctuation)

        if language != "vi":
            document = AlignmentNews.sentencesSegmentation(document, language)

        if language == "vi":
            f = open("Wiki-vi", "a", encoding="utf-8")

        if language == "zh":
            f = open("Wiki-zh", "a", encoding="utf-8")

        if language == "km":
            f = open("Wiki-km", "a", encoding="utf-8")

        if language == "lo":
            f = open("Wiki-lo", "a", encoding="utf-8")


        f.write("{}\n".format(document))

        f.close()
        #pdb.set_trace()
        time.sleep(0.8)
        lim = len(list_link)

        start = start + 1

    driver.delete_all_cookies()
    driver.close()

def get():
    driver = ChromeDriver.getChromeDriver()
    base_url = ".html"

    driver.get("http://www.dzwww.com/")


    html = driver.page_source
    html = BeautifulSoup(html, 'html.parser')
    list_link = html.findAll("a")
    """
    button = driver.find_element_by_class_name("u-btn")
    
    while True:

        button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name("u-btn"))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        if button.get_attribute("disabled"):
            break
        button.click()
        print("lap")
        time.sleep(2)
    print("bat dau tai bai viet")
    if not list_link:
        time.sleep(3)
        html = driver.page_source
        list_link = html.findAll("a")
    """
    #pdb.set_trace()
    list_link = list(x for x in list_link for k, v in x.attrs.items() if k == "href")
    list_link = list(x["href"] for x in list_link if
                     base_url in x["href"] and
                     not ".jpg" in x["href"] and
                     not "ads" in x["href"] and
                     not ".JPG" in x["href"]
                     #not "ln." in x["href"] and
                     #not "pic." in x["href"] and
                     #not "kan." in x["href"] and
                     #not "caijing." in x["href"]
                     )
    list_link = list(dict.fromkeys(list_link))
    start = 0
    lim = len(list_link)
    vi_punctuation = list(SeparateDocumentToSentences.getPunctuationForLanguage("en").keys())

    while (start < lim):

        if html:
            document = html.text

            document = Utility.formatSentence(document)
            document = SeparateDocumentToSentences.slpit_text(document, vi_punctuation)

            f = open("zh", "a", encoding="utf-8")

            f.write("{}\n".format(document))

            f.close()
        if list_link[start]:


            try:

                if list_link[start].startswith("//"):
                    list_link[start] = list_link[start].replace("//","")
                if list_link[start].startswith("/"):
                    list_link[start] = re.sub("^/","https://www.yicai.com/", list_link[start])

                print(list_link[start])
                driver.get(list_link[start])
            except:
                #pdb.set_trace()
                start = start + 1
                continue
        """
        if "http://www.dzwww.com/" not  in driver.current_url :
            start = start + 1
            continue
        """
        html = driver.page_source
        html = BeautifulSoup(html, 'html.parser')
        aTags = html.findAll("a")

        if not aTags:
            time.sleep(1)

            html = driver.page_source
            html = BeautifulSoup(html, 'html.parser')
            aTags = html.findAll("a")

            if  aTags:
                print("Tim thấy : {} link".format(len(aTags)))
                aTags = list(x for x in aTags for k, v in x.attrs.items() if k == "href")
                aTags = list(x["href"] for x in aTags if
                     base_url in x["href"] and
                     not ".jpg" in x["href"] and
                     not ".JPG" in x["href"]
                     #not "ln." in x["href"] and
                     #not "pic." in x["href"] and
                     #not "kan." in x["href"] and
                     #not "caijing." in x["href"]
                     )

                for aTag in aTags:
                    if (aTag not in list_link):
                        list_link.append(aTag)


        start = start + 1
    driver.close()

if __name__ == '__main__':
    pdb.set_trace()