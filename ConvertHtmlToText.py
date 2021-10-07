import os
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
import pdb

def getVovLink(html):
    base_url = "https://vovworld.vn/"

    list_link = list()

    if not html:
        return list()

    soup = BeautifulSoup(html, "lxml")

    container = soup.findAll("div", "l-grid__main")
    if not container:
        return None

    for paragraphs in container:

        list_paragraph = paragraphs.findAll("article", "story")

        if not list_paragraph:
            return list()
        #pdb.set_trace()
        for paragraph in list_paragraph:

            if (paragraph.h2.a.attrs['href'] != None):
                datetime = paragraph.p.time.text
                datetime = datetime.strip()

                try:
                    x = dt.datetime.strptime(datetime, "%d/%m/%Y")
                except:
                    datetime = dt.datetime.strptime(str(dt.datetime.now()).strip(" ")[0: 10], "%Y-%m-%d")
                    datetime = time.strftime("%d/%m/%Y")

                titile = paragraph.h2.text.replace("\n", "").replace("\s+", "").strip()

                if datetime and titile:
                    dic = {"url": base_url + urllib.parse.quote_plus(paragraph.a['href']),
                           "date": datetime,
                           "title": titile}

                    list_link.append(dic)
                continue
            print("khong co duong dan: " + paragraph.h2.text.replace("\n", "").replace("\s+", "").strip())
    return list_link

def getVnanetParagragh(driver):
    """
    :param driver: selenium driver
    :param url:
    :return:
    """
    try:
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

def getVnanetLink(html, list_):
    list_link = list()

    soup = BeautifulSoup(html, "lxml")
    paragraphs = soup.findAll("div", {"id": "listScroll"})

    if not paragraphs:
        return None

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
            crawl_link = urllib.parse.quote_plus(crawl_link)
            time = array_time[count].text.split(" ")[0]

            title = all_title[count].text
            title = title.replace("\t", "").replace("\n", "")\
                .replace("*", "").replace("|", "").replace("\u200b"," ")\
                .replace("/", "").replace("?", "").replace("*", "")

            hadIt = False
            for x in list_:
                if x['url'] == crawl_link:
                    hadIt = True

            if hadIt:
                continue

            dic = {"url": crawl_link,
                   "date": time,
                   "title": title}

            list_link.append(dic)

            count = count + 1


    return list_link

def getQDNDLink(driver, html):
    list_link = list()
    WebDriverWait(driver, 200).until(lambda driver: driver.find_elements_by_tag_name('img'))
    soup = BeautifulSoup(html, "lxml")

    content = soup.find("div", {"class": "list-news-category"})

    if not content:
        content = soup.find("div", {"class": "ctrangc3"})
    if not content:
        return None

    paragraphs = content.findAll("article",{"class": ""})
    if not paragraphs:
        paragraphs = soup.findAll("div", {"class": "pcontent"})
    if not paragraphs:
        paragraphs = soup.findAll("div", {"class": "pcontent3"})
    if not paragraphs:
        return list_link

    for paragraph in paragraphs:
        try:
            href = paragraph.find("a").attrs['href']
            title = paragraph.find("h3").text
            title = title.replace("\"", " ")
            title = title.replace("\'", " ")
            title = title.strip()

            dic = {"url": href,
                   "title": title}

            list_link.append(dic)
        except:
            pass

    return list_link

