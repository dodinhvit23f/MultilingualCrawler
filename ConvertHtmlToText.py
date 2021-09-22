import os
import pdb
import time
import traceback
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
import ChromeDriver
import Utility
import urllib.request
import SaveFile
import datetime as dt
import re
from selenium.webdriver.support.ui import WebDriverWait


def getTextFromTagsWithClass(src_link, tag, class_):
    soup = BeautifulSoup(urllib.request.urlopen(src_link).read(), "lxml")
    text = ""

    for tag_text in soup.findAll(tag, class_=class_):
        tagText = Utility.formatString(tag_text.text)
        tagText = tagText.replace("\n+", " ")
        tagText = tagText.replace("/.", "")
        tagText = tagText.strip()
        # ký tự lạ xuất hiện tại một số bài báo

        if tagText and not tagText == "":
            text += tagText

    return text


def getTextFromTagsWithId(src_link, tag, id):
    soup = BeautifulSoup(urllib.request.urlopen(src_link).read(), "lxml")
    text = ""

    for tag_text in soup.findAll(tag, {"id": id}):
        # pdb.set_trace()
        tagText = Utility.formatString(tag_text.text)
        tagText = tagText.replace("\n+", " ")
        tagText = tagText.replace("/.", "")
        tagText = tagText.strip()
        # ký tự lạ xuất hiện tại một số bài báo

        if tagText and not tagText == "":
            text += tagText

    return text


def getTextFromTags(src_link, tag):
    soup = BeautifulSoup(urllib.request.urlopen(src_link).read(), "lxml")
    text = ""

    for j in soup.findAll(tag):

        text_in_timestamp = Utility.formatString(j.text)
        text_in_timestamp = text_in_timestamp.replace("/.", "")
        text_in_timestamp = text_in_timestamp.strip()
        if text_in_timestamp:
            text += text_in_timestamp

    return text


def getVovParagragh(driver, url, tag_time="time"):
    not_get_web = True
    while (not_get_web):
        try:
            driver.get(url)
            not_get_web = False
        except:
            print("Loi khong get link duoc {}".format(url))
            pdb.set_trace()
            time.sleep(2)
            pass
    time.sleep(0.5)
    try:
        times = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_tag_name(tag_time))
        list_time = list()
        for time_ in times:
            list_time.append(time_.text)
        source = driver.page_source
    except:
         return None
    return  source


def getVovLink(link, list_=list()):
    """
    :param src_link:
    :param dict_:
    :return:
    """
    # src_link chua max_mage va url de lay bai viet

    base_url = "https://vovworld.vn/"

    index = 1
    print("Page: ")
    list_link = list()
    driver = ChromeDriver.getChromeDriver()

    while (index > 0):
        print(index)
        pdb.set_trace()
        html = getVovParagragh(driver, url="{}{}".format(link, index))

        if not html:
            break

        soup = BeautifulSoup(html, "lxml")

        container = soup.findAll("div", "l-grid__main")

        for paragraphs in container:

            list_paragraph = paragraphs.findAll("article", "story")
            index_time = 0

            if not list_paragraph:
                index = - 1
                break

            for paragraph in list_paragraph:

                if (paragraph.h2.a.attrs['href'] != None):
                    hadIt = False
                    # print("Kiểm tra link trùng")
                    # pdb.set_trace()
                    for link_dict in list_:
                        if (link_dict['url'] == str(base_url + urllib.parse.quote_plus(paragraph.a['href']))):
                            hadIt = True
                            break

                    if hadIt:
                        # pdb.set_trace()
                        index = - 1
                        break

                    datetime = paragraph.time.text

                    titile = paragraph.h2.text.replace("\n", "").replace("\s+", "").strip()

                    if datetime:
                        if titile:
                            dic = {"url": base_url + urllib.parse.quote_plus(paragraph.a['href']),
                                   "date": datetime,
                                   "title": titile}

                            list_link.append(dic)

                        index_time = index_time + 1
                    continue
                else:
                    print("khong co duong dan: "+paragraph.h2.text.replace("\n", "").replace("\s+", "").strip())
        index = index + 1

    driver.close()

    return list_link


