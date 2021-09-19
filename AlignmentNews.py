import os
import pdb
import re
import time
import traceback
import urllib
from datetime import datetime

from multipledispatch import dispatch
from selenium.webdriver.support.ui import WebDriverWait
import SentenceAlign
import ChromeDriver

import Utility


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


def vizhApi(src_source, tgt_source):
    url = "http://nmtuet.ddns.net:9977/sentences_align"

    payload = Utility.objectToJson({"type": "vi-lo",
                                    "source": src_source,
                                    "target": tgt_source})

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def viloApi(src_source, tgt_source):
    url = "http://nmtuet.ddns.net:9988/scores/sentences"

    payload = Utility.objectToJson({"type": "vi-lo",
                                    "source": src_source,
                                    "target": tgt_source})

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
