import ConvertHtmlToText
import Punctuation
import ChromeDriver
import os
import traceback
import SeparateDocumentToSentences
import SaveFile
import pdb

import Utility


def getNhanDanViContent(link, file_name, title, list_sign):
    if (os.path.isfile(file_name + ".txt")):
        return
    list_src = list()
    try:

        content = ConvertHtmlToText.getTextFromTagsWithClass(link,"div", {"class": "entry-content"})

        if (content == None):
            return
        text = bytes(content.text, "utf-8").decode('utf-8', 'ignore')

        list_src.append(title)

        list_src = list_src + SeparateDocumentToSentences.slpit_text(text, list_sign)


    except:
        traceback.print_exc()
        pass
    return list_src

def getNhanDanZhContent(link, file_name, title, list_sign):

    if (os.path.isfile(file_name + ".txt")):
        return

    list_src = list()
    try:

        content = ConvertHtmlToText.getTextFromTags(link,"table")

        if (content == None):
            return
        text = bytes(content.text, "utf-8").decode('utf-8', 'ignore')

        list_src.append(title)

        list_src = list_src + SeparateDocumentToSentences.slpit_text(text, list_sign)

    except:
        traceback.print_exc()
        pass
    return list_src

def checkForLatestNews(crawl_folder, tgt_lang_, folder_lang, listResourceFolder):
    """
    :param resourceFile: resource file
    :param listResourceFolder: list folder in resource file
    :param crawl_folder: path to saved url folder
    :param tgt_lang_: target folder
    :param folder_lang: mutilple language folder
    :return:
    """
    for folder in listResourceFolder:
        print(folder)

        link_file = open(crawl_folder + "/linkauto/{}/{}.txt".format(folder_lang, folder), "r", encoding="utf-8")
        array_link = link_file.readline().replace('\n', '').split("\t")
        link_file.close()

        if not os.path.isfile(
                crawl_folder + "/link/{}/{}/link.txt".format("vi", folder)) or not os.path.isfile(
                crawl_folder + "/link/{}/{}/link.txt".format(tgt_lang_, folder)):
            # Tao thu muc
            if not os.path.exists((crawl_folder + "/link/{}/{}/".format("vi", folder))):
                os.makedirs(crawl_folder + "/link/{}/{}/".format("vi", folder))

            if not os.path.exists((crawl_folder + "/link/{}/{}/".format(tgt_lang_, folder))):
                os.makedirs(crawl_folder + "/link/{}/{}/".format(tgt_lang_, folder))

            # đọc file chứa link có định dạng src_link \t max_page \t tgt_link \t max_page

            # Lay link tat ca cac bai viet.

            if not os.path.isfile(crawl_folder + "/link/{}/{}/link.txt".format("vi", folder)):

                src_link = ConvertHtmlToText.getNhanDanAllViParagraph(ChromeDriver.getChromeDriver(),array_link[0])

                f = open(crawl_folder + "/link/{}/{}/link.txt".format("vi", folder), "w", encoding="utf-8")
                f.write(Utility.objectToJson(src_link))
                f.close()

            if not os.path.isfile(crawl_folder + "/link/{}/{}/link.txt".format(tgt_lang_, folder)):

                tgt_link = ConvertHtmlToText.getNhanDanAllZhpragraph(ChromeDriver.getChromeDriver(),array_link[1])

                f = open(crawl_folder + "/link/{}/{}/link.txt".format(tgt_lang_, folder), "w", encoding="utf-8")
                f.write(Utility.objectToJson(tgt_link))
                f.close()

def crawlWithLanguage(language):
    """
    :param language: "en","zh"
    :return: None
    """
    if (language != "en" and language != "zh"):
        raise Exception("Resource not supported")
    # mount to current real part
    current_dir = os.path.dirname(os.path.realpath(__file__))
    map_Punctuation = Punctuation.getPunctuationForLanguage(language)

    _case = {"TH1": 0, "TH2": 1}

    Sentence_folder = current_dir + "/Data/crawler_success/NhanDan/Sentence/"
    Document_folder = current_dir + "/Data/crawler_success/NhanDan/Document/"

    src_lang_ = "vi"
    tgt_lang_ = language

    output_dir_success = [Sentence_folder, Document_folder]

    if not os.path.exists(Sentence_folder):
        os.makedirs(Sentence_folder)
    if not os.path.exists(Document_folder):
        os.makedirs(Document_folder)

    folder_lang = src_lang_ + "-" + tgt_lang_
    crawl_folder = current_dir + "/NhanDanCrawler"
    resourcePath = crawl_folder + "/linkauto/" + folder_lang + ".txt"

    resourceFile = None

    if os.path.isfile(resourcePath):
        resourceFile = open(resourcePath, 'r', encoding='utf-8')

    if (resourceFile == None):
        messageString = "{} - resource file not exist".format(resourcePath)
        raise Exception(messageString)

    listResourceFolder = list()

    for line in resourceFile:
        listResourceFolder.append(line.strip())
    resourceFile.close()
    # check for the latest news
    checkForLatestNews(crawl_folder, tgt_lang_, folder_lang, listResourceFolder)
    # set all news in to list
    for folder in listResourceFolder:

        f = open(crawl_folder + "/link/{}/{}/link.txt".format(src_lang_, folder), "r", encoding="utf-8")

        src_link = list()

        for line in f:
            line = line.replace("\n", "")
            if (line != ""):
                src_link.append(line.split("\t"))
        f.close()

        f = open(crawl_folder + "/link/{}/{}/link.txt".format(tgt_lang_, folder), "r", encoding="utf-8")

        tgt_link = list()

        for line in f:
            line = line.replace("\n", "")
            if (line != ""):
                tgt_link.append(line.split("\t"))
        f.close()
    # sorting news
if __name__ == '__main__':
    crawlWithLanguage("zh")
    """
    src_sign = list( map_vi2ja_end_sign.keys() )
    tgt_sign = list( map_vi2ja_end_sign.values() )


    
    for data in src_link:
        date_time = datetime.strptime(data[1], "%Y/%m/%d").strftime("%Y/%m/")
        file_name = data[0].split("/")[5]
        #pdb.set_trace()
        save_folder = TH1_folder +"/"+folder+"/" + date_time 
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            
        try:    
            save_folder = save_folder +file_name
            getViContent(data[0], save_folder,data[2],  src_sign)
            print(file_name)
        except:
            traceback.print_exc()
       
    # lay link 
    
    for data in tgt_link:
        
        date_time = datetime.strptime(data[1].replace("\xa0",""), "%Y/%m/%d").strftime("%Y/%m/")
        file_name = data[0].split("-")[1].replace(".html","")
        
        save_folder = TH2_folder +"/"+folder+"/" + date_time 
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            
        save_folder = save_folder +file_name[0:15]
        
        try:
            getZhContent(data[0], save_folder,data[2],  tgt_sign)
            print(file_name)
        except:
            traceback.print_exc() 
            pdb.set_trace()
            pass
    
    os.system("cls")
    """