def getVnanetParagragh(driver, url):
    """
    :param driver: selenium driver
    :param url:
    :return:
    """
    try:
        driver.get(url)
        print(url)
        xx = driver.find_element_by_id("idviewsmores")

        while (True):
            if xx:
                button = xx.find_element_by_tag_name("a").click()
                time.sleep(1)

                xx = driver.find_element_by_id("idviewsmores")
                print(xx)

            else:
                break
    except:
        pass

    return driver.page_source


def getVnanetLink(link, list_):
    list_link = list()

    driver = webdriver.Chrome(executable_path=os.path.abspath(os.getcwd() + "/chromedriver.exe"))
    source = getVnanetParagragh(driver, link)
    soup = BeautifulSoup(source, "lxml")

    paragraphs = soup.findAll("div", {"id": "listScroll"})

    hadIt = False

    for paragraph in paragraphs:
        all_link = paragraph.findAll("a", {"class": "fon1"})
        array_time = paragraph.findAll("p", {"class": "fon3"})
        all_title = paragraph.findAll("h3")
        count = 0

        for link in all_link:

            href_array = link.attrs['href'].split("/")
            href_array[4] = urllib.parse.quote_plus(href_array[4])

            crawl_link = "{}//{}/{}/{}/{}".format(href_array[0], href_array[2], href_array[3], href_array[4],
                                                  href_array[5])

            for list_dict in list_:
                if crawl_link == list_dict['url']:
                    hadIt = True
                    break
            if hadIt:
                break

            time = array_time[count].text.split(" ")[0]

            title = all_title[count].text

            title = title.replace("\t", "").replace("\n", "").replace("*", "").replace("|", "").replace("\u200b",
                                                                                                        " ").replace(
                "/", "").replace("?", "").replace("*", "")

            dic = {"url": urllib.parse.quote_plus(crawl_link),
                   "date": time,
                   "title": title}

            list_link.append(dic)

            count = count + 1
        if hadIt:
            break
    driver.close()

    return list_link


def getQDNDParagragh(driver, url):
    driver.get(url)
    time.sleep(0.5)
    return driver.page_source


def getQDNDLink(link, list_):
    list_link = list()
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.getcwd() + "/chromedriver.exe"))
    index = 1

    Running = True

    while (Running):
        try:
            source = getQDNDParagragh(driver, link.format(index))
            WebDriverWait(driver, 200).until(lambda driver: driver.find_elements_by_tag_name('img'))
            soup = BeautifulSoup(source, "lxml")

            content = soup.find("div", {"class": "list-news-category"})
            if not content:
                content = soup.find("div", {"class": "ctrangc3"})

            paragraphs = content.findAll("article", {"class": ""})
            if not paragraphs:
                paragraphs = soup.findAll("div", {"class": "pcontent"})
            if not paragraphs:
                paragraphs = soup.findAll("div", {"class": "pcontent3"})
            if not paragraphs:
                break

            for paragraph in paragraphs:
                try:
                    href = paragraph.find("a").attrs['href']
                    title = paragraph.find("h3").text
                    title = title.replace("\"", " ")
                    title = title.replace("\'", " ")
                    title = title.strip()
                    dic = {"url": href,
                           "title": title}
                    for link_dict in list_:
                        if link_dict['url'] == dic["url"]:
                            Running = False
                            break
                    list_link.append(dic)
                except:
                    pass

            index = index + 1
        except:
            print("ngu 10 s")
            time.sleep(10)
            pass
    driver.close()
    return list_link


def enlist_talk_names(path, dict_, src_lang_, tgt_lang_):
    status = False
    time.sleep(2)
    try:
        r = urllib.request.urlopen(path).read()
        soup = BeautifulSoup(r, "lxml")
        talks = soup.find_all("a")

        for i in talks:
            href = i.attrs['href'].replace("?language=" + tgt_lang_, "")
            if href.find('/talks/') == 0:
                if dict_.get(href) != 1:
                    dict_[href] = 1
                status = True
    except Exception as e:
        print(e)
        print("error page couldn't get link")

    return status


