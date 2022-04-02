import pdb
import re
import math
import datetime
import random
import sys
import  time
from CocCocTokenizer import PyTokenizer
import numpy as np

vector = dict()
list_stopwords = list()

def compareTitle(src_title, tgt_title):

    count = 0
    for word in src_title:
        if (word in tgt_title):
            count = count + 1

    return (count / len(tgt_title))

def loadStopWords():
    f = open("stopwords.txt", "r", encoding="utf-8")
    for line in f:
        line = line.strip()
        list_stopwords.append(line)
    f.close()

def removeStopWord(words):
    global list_stopwords
    list_new_word = list()

    for word in words:
        if word not in list_stopwords:
            if(word.strip() != ""):
                list_new_word.append(word)
    return list_new_word

def loadVectorEmbbeding(vector):
    f = open("dict.txt", "r", encoding="utf-8")
    for line in f:
        line = line.strip()

        line = line.split(" ")
        key = str(line[0])

        if('@@' in key):
            continue
        #print(line[1])

        if(key.lower() in vector):
            continue
        vector[key.lower()] = int(line[1])
    f.close()

def cosineSinmilar(src_vector, tgt_vector):
    #pdb.set_trace()
    y = np.sqrt(np.sum(np.square(src_vector))) * np.sqrt(np.sum(np.square(tgt_vector)))
    if y == 0:
        return 0
    x = np.sum(src_vector * tgt_vector)
    if x == 0:
        return 0
    return  x / y

def wordToVector(word):

    global  vector
    if word in vector:
        return vector[word]
    else:
        return 100

def TF_IDF(src_sentence, tgt_sentence):
    dict_words = {}
    dict_src = {}
    dict_tgt = {}
    TF_IDF_CountWords(dict_words, dict_src, src_sentence)


    TF_IDF_CountWords(dict_words, dict_tgt, tgt_sentence)

    TF_IDF_Document_Point(dict_words, dict_src, dict_tgt)
    TF_IDF_Document_Point(dict_words, dict_tgt, dict_src)



    tf_idf_sorce = cosineSinmilar(TF_IDF_Vector(dict_words, dict_src), TF_IDF_Vector(dict_words, dict_tgt))
    return  tf_idf_sorce

def TF_IDF_CountWords(dict_words, dict_, words):

    for word in words:
        if word not in dict_words:
            dict_words[word] = 1
        else:
            dict_words[word] = dict_words[word] + 1

        if word not in dict_:
            dict_[word] = 1
        else:
            dict_[word] = dict_[word] + 1

def TF_IDF_Document_Point(dict_words, dict_src, dict_tgt ):

    idf = {}
    for word in dict_src :

        number_of_word_in_sentences = dict_src[word]
        number_of_sentences_contains = 1

        tf =  (number_of_word_in_sentences / dict_words[word])

        if word in dict_tgt:
            number_of_sentences_contains = number_of_sentences_contains + 1

        #idf = math.log(2/number_of_sentences_contains)
        idf = math.log(2/number_of_sentences_contains,10)
        dict_src[word] = tf * idf

def TF_IDF_Vector(dict_words, dict_src):
    vector = np.zeros(len(dict_words))

    start = 0
    for word in dict_words:
        if word in dict_src:
            if(dict_src[word] == 0):
                vector[start] = 1
            else:
                vector[start] = dict_src[word]
            start = start + 1
            continue
        vector[start] = -.65
        start = start + 1
    return vector

def sentenceToTokenize(sentences, annotator):
    word_segmented_text = annotator.word_tokenize(sentences, tokenize_option=0)
    return [x.lower() for x in word_segmented_text]

def preprocessSentence(sentences, annotator):

    sentence = sentences.strip()
    sentence = re.sub("[!.,@#$%^&*()?<>“:]+", "", sentence)
    sentence = re.sub("[-]+", " ", sentence)
    sentence = re.sub("\s+", " ", sentence)

    words = sentenceToTokenize(sentence, annotator)
    return removeStopWord(words)

