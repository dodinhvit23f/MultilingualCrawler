import os
import pdb

import AlignmentNews
import PageContent
import Punctuation
import SaveFile
import SentenceAlign
import requests
import datetime

import Utility


class BaseWebsite:

    def __init__(self, name, crawl_folder, accept_language):
        """
        :param name: tên của trang wed
        :param crawl_folder: thư mục tải VD:
        :param accept_language: mảng các nguôn ngữ được trong trang web VD: ["en", "ja", "km", "zh", "lo", "vi"]
        """
        self.crawlFolder = crawl_folder
        self.accept_language = accept_language
        self.name = name

    def crawlWithLanguage(self, language):
        """
        :param language: ["en", "ja", "km", "zh", "lo", "vi"]
        :return: None
        """
        if language not in self.accept_language:
            raise Exception("Resource not supported")

    def checkForLatestNews(self, link=None, list_crawled=None):
        return None

    def getNewsContent(self, link, language):

        html = requests.get(link).content
        if self.name == "Vov":
            return PageContent.getVovNewsContent(html)
        if self.name == "QDND":
            return PageContent.getQuanDoiNhanDan(html, language)
        if self.name == "Vnanet":
            return PageContent.getVnanetNewsContet(html)
        if self.name == "VietNamPlus":
            return PageContent.getVietNamPlusNewsContent(html)
        if self.name == "VietLao":
            return PageContent.getVietLaoVietNamNewsContent(html)
        if self.name == "NhanDan":
            return PageContent.getNhanDanNewsContent(html, language)

    def bilingualNews(self, type, src_link, tgt_link, tgt):

        if self.name == "Vov":
            return SentenceAlign.AlignByTitleAndDateNews(src_link, tgt_link, tgt=tgt, score_lim=0.1, score=0.8, token=False)
        if (type == "date"):
            return SentenceAlign.AlignByTitleAndDateNews(src_link, tgt_link, tgt=tgt, score_lim=0.06, score=0.8)
        if (type == "title"):
            return SentenceAlign.AlignByTitleNews(src_link, tgt_link, tgt=tgt, score_lim=0.06, score=0.8)

    def saveDocument(self, src_link, tgt_link, tgt_lang, document_folder):
        file_name = src_link.split("/")
        file_name = file_name[len(file_name) - 1]
        if os.path.isfile(os.path.join(document_folder, file_name+".{}.txt".format("vi"))):
            return

        src_document = self.getNewsContent(src_link, language="vi")
        tgt_document = self.getNewsContent(tgt_link, language=tgt_lang)

        SaveFile.saveDocument(src_text=src_document, tgt_text=tgt_document, file_path=os.path.join(document_folder, file_name), src_lang_="vi",
                              tgt_lang_=tgt_lang)

    def sortBy(self, type, lict_dict):
        if (type == "date"):
            lict_dict.sort(key=lambda x: datetime.datetime.strptime(x.get('date'), "%d/%m/%Y"))
        if (type == "title"):
            lict_dict.sort(key=lambda x: len(x.get('title').strip()))
            lict_dict.reverse()

    def auto_crawl_website(self, target_lang, type="date"):
        resource_lang = "vi"
        self.crawlWithLanguage(resource_lang)
        self.crawlWithLanguage(target_lang)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        map_punctuation = Punctuation.getPunctuationForLanguage(target_lang)
        _case = {"TH1": 0, "TH2": 1}

        sentence_folder = current_dir + "/Data/crawler_success/{}/Sentence/".format(self.name)
        document_folder = current_dir + "/Data/crawler_success/{}/Document/".format(self.name)

        output_dir_success = [sentence_folder, document_folder]

        if not os.path.exists(sentence_folder):
            os.makedirs(sentence_folder)
        if not os.path.exists(document_folder):
            os.makedirs(document_folder)

        folder_lang = "{}-{}".format(resource_lang, target_lang)

        crawl_folder = current_dir + "/{}".format(self.crawlFolder)
        resource_path = crawl_folder + "/linkauto/{}.txt".format(folder_lang)
        resource_file = None

        if os.path.isfile(resource_path):
            resource_file = open(resource_path, 'r', encoding='utf-8')

        if resource_file == None:
            message_string = "{} - resource file not exist".format(resource_path)
            raise Exception(message_string)

        list_resource_folder = list()
        for line in resource_file:
            list_resource_folder.append(line.strip())
        resource_file.close()

        src_link = list()
        tgt_link = list()
        list_tgt_title = list()
        if os.path.isfile(crawl_folder + "/link/{}/link.txt".format(resource_lang)):
            src_link = SaveFile.loadJsonFile(crawl_folder + "/link/{}/link.txt".format(resource_lang))
        if os.path.isfile(crawl_folder + "/link/{}/link.txt".format(target_lang)):
            tgt_link = SaveFile.loadJsonFile(crawl_folder + "/link/{}/link.txt".format(target_lang))

        for folder in list_resource_folder:
            print(folder)
            # Kiểm tra xem các file, có file link hay chưa
            array_link = list()
            link_file = open(crawl_folder + "/linkauto/{}/{}.txt".format(folder_lang, folder), "r",
                             encoding="utf-8")
            for line in link_file:
                array_link.append(line.replace('\n', '').split("\t"))
            link_file.close()

            if not os.path.isfile(
                    crawl_folder + "/link/{}/link.txt".format(resource_lang)) or not os.path.isfile(
                crawl_folder + "/link/{}/link.txt".format(target_lang)):
                # Tao thu muc
                if not os.path.exists((crawl_folder + "/link/{}/".format(resource_lang))):
                    os.makedirs(crawl_folder + "/link/{}/".format(resource_lang))
                if not os.path.exists((crawl_folder + "/link/{}/".format(target_lang))):
                    os.makedirs(crawl_folder + "/link/{}/".format(target_lang))
            """
            for line in array_link:
                if line[0] != "" and line[0] != " ":
                    src_link = self.checkForLatestNews(line[0], src_link)
            for line in array_link:
                if line[1] != "" and line[1] != " ":
                    tgt_link = self.checkForLatestNews(line[1], tgt_link)
            """

        if src_link:
            SaveFile.saveJsonFile(
                file_path=crawl_folder + "/link/{}/link.txt".format(resource_lang),
                link_dict=src_link)
        if tgt_link:
            SaveFile.saveJsonFile(
                file_path=crawl_folder + "/link/{}/link.txt".format(target_lang),
                link_dict=tgt_link)

        if os.path.isfile(crawl_folder + "/link/{}/title.txt".format(target_lang)):
            list_tgt_title = SaveFile.loadJsonFile(crawl_folder + "/link/{}/title.txt".format(target_lang))

        if not os.path.isfile(crawl_folder + "/link/{}/title.txt".format(target_lang)):
            temp = tgt_link.copy()
            for x in temp:
                list_tgt_title.append(x["title"])

            if (target_lang == 'zh'):
                list_translate = AlignmentNews.translate("vi", 'zh-CN', list_tgt_title)
            else:
                list_translate = AlignmentNews.translate("vi", target_lang, list_tgt_title)

            SaveFile.saveJsonFile(crawl_folder + "/link/{}/title.txt".format(target_lang), link_dict=list_translate)

        if len(tgt_link) > len(list_tgt_title):
            # Tạo một bản copy
            temp = tgt_link.copy()
            # Tạo vòng lặp xóa các tiêu đề đã dịch
            for title in list_tgt_title:
                start = 0
                lim = len(tgt_link)
                while start < lim:
                    try:
                        if (temp[start]['title'] == title[target_lang]):
                            del (temp[start])
                            break
                    except:
                        pdb.set_trace()
                    start = start + 1

            list_trans = list()
            # Thêm các tiêu đề vào trong danh sách
            for x in temp:
                list_trans.append(x["title"])

            if (target_lang == 'zh'):
                list_tgt_title += AlignmentNews.translate("vi", 'zh-CN', list_trans)
            else:
                list_tgt_title += AlignmentNews.translate("vi", target_lang, list_trans)

            SaveFile.saveJsonFile(crawl_folder + "/link/{}/title.txt".format(target_lang), link_dict=list_tgt_title)
        #pdb.set_trace()
        for link in tgt_link:
            start = 0
            lim = len(list_tgt_title)
            while (start < lim):
                if link["title"] == list_tgt_title[start][target_lang]:
                    link["title"] = list_tgt_title[start][resource_lang]
                    del(list_tgt_title[start])
                    break

        pair_link = self.bilingualNews(type, src_link=src_link, tgt_link=tgt_link, tgt=target_lang)


        if not os.path.exists(crawl_folder + "/link/{}-{}".format(resource_lang, target_lang)):
            os.makedirs(crawl_folder + "/link/{}-{}".format(resource_lang, target_lang))

        SaveFile.saveJsonFile(crawl_folder + "/link/{}-{}/link.txt".format(resource_lang, target_lang), pair_link)

        for link in pair_link:
            self.saveDocument( link[resource_lang], link[target_lang], target_lang, document_folder)