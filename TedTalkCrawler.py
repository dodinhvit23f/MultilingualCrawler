import os
from datetime import datetime
import ConvertHtmlToText
import Punctuation


def crawlWithLanguage(language):
    """
    :param language: "en", "ja", "km", "zh", "lo"
    :return: None
    """
    if (language != "en" and language != "ja" and language != "km" and language != "zh" and language != "lo"):
        raise Exception("Resource not supported")
    # mount to current real part
    current_dir = os.path.dirname(os.path.realpath(__file__))
    map_Punctuation = Punctuation.getPunctuationForLanguage(language)

    _case = {"TH1": 0, "TH2": 1}

    Sentence_folder = current_dir + "/Data/crawler_success/TedTalk/Sentence/"
    Document_folder = current_dir + "/Data/crawler_success/TedTalk/Document/"

    src_lang_ = language
    tgt_lang_ =  "vi"

    output_dir_success = [Sentence_folder, Document_folder]

    if not os.path.exists(Sentence_folder):
        os.makedirs(Sentence_folder)
    if not os.path.exists(Document_folder):
        os.makedirs(Document_folder)

    all_talk_names = {}
    i = 1
    while( i > 0):
        path = "https://www.ted.com/talks?sort=newest&language=" + tgt_lang_ + "&page=%d&sort=newest" % (i)

        all_talk_names = {}
        if ConvertHtmlToText.enlist_talk_names(path, all_talk_names, src_lang_, tgt_lang_):
            #
            # FOR TEST A SPECIFIC LINKS
            # all_talk_names = ["/talks/frank_gehry_as_a_young_rebel"]

            for i in all_talk_names:
                now = datetime.now()
                batch_name = now.strftime("/%Y-%m_%M/")

                ConvertHtmlToText.extract_talk('https://www.ted.com' + i + '/transcript', i[7:], output_dir_success,"", src_lang_, tgt_lang_)
            i = i + 1
            continue
        i = -1
        print("no more talk")
        break
#crawlWithLanguage("en")