def preprocessString(list_dict_src, annotator, token=True):
    start = 0
    length = len(list_dict_src)

    while (start < length):

        sentence = list_dict_src[start]['title']

        sentence = sentence.strip()
        sentence = re.sub("[!.,@#$%^&*()?<>“:]+", "", sentence)
        sentence = re.sub("[-]+", " ", sentence)
        sentence = re.sub("\s+", " ", sentence)

        if(token):
            words = sentenceToTokenize(sentence, annotator)
       
        list_dict_src[start]['title'] = sentence
        if (token):
            list_dict_src[start]["words"] = removeStopWord(words)
        else:
            list_dict_src[start]["words"] = sentence.split(" ")
        start = start + 1


def cosine(x, y):
    cos_sim = np.dot(x, y)/(np.linalg.norm(x)*np.linalg.norm(y))
    return cos_sim
"""
Align News By Title And Date
"""
def AlignByTitleAndDateNews(list_dict_src, list_dict_tgt, tgt, annotator, date_range=20, score_lim=0.4, score=0.8, token=True):
    """

    :param list_dict_src: danh sách các dictionary chứa link, date, title ngôn ngữ nguồn
    :param list_dict_tgt: danh sách các dictionary chứa link, date, title ngôn ngữ đích được dịch sang ngôn ngữ nguồn
    :param tgt: ngôn ngữ đích
    :param date_range: giới hạn thời gian
    :param score_lim: ngưỡng thấp nhất có thể lấy
    :param score: ngưỡng bắt đầu
    :param token: có token các
    :return:

    """
    for link in list_dict_src:
        src_datetime = datetime.datetime.strptime(link['date'], "%d/%m/%Y")
        link['date'] = src_datetime

    for link in list_dict_tgt:
        tgt_datetime = datetime.datetime.strptime(link['date'], "%d/%m/%Y")
        link['date'] = tgt_datetime

    preprocessString(list_dict_src, annotator, token=token )
    preprocessString(list_dict_tgt, annotator, token=token)
    print("Preprocessing title new")
    lim_src = len(list_dict_src)
    lim_tgt = len(list_dict_tgt)
    print("Start aligning title from ", len(list_dict_src), len(list_dict_tgt))
    list_align_title = list()
    print(len(list_dict_src), len(list_dict_tgt))
    while score >= score_lim:
        print(score)
        start_src = 0

        checkPoint = 0
        time = - date_range
        while (start_src < lim_src):
            max_ = 0
            start_tgt = checkPoint
            true_tgt = 0

            while (start_tgt < lim_tgt):

                delta = list_dict_src[start_src]['date'] - list_dict_tgt[start_tgt]['date']
                # thoi gian vuot qua khoang date_range

                if(abs(delta.days) > date_range):
                    if delta.days > 0:
                        break
                    if delta.days < 0:
                        start_tgt = start_tgt + 1
                        continue

                if delta.days < 0 and time > delta.days:

                    time = delta.days
                    checkPoint = start_tgt

                if(token):
                    true_sore = TF_IDF(list_dict_src[start_src]["words"], list_dict_tgt[start_tgt]['words'])
                else:
                    true_sore = compareTitle(list_dict_src[start_src]["words"], list_dict_tgt[start_tgt]['words'])

                if (max_ < true_sore):
                    max_ = true_sore
                    true_tgt = start_tgt

                if(max_ >= 1.0):
                    break


                start_tgt = start_tgt + 1
            # print(list_dict_src[start_src]['title'], max_)
            if (max_ < score_lim):
                del (list_dict_src[start_src])
                lim_src = len(list_dict_src)
                continue

            if max_ > score:
                f = open("thongke.csv", "a", encoding="utf-8")
                f.write("{} \t {} \t {}\n".format(list_dict_src[start_src]['title'], list_dict_tgt[true_tgt]['title'], max_))
                f.close()
                list_align_title.append({"vi": list_dict_src[start_src]['url'], tgt: list_dict_tgt[true_tgt]['url']})

                del (list_dict_src[start_src])
                del (list_dict_tgt[true_tgt])

                lim_src = len(list_dict_src)
                lim_tgt = len(list_dict_tgt)
                continue

            start_src = start_src + 1

        score = score - 0.1
    return list_align_title

