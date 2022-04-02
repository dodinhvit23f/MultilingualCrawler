import os
import pdb
import time

import SaveFile
import ChromeDriver
import PageContent
import SeparateDocumentToSentences
import Utility
import AlignmentNews

def SeparateSentence(file_name, web, language, list_):
    src_link = SaveFile.loadJsonFile(file_name)
    driver = ChromeDriver.getChromeDriver()

    vi_punctuation = list(SeparateDocumentToSentences.getPunctuationForLanguage("en").keys())


    for dict_ in src_link:
        while(True):
            try:
                driver.get(dict_['url'])
                break
            except:
                time.sleep(1)
        html = driver.page_source
        if "Vov" in web:
            document =  PageContent.getVovNewsContent(html)
        if "QDND" in web :
            document = PageContent.getQuanDoiNhanDan(html, language)
        if "Vnanet" in web:
            document = PageContent.getVnanetNewsContet(html)
        if "VietNamPlus" in web:
            document = PageContent.getVietNamPlusNewsContent(html)
        if "VietLao" in web:
            document = PageContent.getVietLaoVietNamNewsContent(html)
        if "NhanDan" in web:
            document = PageContent.getNhanDanNewsContent(html, language)
        if "TapChiCongSan" in web:
            document = PageContent.getTapChiCongSanConntent(html, language)

        document = Utility.formatSentence(document)
        document = SeparateDocumentToSentences.slpit_text(document, vi_punctuation)

        if language != "vi":

            document = AlignmentNews.sentencesSegmentation(document, language)

        document = document.split("\n")


        if language == "vi":
            f = open("vi", "a", encoding="utf-8")

        if language == "zh":
            f = open("zh", "a", encoding="utf-8")

        if language == "km":
            f = open("km", "a", encoding="utf-8")

        if language == "lo":
            f = open("lo", "a", encoding="utf-8")

        for sentence in document:
            if sentence.strip() not in list_:
                list_.append(sentence.strip())
                f.write("{}\n".format(sentence))

        f.close()
        time.sleep(0.1)
    driver.delete_all_cookies()
    driver.close()
    list_ = list()

if __name__ == '__main__':
    #folders = ['NhanDanCrawler', 'QDNDCrawler', 'TapChiCongSanCrawler', 'VietLaoVietNamCrawler','VietNamPlusCrawler', 'VovCrawler']
    folders = ['TapChiCongSanCrawler', 'VietLaoVietNamCrawler', 'VietNamPlusCrawler','VovCrawler']

    base_dir = os.getcwd()

    vi_list = list()
    zh_list = list()
    km_list = list()
    lo_list = list()

    for folder in folders:
        sub_folders = os.listdir(os.path.join(base_dir, folder))
        for sub_folder in sub_folders:
            if( sub_folder == "link"):

                crawl_path = os.path.join(base_dir, folder)
                link_folders = os.listdir(crawl_path)

                for x in link_folders:
                    link_path = os.path.join(crawl_path, x)
                    mololingual_folders = os.listdir(link_path)

                    for mololingual_folder in mololingual_folders:
                        mololingual_path = os.path.join(link_path, mololingual_folder)


                        file_name =  os.path.join(mololingual_path,"link.txt")

                        if mololingual_folder == "zh":
                            SeparateSentence(file_name, folder, mololingual_folder, zh_list)

                        """
                        if mololingual_folder == "lo":
                            SeparateSentence(file_name, folder, mololingual_folder, lo_list)

                        if mololingual_folder == "km":
                            SeparateSentence(file_name, folder, mololingual_folder, km_list)
                         if mololingual_folder == "vi":
                            SeparateSentence(file_name, folder, mololingual_folder, vi_list)
                        
                        """

