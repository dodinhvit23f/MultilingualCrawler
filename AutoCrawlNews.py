import argparse
import pdb
import sys
import ConvertHtmlToText
from CrawlWebSite import BaseWebsite

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-web', type=str, help='vov, vnanet, vietnamplus, qdnd, vietlao',default=1)
    parser.add_argument('-tgt_lang', type=str, help='Source Language.',default="lo")
    parser.add_argument('-lim_sorce', type=str, help='Source Language.', default="lo")
    return parser.parse_args(argv)

# python AutoCrawlNews.py -web vietlao -tgt_lang lo
# python AutoCrawlNews.py -web vov -tgt_lang lo
if __name__ == '__main__':

    parser = parse_arguments(sys.argv[1:])

    if parser.web == "vov":
        web = BaseWebsite("Vov", "VovCrawler", ["en", "ja", "km", "zh", "lo", "vi"])
        web.auto_crawl_website(parser.tgt_lang)
    if parser.web == "vietlao":
        web = BaseWebsite("VietLao", "VietLaoVietNamCrawler", ["lo", "vi"])
        web.auto_crawl_website(parser.tgt_lang)
    if parser.web == "vnanet":
        web = BaseWebsite("Vnanet", "VnanetCrawler", ["vi", "lo", "zh", "en"])
        web.auto_crawl_website(parser.tgt_lang)
    if parser.web == "vietnamplus":
        web = BaseWebsite("VietNamPlus", "VietNamPlusCrawler", ["vi", "zh", "en"])
        web.auto_crawl_website(parser.tgt_lang, type="date")
    if parser.web == "qdnd":
        web = BaseWebsite("QDND", "QDNDCrawler", ["lo", "vi", "zh", "en","km"])
        web.auto_crawl_website(parser.tgt_lang, type="title")
    if parser.web == "tapchicongsan":
        web = BaseWebsite("TapchiCongSan", "TapChiCongSanCrawler", ["lo", "vi", "zh", "en"])
        web.auto_crawl_website(parser.tgt_lang, type="title")
    if parser.web == "nhandan":
        web = BaseWebsite("NhanDan", "NhanDanCrawler", ["vi", "zh",'en'])
        web.auto_crawl_website(parser.tgt_lang, type="title")