def get_links_and_langs(target_link, target_lang, all_link, src_lang_, tgt_lang_):
    for soup in all_link:
        # kiểm tra đường dẫn có bằng None hay không và tìm
        if (soup.get('href') != None and soup.attrs['href'].find('?language=') != -1):
            # kiểm tra xem ngôn ngữ có trùng với ngôn ngữ ở nguồn và đích hay không
            position = soup.attrs['href'].find('?language=') + 10
            lang = soup.get('href')[position:]
            #
            if (src_lang_ == lang or tgt_lang_ == lang
                    and len(target_lang) < 2):
                target_link.append(soup)
                target_lang.append(lang)


"""
src_params a list of vi transcript segments
tgt_params a list of ja transcript segments  
"""


def get_transcript(src_params, tgt_params, target_link, tgt_lang_):
    for j in target_link:
        if j.get('href') != None and j.attrs['href'].find('?language=') != -1:
            if (j.attrs['hreflang'] == None):
                return
            lang = j.attrs['hreflang']
            path = j.attrs['href']
            time.sleep(1.0)
            r1 = urllib.request.urlopen(path).read()
            soup1 = BeautifulSoup(r1, "lxml")
            text_params = []
            # each <p>

            for tag in soup1.find("div", class_="Grid"):

                try:
                    p_tag = tag.p
                    text_in_timestamp = convert_2_speech_per_line(p_tag.text).strip()
                    if text_in_timestamp:
                        text_params.append(text_in_timestamp)
                except:
                    continue
                    pass

            if lang == tgt_lang_:
                tgt_params += text_params
            else:
                src_params += text_params


def convert_2_speech_per_line(ori_text):
    # tmp_text = ori_text.replace('\t', '\n')
    tmp_text = ori_text.replace('\n', ' ').replace('\t', '\n')
    while tmp_text.find("  ") != -1:
        tmp_text = tmp_text.replace('  ', ' ')
    while tmp_text.find("\n\n") != -1:
        tmp_text = tmp_text.replace('\n\n', '\n')
    tmp_text = tmp_text.strip()
    return tmp_text


def merge_all_params(list_param, spliting_param_by_empty_line=False):
    final_text = ""
    spliting_param_char = '\n\n' if spliting_param_by_empty_line else '\n'
    for param in list_param:
        final_text += param.strip() + spliting_param_char
    return final_text.strip()


""" 
There are many cases.
Currenty, they are:
+ TH1: format using script in <p> tag (== timestamp) => Success or Fail in each timestamp
+ TH2: format using script of the whole subtitles .vi and .ja. => Success or Fail in the whole transcript of subtitle

src_params a list of vi transcript segments
tgt_params a list of ja transcript segments  
"""


def format_subtitle_and_saving(src_params, tgt_params,
                               output_dir_fail, output_dir_success, talk_name, src_lang_, tgt_lang_):
    if (tgt_lang_.find("zh") != -1):

        list_text = list()
        for param in src_params:
            param = param.replace(".", "")
            list_text.append(param)
        src_params = list_text

        list_text = list()
        for param in tgt_params:
            param = param.replace("。", "")
            list_text.append(param)
        tgt_params = list_text

    if (src_lang_.find("zh") != -1):
        list_text = list()
        for param in tgt_params:
            param = param.replace(".", "")
            list_text.append(param)

        tgt_params = list_text

        list_text = list()
        for param in src_params:
            param = param.replace("。", "")
            list_text.append(param)

    if not os.path.exists(output_dir_success[0] + "{}-{}".format(tgt_lang_, src_lang_)):
        os.makedirs(output_dir_success[0] + "{}-{}".format(tgt_lang_, src_lang_))

    if not os.path.exists(output_dir_success[1] + "{}-{}".format(tgt_lang_, src_lang_)):
        os.makedirs(output_dir_success[1] + "{}-{}".format(tgt_lang_, src_lang_))

    SaveFile.saveSentences(src_text=tgt_params,
                           tgt_text=src_params,
                           file_path=output_dir_success[0] + "{}-{}/{}".format(tgt_lang_, src_lang_, talk_name),
                           src_lang_=tgt_lang_,
                           tgt_lang_=src_lang_)

    SaveFile.saveDocument(src_text=tgt_params,
                          tgt_text=src_params,
                          file_path=output_dir_success[1] + "{}-{}/{}".format(tgt_lang_, src_lang_, talk_name),
                          src_lang_=tgt_lang_,
                          tgt_lang_=src_lang_)

    return


