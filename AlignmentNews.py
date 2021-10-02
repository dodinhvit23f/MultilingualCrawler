import pdb
import time
import urllib
from multipledispatch import dispatch
from selenium.webdriver.support.ui import WebDriverWait
import ChromeDriver
import Utility
import configparser
@dispatch(str, str, list)
def translate(src_lang, tgt_lang, list_text):
    list_transed_text = list()
    # sl la nguon ngu nguon
    # tl la nguon ngu dich

    count = 1
    search_text = ""
    sign = ";"
    # f = open("link.test.txt", "w", encoding="utf-8")
    loop = 0

    driver = ChromeDriver.getChromeDriver()
    print(len(list_text))
    try:
        for text in list_text:
            rawtext = text
            text = text.replace("?", "").replace(".", "？").replace(".", "")
            print(loop)
            while (True):

                text = text.replace("?", "").replace(".", "？").replace(".", "")
                #
                # pdb.set_trace()
                search_text = urllib.parse.quote_plus(text)

                # search_text = urllib.parse.quote_plus(search_text)
                url = "https://translate.google.com/?sl={}&tl={}&text={}&op=translate".format(tgt_lang, src_lang,
                                                                                              search_text)
                driver.get(url)

                content_translate_text = WebDriverWait(driver, 5).until(
                    lambda driver: driver.find_element_by_class_name('J0lOec'))

                list_ = content_translate_text.text.replace("\n", "")
                if (tgt_lang != "zh-CN"):
                    list_transed_text.append({src_lang: list_, tgt_lang: rawtext})
                else:
                    list_transed_text.append({src_lang: list_, "zh": rawtext})
                break
            print(list_)
            time.sleep(1)
            loop = loop + 1
    except Exception as e:
        print(e)
        time.sleep(3)
        pass
        # f.close()

    return list_transed_text

import requests

config = configparser.RawConfigParser()
config.read('Api.properties')

def sentencesAlignment(src_source, tgt_source, tgt_lang):
    global  config
    payload = Utility.objectToJson({"type": config.get(tgt_lang, 'api.type'),
                                    "source": src_source,
                                    "target": tgt_source})
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST",  config.get(tgt_lang,'api.url'), headers=headers, data=payload.encode("utf-8"))
    print(response.text)
    data = Utility.stringJsonToOject(response.text)
    for x in data['data']:
        print(x)


def sentencesSegmentation(src_source, tgt_lang):
    global  config

    payload = Utility.objectToJson({"type":tgt_lang,
                                    "source": src_source})
    headers = { 'Content-type': 'application/json; charset=utf-8'}

    response = requests.request("POST",  config.get('segmentation','api.url'), headers=headers, data=payload.encode("utf-8"))
    try:
        data = Utility.stringJsonToOject(response.text)
    except:
        return src_source
    return data['data']

#sentencesAlignment("kiểm tra", "ກວດສອບ", "lo")