from bs4 import BeautifulSoup
import Utility
import pdb
from requests_html import HTMLSession

def getTextFromTagsWithClass(html, tag, class_):
    soup = BeautifulSoup(html, "lxml")
    text = ""

    for tag_text in soup.findAll(tag, class_=class_):

        tagText = Utility.formatString(tag_text.text)
        tagText = tagText.replace("\n+", " ")
        tagText = tagText.replace("/.", "")
        tagText = tagText.strip()
        # ký tự lạ xuất hiện tại một số bài báo

        if tagText and not tagText == "":
            text += tagText

    text =  bytes(text, "utf-8").decode('utf-8', 'ignore')
    return text

def getTextFromTagsWithId(html, tag, id_):
    soup = BeautifulSoup(html, "lxml")
    text = ""

    for tag_text in soup.findAll(tag, {"id":id_} ):
        #
        tagText = Utility.formatString(tag_text.text)
        tagText = tagText.replace("\n+", " ")
        tagText = tagText.replace("/.", "")
        tagText = tagText.strip()
        # ký tự lạ xuất hiện tại một số bài báo

        if tagText and not tagText == "":
            text += tagText

    text = bytes(text, "utf-8").decode('utf-8', 'ignore')
    return text

def getTextFromTags(html, tag):
    soup = BeautifulSoup(html, "lxml")
    text = ""

    for j in soup.findAll(tag):

        text_in_timestamp = Utility.formatString(j.text)
        text_in_timestamp = text_in_timestamp.replace("/.", "")
        text_in_timestamp = text_in_timestamp.strip()
        if text_in_timestamp:
            text += text_in_timestamp

    text = bytes(text, "utf-8").decode('utf-8', 'ignore')
    return text

# từ đây là các hàm để lấy dự liệu các trang web theo từ tên miền
def getVovNewsContent(html):
    """
    :param html: VOV HTML content
    :return:
    """
    return getTextFromTagsWithClass(html, "article", "article")

def getVnanetNewsContet(html):
    return getTextFromTagsWithClass(html, "div", "detail")

def getCanThoNewsContent(html):
    return getTextFromTagsWithId(html, tag="div", id_="newscontents")

def getVietLaoVietNamNewsContent(html):
    return getTextFromTagsWithClass(html, tag="div", class_="post")

def getVietNamPlusNewsContent(html):
    return getTextFromTagsWithClass(html, "div", "article-body")

def getTNUNewsContent(html, lang = "vi"):
    content = ""
    if (lang == "zh" or lang == "en"):
        content = getTextFromTagsWithId(html, tag="div", id="wrapper")
        return content

    return getTextFromTagsWithId(html, tag="div", id="container")

def getQuanDoiNhanDan(html, lang = "vi"):
    if lang == "vi":
        return getTextFromTagsWithId(html = html, tag ="div", id_="dnn_VIEWSINDEX_ctl00_viewhinone")
    if lang == "en":
        return getTextFromTagsWithClass(html, tag="div", class_="NewsNexttop")
    if lang == "zh":
        text = getTextFromTagsWithClass(html, tag="div", class_="detail-post hnoneview")
        if (text != " " or text != ""):
            return text

        return getTextFromTagsWithClass(html, tag="div", class_="col-sm-8")

    if lang == "km":
        text = getTextFromTagsWithClass(html, tag="div", class_="detail-post hnoneview")
        if(text != " " or text != ""):
            return text
        return getTextFromTagsWithClass(html, tag="div", class_="bgqdnd")

    if lang == "lo":
        return getTextFromTagsWithId(html=html, tag="div", id_="dnn_NewsView_Main_ctl00_viewhinone")

def getNhanDanNewsContent(html, lang = "vi"):
    if lang != "vi":
        return getTextFromTagsWithClass(html, "div", "col-sm-8")

    return getTextFromTagsWithClass(html, "div", "detail-page")

def getTapChiCongSanConntent(html, lang = "vi"):

    if lang == "vi":
        return getTextFromTagsWithClass(html, "div", "ContentDetail")

    return getTextFromTagsWithClass(html, "div", "journal-content-article")
#print(getQuanDoiNhanDan(requests.get("https://kh.qdnd.vn/preview/pid/27/newid/513765").content, lang= "km"))