"""
format_and_save by using the script in <p> not the whole script of subtitle in .ja and .vi
there are two cases:
+ success: The output data does not need to align by hand
+ fail: The output data needs to be aligned by hand

src_params a list of vi transcript segments
tgt_params a list of ja transcript segments  
"""


def extract_talk(path, talk_name, output_dir_success, output_dir_fail, src_lang_, tgt_lang_):
    # if talk_name in os.path.isfile(output_dir_success[0]+):
    # return

    while (True):
        try:
            time.sleep(2)
            r = urllib.request.urlopen(path).read()
            soup = BeautifulSoup(r, "lxml")

            # GET links and langs
            target_link = []
            target_lang = []
            all_link = soup.findAll('link')

            # Lấy link dẫn tới chuỗi nguồn và đích.
            get_links_and_langs(target_link, target_lang, all_link, src_lang_, tgt_lang_)

            # GET DATA
            tgt_params = []
            src_params = []

            if len(target_link) != 2:
                print("talk {} -  error".format(talk_name))
                return
            print("talk {}".format(talk_name))
            get_transcript(src_params, tgt_params, target_link, tgt_lang_)

            if (format_subtitle_and_saving(src_params, tgt_params
                    , output_dir_fail, output_dir_success, talk_name, src_lang_, tgt_lang_)):
                print(talk_name)
            break
        except Exception as e:
            time.sleep(2)
            traceback.print_exc()
            pass


def getNhanDanAllViParagraph(driver, url):
    # driver = ChromeDriver.getChromeDriver()

    list_src = list()
    index = 1
    count_fail = 1
    while (True):
        try:

            driver.get(url.format(index))

            WebDriverWait(driver, 200).until(lambda driver: driver.find_elements_by_tag_name('article'))

            soup = BeautifulSoup(driver.page_source, "lxml")
            articles = soup.findAll("article")

            while (articles == None):
                time.sleep(6)
                count_fail = count_fail + 1
                driver.get(url.format(index))

                if (count_fail == 7):
                    break

            if not articles:
                break

            for article in articles:

                div = article.find("div", {"class": "box-title"})
                title = div.a.attrs['title'].replace("\n", "").replace("\t", "")

                if (div == None):
                    continue

                href = div.a.attrs['href']
                href = href.replace("%2F", "/")

                date_box = article.find("div", {"class": "box-meta-small"})

                if (date_box == None):
                    continue
                if not date_box:
                    continue
                date_time = date_box.text
                date_time = dt.datetime.strptime(date_time.split(" ")[1], '%d/%m/%Y').strftime("%Y/%m/%d")

                if not href in list_src:
                    print(href)

                    dic = {"url": href,
                           "title": title,
                           "date": date_time}
                    list_src.append(dic)


        except:
            traceback.print_exc()

            break
            pass
        index = index + 1

    driver.delete_all_cookies()
    driver.close()
    return list_src