def getNhanDanLink(html, language):
    list_ = list()
    soup = BeautifulSoup(html, "lxml")
    if language == "vi":
        articles = soup.findAll("article")
    if language == "zh":
        articles = soup.findAll("div", {"class": "media-body"})

    if articles == None:
        return None
    if not articles:
        return list_

    base_url = "https://nhandan.com.vn/"
    if language == 'zh':
        base_url = "https://cn.nhandan.com.vn/"

    for div in articles:
        if language == "lo":
            if (div.h3 == None):
                continue

            date_box = div.find("small", {"class": "text-muted"})

            if (date_box == None):
                continue

            title = div.h3.text.replace("\n", "").replace("\t", "")

            href = base_url + urllib.parse.quote_plus(div.h3.a.attrs['href'])
            href = href.replace("%2F", "/")

            date_time = date_box.text.replace("nbsp;", "").split(" ")[0]
            date_time = date_time.replace("\xa0", "")
            date_time = date_time.replace("年", "/").replace("月", "/").replace("日", "")
        if language == "vi":
            div_ = div.find("div", {"class": "box-title"})
            if (div_ == None):
                continue

            date_box = div.find("div", {"class": "box-meta-small"})
            if (date_box == None):
                continue

            title = div_.a.attrs['title'].replace("\n", "").replace("\t", "")
            href = base_url + urllib.parse.quote_plus(div_.a.attrs['href'])
            href = href.replace("%2F", "/")

            date_time = date_box.text
            date_time = dt.datetime.strptime(date_time.split(" ")[1], '%d/%m/%Y').strftime("%Y/%m/%d")

        dict_ = {"url": href, "date": date_time, "title": title}
        list_.append(dict_)
    return list_

def getVietNamVietLaoLink(html):
    list_link = list()
    base_url = "https://vietlao.vietnam.vn"
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("div", {"class": "post-meta"})

    if not divs:
        return list_link

    for div in divs:

        link_string = base_url + div.find("a").attrs['href']
        titile_string = div.find("a").attrs['title']
        titile_string = titile_string.replace("\"", "")

        new = re.sub("\"", "\'", titile_string)

        time_string = div.find("li").text
        time_ = re.sub("\"", "\'", time_string)

        dict_ = {"url": link_string, "date": time_, "title": new}

        list_link.append(dict_)


    return list_link

def getVietNamPlusLink_Date_Titile(html, link):
    base_link = "https://www.vietnamplus.vn/"
    lang = "vi"
    if ("zh" in link):
        lang = "zh"
        base_link = "https://zh.vietnamplus.vn/"

    list_link = list()

    soup = BeautifulSoup(html, "lxml")

    div_clear_fix = soup.findAll("div", {"class": "clearfix"})

    if (div_clear_fix != None):
        articles = div_clear_fix[0].findAll("article", class_="story")
        if (articles != None):
            for article in articles:
                if article.time != None:
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

                title = article.h2.text
                title = title.replace("\n", "").replace("/", "").replace("*", "").replace("{", "").replace("}", "")
                title = re.sub("\s+", " ", title).strip()

                dic = {"url": href,
                       "title": title,
                       "date": time}

                list_link.append(dic)

    return list_link

def getTapChiCongSanLink(driver, link, list_, first=True):
    driver.get(link)
    index = 1
    list_link = list()

    Ended = False
    while (True):

        soup = BeautifulSoup(driver.page_source, "lxml")
        divs = soup.findAll("div", class_="itemNews")

        if divs == None:
            break

        if not divs:
            break

        for div in divs:
            href = div.find("h4", class_="titleNews").a.attrs['href']
            title = div.find("h4", class_="titleNews").text
            title = title.strip()
            title = Utility.formatSentence(title)
            addIt = True
            for x in list_:
                if x['url'] == href:
                    if not first:
                        Ended = True
                    addIt = False
                    break

            if addIt:
                list_link.append({"url": href, "title": title})

        div = driver.find_element_by_xpath("//div[@class='search-results']")
        li_tags = div.find_elements_by_xpath(".//li")

        next_page = 0

        for li in li_tags:
            a_tag = li.find_element_by_xpath(".//a")

            if (a_tag.text == "»"):
                Ended = True
                break

            if not a_tag.text.isnumeric():
                continue

            next_page = int(a_tag.text)

            if (index < next_page):
                index = next_page
                a_tag.click()
                break

        if (Ended):
            break
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

