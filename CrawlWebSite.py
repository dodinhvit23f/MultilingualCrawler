import os
import pdb

import ChromeDriver
import ConvertHtmlToText
import PageContent
import Punctuation
import SaveFile
import SentenceAlign
import time
import datetime
import AlignmentNews
import SeparateDocumentToSentences
import Utility
from selenium.common.exceptions import WebDriverException

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

    def checkForLatestNews(self, driver , link=None, link_crawled=list(), first=True):
        return self.getWebsiteLink(driver = driver,link=link, list_=link_crawled, first=first)

    def getNewsContent(self, driver, link, language):

        driver.get(link)
        html = driver.page_source

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
        if self.name == "TapchiCongSan":
            return PageContent.getTapChiCongSanConntent(html, language)

    def bilingualNews(self, type, src_link, tgt_link, tgt):
        print("sort data")
        self.sortBy(src_link, type)
        self.sortBy(tgt_link, type)

        print("find bilingual")
        if (type == "date"):
            return SentenceAlign.AlignByTitleAndDateNews(src_link, tgt_link, tgt=tgt, score_lim=0.1, score=0.8)
        if (type == "title"):
            return SentenceAlign.AlignByTitleNews(src_link, tgt_link, tgt=tgt, score_lim=0.1, score=0.8)

    def saveDocument(self, driver, src_link, tgt_link, tgt_lang, document_folder):
        file_name = src_link.split("/")
        file_name = file_name[len(file_name) - 1]
        file_name = file_name[int(len(file_name) / 2):]

        if os.path.isfile(os.path.join(document_folder, file_name + ".{}.txt".format("vi"))):
            return

        src_document = self.getNewsContent(driver, src_link, language="vi")
        tgt_document = self.getNewsContent(driver, tgt_link, language=tgt_lang)

        vi_punctuation = list(Punctuation.getPunctuationForLanguage("en").keys())

        src_document = Utility.formatSentence(src_document)
        tgt_document = Utility.formatSentence(tgt_document)

        src_document = SeparateDocumentToSentences.slpit_text(src_document, vi_punctuation)
        tgt_document = AlignmentNews.sentencesSegmentation(tgt_document, tgt_lang)

        print(file_name)
        SaveFile.saveDocument(src_text=src_document, tgt_text=tgt_document,
                              file_path=os.path.join(document_folder, file_name), src_lang_="vi",
                              tgt_lang_=tgt_lang)

    def sortBy(self, lict_dict, type="date"):
        """
        Sort list of dictionary by title or time
        :param lict_dict:
        :param type:
        :return: None
        """
        if (type == "date"):
            lict_dict.sort(key=lambda x: datetime.datetime.strptime(x.get('date'), "%d/%m/%Y"), reverse=True)
        if (type == "title"):
            lict_dict.sort(key=lambda x: len(x.get('title').strip()), reverse=True)
            lict_dict.reverse()

    def auto_crawl_website(self, target_lang, type="date"):
        resource_lang = "vi"
        self.crawlWithLanguage(resource_lang)
        self.crawlWithLanguage(target_lang)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        map_punctuation = Punctuation.getPunctuationForLanguage(target_lang)
        _case = {"TH1": 0, "TH2": 1}

        sentence_folder = current_dir + "/Data/crawler_success/{}/{}-{}/Sentence/".format(self.name, resource_lang,
                                                                                          target_lang)
        document_folder = current_dir + "/Data/crawler_success/{}/{}-{}/Document/".format(self.name, resource_lang,
                                                                                          target_lang)
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
        print("Vi : {}".format(len(src_link)))
        print("{} : {}".format(target_lang,len(tgt_link)))
        pdb.set_trace()
        driver = ChromeDriver.getChromeDriver()

        for folder in list_resource_folder:
            print(folder)
            # Kiểm tra xem các file, có file link hay chưa
            array_link = list()
            link_file = open(crawl_folder + "/linkauto/{}/{}.txt".format(folder_lang, folder), "r",
                             encoding="utf-8")
            for line in link_file:
                array_link.append(line.replace('\n', '').split("\t"))
            link_file.close()

            first_tgt = False
            first_source = False

            if not os.path.isfile(
                    crawl_folder + "/link/{}/link.txt".format(resource_lang)) or not os.path.isfile(
                crawl_folder + "/link/{}/link.txt".format(target_lang)):
                # Tao thu muc

                if not os.path.exists((crawl_folder + "/link/{}/".format(resource_lang))):
                    os.makedirs(crawl_folder + "/link/{}/".format(resource_lang))
                    first_source = True
                if not os.path.exists((crawl_folder + "/link/{}/".format(target_lang))):
                    os.makedirs(crawl_folder + "/link/{}/".format(target_lang))
                    first_tgt = True

            """
            for line in array_link:
                if line[0] != "" and line[0] != " ":
                    src_link = self.checkForLatestNews(driver=driver,link=line[0], link_crawled=src_link, first=first_source)
            """
            for line in array_link:
                if line[1] != "" and line[1] != " ":
                    tgt_link = self.checkForLatestNews(driver=driver,link=line[1], link_crawled=tgt_link, first=first_tgt)

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
                list_translate = AlignmentNews.translate(driver, "vi", 'zh-CN', list_tgt_title)
            else:
                list_translate = AlignmentNews.translate(driver, "vi", target_lang, list_tgt_title)

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
                list_tgt_title += AlignmentNews.translate(driver, "vi", 'zh-CN', list_trans)
            else:
                list_tgt_title += AlignmentNews.translate(driver, "vi", target_lang, list_trans)

            SaveFile.saveJsonFile(crawl_folder + "/link/{}/title.txt".format(target_lang), link_dict=list_tgt_title)

        list_tgt_title = SaveFile.loadJsonFile(crawl_folder + "/link/{}/title.txt".format(target_lang))

        for link in tgt_link:
            start = 0
            lim = len(list_tgt_title)
            while (start < lim):
                if link["title"] == list_tgt_title[start][target_lang]:
                    link["title"] = list_tgt_title[start][resource_lang]
                    del (list_tgt_title[start])
                    break

        pair_link = self.bilingualNews(type, src_link=src_link, tgt_link=tgt_link, tgt=target_lang)
        pdb.set_trace()
        if not os.path.exists(crawl_folder + "/link/{}-{}".format(resource_lang, target_lang)):
            os.makedirs(crawl_folder + "/link/{}-{}".format(resource_lang, target_lang))

        SaveFile.saveJsonFile(crawl_folder + "/link/{}-{}/link.txt".format(resource_lang, target_lang), pair_link)

        pair_link = SaveFile.loadJsonFile(crawl_folder + "/link/{}-{}/link.txt".format(resource_lang, target_lang))



        for link in pair_link:
            self.saveDocument(driver, link[resource_lang], link[target_lang], target_lang, document_folder)

        driver.delete_all_cookies()
        driver.close()

    def getWebsiteLink(self, driver, link, list_=list(), first=True ,language = 'vi'):
        """
        :param link:    link to craw
        :param list_: list link crawled
        :param first: first time crawl
        :return:
        """
        run = True
        index = 1
        step = 1

        if self.name == "NhanDan" and language == 'lo':
            step = 15
            index = 15

        return_list = list()

        if self.name == "TapchiCongSan":
            return ConvertHtmlToText.getTapChiCongSanLink(driver=driver, link=link, list_=list_, first=first)

        while(run):

            time.sleep(2)
            #pdb.set_trace()

            driver.get(link.format(index))

            html = driver.page_source
            if self.name == "Vov":
                list_link = ConvertHtmlToText.getVovLink(html)
            if self.name == "QDND":
                list_link = ConvertHtmlToText.getQDNDLink(driver, html)
            if self.name == "VietLao":
                list_link = ConvertHtmlToText.getVietNamVietLaoLink(html)
            if self.name == "Vnanet":
                html = ConvertHtmlToText.getVnanetParagragh(driver)
                list_link = ConvertHtmlToText.getVnanetLink(html)
            if self.name == "NhanDan":
                list_link = ConvertHtmlToText.getNhanDanLink(html=html, language=language)

            if list_link == None:
                time.sleep(3)
                continue
            if not list_link:
                run = False

            hadIt = False
            for dict in list_link:

                for crawled in list_:
                    if dict['url'] == crawled['url']:
                        hadIt = True
                        break
                #pdb.set_trace()
                if not hadIt:
                    return_list.append(dict)
                    continue

                if not first and hadIt:
                    run = False
                    break
                if first and hadIt:
                    continue

            index = index + step

        return list_ + return_list