def getNhanDanAllZhpragraph(driver, url):
    list_ = list()
    index = 1
    count_fail = 1

    while (True):
        try:

            driver.get(url.format(index))

            soup = BeautifulSoup(driver.page_source, "lxml")

            WebDriverWait(driver, 200).until(lambda driver: driver.find_elements_by_tag_name('div'))
            divs = soup.findAll("div", {"class": "media-body"})

            if (divs == None):
                break

            if not divs:
                break
            # pdb.set_trace()

            for div in divs:

                if (div.h3 == None):
                    continue

                title = div.h3.text.replace("\n", "").replace("\t", "")

                href = div.h3.a.attrs['href']

                date_box = div.find("small", {"class": "text-muted"})

                if (date_box == None):
                    continue

                if not divs:
                    break

                date_time = date_box.text.replace("nbsp;", "").split(" ")[0]
                date_time = date_time.replace("\xa0", "")
                date_time = date_time.replace("年", "/").replace("月", "/").replace("日", "")

                dic = {"url": href,
                       "title": title,
                       "date": date_time}

                if not dic in list_:
                    # pdb.set_trace()

                    list_.append(dic)


        except:
            traceback.print_exc()
            pass
        index = index + 15
    driver.close()

    return list_


def getVietNamVietLaoLink(link, list_):
    index = 1
    list_link = list()
    dict_ = dict()
    hadIt = False
    driver = ChromeDriver.getChromeDriver()
    while (True):

        if hadIt:
            break
        driver.get(link.format(index))
        divs = driver.find_elements_by_xpath("//div[@class='post-meta']")

        if not divs:
            break

        time.sleep(1)

        for div in divs:

            if hadIt:
                break
            link_string = div.find_element_by_xpath(".//a").get_attribute('href')
            titile_string = div.find_element_by_xpath(".//a").get_attribute('title')
            titile_string = titile_string.replace("\"", "")

            for link_dict in list_:
                if link_dict['url'] == link_string:
                    hadIt = True
                    break

            new = re.sub("\"", "\'", titile_string)

            time_string = div.find_element_by_xpath(".//li").text

            time_ = re.sub("\"", "\'", time_string)

            #print("{}  - {}".format(titile_string, new))

            dict_ = {"url": link_string, "date": time_, "title": new}
            list_link.append(dict_)
        index = index + 1
    driver.delete_all_cookies()
    driver.close()

    return list_link


def getVietNamPlusLink_Date_Titile(link, list_):
    base_link = "https://www.vietnamplus.vn/"
    lang = "vi"
    if ("zh" in link):
        lang = "zh"
        base_link = "https://zh.vietnamplus.vn/"

    if (base_link == None):
        return

    list_link = list()
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.getcwd() + "/chromedriver.exe"))
    hadLink = False
    index = 1
    #pdb.set_trace()
    while(index > 0):

        driver.get(link.format(index))

        soup = BeautifulSoup(driver.page_source, "lxml")

        div_clear_fix = soup.findAll("div", {"class": "clearfix"})

        if (div_clear_fix != None):
            articles = div_clear_fix[0].findAll("article", class_="story")

            if (articles != None):
                for article in articles:
                    if (article.time != None):
                        time = article.time.text.strip()

                        # time = "2021年2月12日14:12"
                        if (lang != "vi"):
                            time = time.replace('年', '-').replace('月', '-').replace('日', ' ')
                            time = dt.datetime.strptime(time, '%Y-%m-%d %H:%M')
                            time = time.strftime("%d-%m-%Y")
                        else:
                            # pdb.set_trace()
                            time = dt.datetime.strptime(time, '%d/%m/%Y - %H:%M')
                            time = time.strftime("%d-%m-%Y")

                    else:
                        time = dt.datetime.strptime(str(dt.datetime.now()).strip(" ")[0: 10], "%Y-%m-%d")
                        time = time.strftime("%d-%m-%Y")

                    href = base_link + urllib.parse.quote_plus(article.h2.a.attrs['href'])


                    for exists_link in list_:

                        if (exists_link["url"] == href):
                            hadLink = True
                            break

                    for exists_link in list_link:
                        if (exists_link["url"] == href):
                            hadLink = True
                            break

                    if hadLink:
                        break

                    title = article.h2.text
                    title = title.replace("\n", "").replace("/", "").replace("*", "").replace("{", "").replace("}", "")
                    title = re.sub("\s+", " ", title).strip()

                    dic = {"url": href,
                           "title": title,
                           "date": time}

                    list_link.append(dic)
            index += 1
            continue
        break
    driver.close()

    return list_link
