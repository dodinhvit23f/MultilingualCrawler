import datetime
import os
import Utility
import AlignmentNews
def saveSentences (src_text, tgt_text, file_path, src_lang_, tgt_lang_):
    time = datetime.datetime.now()

    if src_text and tgt_text:

        if not src_text or not tgt_text:
            print("empty file: " + file_path)
        else:
            f = open(file_path+"-" + src_lang_ + "-" + tgt_lang_ + ".txt", "w", encoding='utf-8')

            # code này để tạm thời
            lim_src = len(src_text)
            lim_tgt = len(tgt_text)
            lim = lim_tgt if lim_tgt >= lim_src else lim_src
            text_src = ""
            text_tgt = ""
            for index in range(0, lim):

                if (index < lim_src):
                    text_src = src_text[index]

                if (index < lim_tgt):
                    text_tgt = tgt_text[index]
                # if tgt_text[index] != "" and
                f.write(text_src + "\t" + text_tgt + "\n")

                text_src = ""
                text_tgt = ""
            f.close()

def saveDocument (src_text, tgt_text, file_path, src_lang_, tgt_lang_):

    if src_text and tgt_text:
        f = open(file_path + ".{}.txt".format(src_lang_), "w", encoding='utf-8')
        f.write(src_text + "\n")
        f.close()

        f = open(file_path + ".{}.txt".format(tgt_lang_), "w", encoding='utf-8')
        f.write(tgt_text + "\n")
        f.close()
    return

def save_data(src_text, file_path):
    if not src_text:
        print("empty file: ")
    else:
        if os.path.isfile(file_path + ".txt"):
            return

        f = open(file_path + ".txt", "w", encoding='utf-8')

        # code này để tạm thời
        lim_src = len(src_text)

        f.write(src_text + "\n")

        f.close()

    return

def saveJsonFile(file_path, link_dict):
    f = open(file_path, "w", encoding="utf-8")
    f.write(Utility.objectToJson(link_dict))
    f.close()

def saveTranslatedTitle(crawl_folder,src_lang, tgt_lang, list_tgt_title, translated = False):
    list_translate = AlignmentNews.translate(src_lang, tgt_lang, list_tgt_title)

    if not translated:
        f = open(crawl_folder + "/link/title.txt", "w", encoding="utf-8")
        for x, y in zip(list_translate, list_tgt_title):
            f.write(Utility.objectToJson({"vi": x, tgt_lang: y}))
            f.write("\n")
        f.close()
        return

    f = open(crawl_folder + "/link/title.txt", "a", encoding="utf-8")
    for x, y in zip(list_translate, list_tgt_title):
        f.write(Utility.objectToJson({"vi": x, tgt_lang: y}))
        f.write("\n")
    f.close()

def openTranslatedTitle(crawl_folder, tgt_link):
    list_trans = list()
    f = open(crawl_folder + "/link/title.txt", "r", encoding="utf-8")
    for line in f:
        list_trans.append(Utility.stringJsonToOject(line.strip()))
    f.close()

    for link in tgt_link:
        start = 0
        for title in list_trans:
            if (title['lo'] == link['title']):
                link['title'] = title['vi']
                break
            start = start + 1
        del (list_trans[start])

def loadJsonFile(file_path):
    f = open(file_path, "r", encoding="utf-8")
    for line in f:
        src_link = Utility.stringJsonToOject(line)
    f.close()

    return src_link