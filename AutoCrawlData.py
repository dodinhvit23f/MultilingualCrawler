import argparse
import pdb
import sys
import ConvertHtmlToText
from CrawlWebSite import BaseWebsite

class VietLaoWebCrawl(BaseWebsite):

    def __init__(self, name, crawl_folder, accept_language):
        BaseWebsite.__init__(self, name, crawl_folder, accept_language)

    def checkForLatestNews(self, link, list_crawled=list()):

        return list_crawled + ConvertHtmlToText.getVietNamVietLaoLink(link=link,list_=list_crawled)

    pass

class VovWebsite(BaseWebsite):

    def __init__(self, name, crawl_folder, accept_language):
        BaseWebsite.__init__(self, name, crawl_folder, accept_language)

    def checkForLatestNews(self, link, list_crawled=list()):

        return list_crawled + ConvertHtmlToText.getVovLink(link=link,list_=list_crawled)

    pass

class VnanetWeb(BaseWebsite):
    def __init__(self, name, crawl_folder, accept_language):
        BaseWebsite.__init__(self, name, crawl_folder, accept_language)

    def checkForLatestNews(self, link, list_crawled=list()):
        return list_crawled + ConvertHtmlToText.getVnanetLink(link=link,list_=list_crawled)
    pass

class QuanDoiNhanDanWeb(BaseWebsite):
    def __init__(self, name, crawl_folder, accept_language):
        BaseWebsite.__init__(self, name, crawl_folder, accept_language)

    def checkForLatestNews(self, link, list_crawled=list()):
        return list_crawled + ConvertHtmlToText.getQDNDLink(link=link,list_=list_crawled)
    pass

class VietNamPlusCrawlerWeb(BaseWebsite):
    def __init__(self, name, crawl_folder, accept_language):
        BaseWebsite.__init__(self, name, crawl_folder, accept_language)

    def checkForLatestNews(self, link, list_crawled=list()):
        return list_crawled + ConvertHtmlToText.getVietNamPlusLink_Date_Titile(link=link,list_=list_crawled)
    pass

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-web', type=str, help='vov, vnanet, vietnamplus, qdnd, vietlao',default=1)
    parser.add_argument('-tgt_lang', type=str, help='Source Language.',default="lo")
    parser.add_argument('-lim_sorce', type=str, help='Source Language.', default="lo")
    return parser.parse_args(argv)

# python AutoCrawlData.py -web vietnamplus -tgt_lang lo
# python AutoCrawlData.py -web vov -tgt_lang lo
if __name__ == '__main__':

    parser = parse_arguments(sys.argv[1:])

    if parser.web == "vov":
        web = VovWebsite("Vov", "VovCrawler", ["en", "ja", "km", "zh", "lo", "vi"])
        web.auto_crawl_website(parser.tgt_lang)
    if parser.web == "vietlao":
        web = VietLaoWebCrawl("VietLao", "VietLaoVietNamCrawler", ["lo", "vi"])
        web.auto_crawl_website(parser.tgt_lang)
    if parser.web == "vnanet":
        web = VnanetWeb("Vnanet", "VnanetCrawler", ["vi", "lo", "zh", "en"])
        web.auto_crawl_website(parser.tgt_lang)
    if parser.web == "vietnamplus":
        web = VietNamPlusCrawlerWeb("VietNamPlus", "VietNamPlusCrawler", ["vi", "zh", "en"])
        web.auto_crawl_website(parser.tgt_lang, type="date")
    if parser.web == "qdnd":
        web = QuanDoiNhanDanWeb("QDND", "QDNDCrawler", ["lo", "vi", "zh", "en"])
        web.auto_crawl_website(parser.tgt_lang, type="title")

