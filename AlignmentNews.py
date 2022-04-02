import pdb
import time
import urllib
import Utility
import configparser
from deep_translator import  GoogleTranslator

def translate(src_lang, tgt_lang, list_text):
    list_transed_text = list()
    googleTranslator = GoogleTranslator(source=tgt_lang, target=src_lang)
    time_except = 360
    for text in list_text:
        while(True):
            try:
                rawtext = text
                text = text.replace("?", "").replace(".", "？").replace(".", "")
                list_ = googleTranslator.translate(text)
                if (tgt_lang != "zh-CN"):
                    list_transed_text.append({src_lang: list_, tgt_lang: rawtext})
                else:
                    list_transed_text.append({src_lang: list_, "zh": rawtext})
                print(list_)
                break

            except Exception as e:
                print(e)

                if time_except == 0:
                    break

                time_except = time_except - 1
                time.sleep(2)
                pass
        if time_except == 0:
            break

    return list_transed_text

import requests

config = configparser.RawConfigParser()
config.read('Api.properties')

def sentencesAlignment(src_source, tgt_source, tgt_lang):
    global  config
    payload = Utility.objectToJson({"type": config.get(tgt_lang, 'api.type'),
                                    "source": src_source,
                                    "target": tgt_source})
    if tgt_lang == "km":
        payload = Utility.objectToJson({"type": config.get(tgt_lang, 'api.type'),
                                        "doc_source": src_source,
                                        "doc_target": tgt_source})
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
    try:
        response = requests.request("POST",  config.get('segmentation','api.url'), headers=headers, data=payload.encode("utf-8"), timeout=3)
        data = Utility.stringJsonToOject(response.text)
        response.close()
    except:
        return src_source
    time.sleep(0.001)
    return data['data']
