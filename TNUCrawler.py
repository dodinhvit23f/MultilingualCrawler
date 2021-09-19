import Punctuation
import os
import ConvertHtmlToText
import datetime
import SeparateDocumentToSentences

def extractContentNews(src_link, language):
    content = ""
    if (language == "zh" or language == "en"):
        content = ConvertHtmlToText.getTextFromTagsWithId(src_link= src_link,tag= "div",id= "wrapper")
        return content

    return  ConvertHtmlToText.getTextFromTagsWithId(src_link = src_link, tag= "div", id="container")
def crawlWithLanguage(language):
    """
    :param language: "en", "zh"
    :return: None
    """
    if(language != "en" and language != 'zh'):
        raise Exception("Resource not supported")

    current_dir = os.path.dirname(os.path.realpath(__file__))
    map_Punctuation = Punctuation.getPunctuationForLanguage(language)

    resource_file = "{}/TNUCrawler/{}-{}.txt".format(current_dir,"vi",language)

    Document_folder = current_dir + "/Data/crawler_success/TNU/Document/"
    if not os.path.exists(Document_folder):
        os.makedirs(Document_folder)

    f = open(resource_file, "r",encoding="utf-8")

    if not f:
        raise Exception("Resource file not exist")

    for line in f:
        src_link, tgt_link, mutil_page = (line.split("\t"))
        file_name = datetime.datetime.now().timestamp()

        list_src = SeparateDocumentToSentences.slpit_text( text = extractContentNews(src_link, "vi")
                                                           ,list_sign= list(map_Punctuation.keys()) )

        file = open(Document_folder+"{}.vi.txt".format(file_name), "w", encoding="utf-8")
        for line in list_src:
            file.write("{} \n".format(line))
        file.close()

        list_tgt = SeparateDocumentToSentences.slpit_text( text= extractContentNews(tgt_link, "zh")
                                                          , list_sign=list(map_Punctuation.keys()))
        file = open(Document_folder + "{}.{}.txt".format(file_name, language), "w", encoding="utf-8")
        for line in list_tgt:
            file.write("{} \n".format(line))
        file.close()

    f.close()

crawlWithLanguage("zh")