def AlignByTitleNews(list_dict_src, list_dict_tgt , tgt, annotator, score_lim=0.35, score=0.75, token = True):

    src = "vi"

    if(len(list_dict_src) > len(list_dict_tgt)):
        temp_list = list_dict_src.copy()
        list_dict_src = list_dict_tgt
        list_dict_tgt = temp_list
        temp = tgt
        tgt = "vi"
        src = temp


    lim_src = len(list_dict_src)
    lim_tgt = len(list_dict_tgt)
    print(len(list_dict_src), len(list_dict_tgt))
    print("Tien xu ly title")
    preprocessString(list_dict_src, annotator=annotator)
    preprocessString(list_dict_tgt, annotator=annotator)

    list_align_title = list()

    while score >= score_lim:
        print(score)
        start_src = 0

        checkPoint = 0

        while (start_src < lim_src):
            max_ = 0
            start_tgt = checkPoint
            true_tgt = 0
            # print(start_tgt)

            while (start_tgt < lim_tgt):
                # so sánh title
                if(token):
                    true_sore = TF_IDF(list_dict_src[start_src]['words'],
                                                 list_dict_tgt[start_tgt]['words'])
                else:
                    true_sore = compareTitle(list_dict_src[start_src]["words"], list_dict_tgt[start_tgt]['words'])
                if (max_ < true_sore):
                    max_ = true_sore
                    true_tgt = start_tgt

                if (max_ >= 1.0):
                    break

                if (true_sore < score):
                    start_tgt = start_tgt + 1
                    continue

                start_tgt = start_tgt + 1

            # print(list_dict_src[start_src]['title'], max_)
            if (max_ < score_lim):
                del (list_dict_src[start_src])
                lim_src = len(list_dict_src)
                continue

            if max_ > score:
                print(list_dict_src[start_src]['title'] + " / " + list_dict_tgt[true_tgt]['title'], max_)

                list_align_title.append({src: list_dict_src[start_src]['url'], tgt: list_dict_tgt[true_tgt]['url']})

                del (list_dict_src[start_src])
                del (list_dict_tgt[true_tgt])

                lim_src = len(list_dict_src)
                lim_tgt = len(list_dict_tgt)
                continue

            start_src = start_src + 1

        score = score - 0.1
    return list_align_title
# To perform word segmentation, POS tagging and then NER
# annotator = VnCoreNLP("<FULL-PATH-to-VnCoreNLP-jar-file>", annotators="wseg,pos,ner", max_heap_size='-Xmx2g')
# To perform word segmentation and then POS tagging
# annotator = VnCoreNLP("<FULL-PATH-to-VnCoreNLP-jar-file>", annotators="wseg,pos", max_heap_size='-Xmx2g')
# To perform word segmentation only
# annotator = VnCoreNLP("<FULL-PATH-to-VnCoreNLP-jar-file>", annotators="wseg", max_heap_size='-Xmx500m')
loadVectorEmbbeding(vector)
loadStopWords()


if __name__ == '__main__':

    # Input
    """
    text_origin = "Chủ tịch Quốc hội Vương Đình Huệ: Tháo gỡ khó khăn để tỉnh Bến Tre phát triển cùng khu vực Đồng bằng sông Cửu Long"
    text_trans = "Chủ tịch Quốc hội Vương Đình Huệ: Sự phát triển của tỉnh Bến Tre cùng với Đồng bằng sông Cửu Long ở phía Nam Việt Nam"
    
    annotator = PyTokenizer(load_nontone_data=True)

    text_origin = preprocessSentence(text_origin, annotator)
    text_trans = preprocessSentence(text_trans, annotator)

    print(text_origin)
    print(text_trans)

    print(TF_IDF(text_origin, text_trans))
    """

    list_ = [{"title":"Chủ tịch Quốc hội Vương Đình Huệ: Tháo gỡ khó khăn để tỉnh Bến Tre phát triển cùng khu vực Đồng bằng sông Cửu Long"},
     {"title":"Chủ tịch Quốc hội Vương Đình Huệ: Sự phát triển của tỉnh Bến Tre cùng với Đồng bằng sông Cửu Long ở phía Nam Việt Nam"}]

    annotator = PyTokenizer(load_nontone_data=True)
    preprocessString(list_, annotator, token=True)
    print(list_)