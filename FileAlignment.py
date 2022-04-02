import pdb

import SentenceAlign
from deep_translator import  GoogleTranslator
import os
from vncorenlp import VnCoreNLP


def findBilingualFile(file_name, list_file, extension):
    file = None
    file = filter(lambda file_tgt: file_tgt == "{}.{}".format(file_name, extension), list_file)
    return list(file)

def translateDocument(document_path, tgt_lang,  annotator):
    googleTranslator = GoogleTranslator(source=tgt_lang, target="vi")
    list_file = os.listdir(document_path)

    for viFile in filter(lambda file: "vi.txt" in file,list_file):
        bilingualFile = findBilingualFile(viFile.split(".")[0], list_file, "{}.txt".format(tgt_lang))

        list_source = list()
        list_target = list()
        f = open(os.path.join(document_path, viFile), "r", encoding="utf-8")
        for line in f:
            if line.strip() != "":
                list_source.append(line.strip())
        f.close()

        f = open(os.path.join(document_path, bilingualFile[0]), "r", encoding="utf-8")
        for line in f:
            if line.strip() != "":
                list_target.append(line.strip())
        f.close()

        translated_list = googleTranslator.translate_batch(list_target)

        for line in AlignFileSentence(list_source, list_target, translated_list, annotator):

            print(line)

def AlignFileSentence(list_origin, list_target, translated_list, annotator):
    """
        gióng hàng văn bản: danh sách câu nguôn, danh sách câu gốc, danh sách câu được dịch
    """
    text = ""
    text_translate = ""

    while (True):
        lim = len(list_origin)
        lim_tgt = len(list_origin)

        start = 0
        list_ = list()

        highest_origin = 0
        highest_translated = 0
        scorce = 0.0

        while start < lim:
            start_tgt = 0
            bag_of_word_origin = SentenceAlign.preprocessSentence(list_origin[start], annotator=annotator)

            while start_tgt < lim_tgt:
                bag_of_word_translated = SentenceAlign.preprocessSentence(translated_list[start_tgt],annotator=annotator)
                scorce_sentence = SentenceAlign.TF_IDF(bag_of_word_origin, bag_of_word_translated)

                if scorce < scorce_sentence:

                    highest_origin = start
                    highest_translated = start_tgt
                    scorce = scorce_sentence

                else:
                    list_.append((list_origin[start], translated_list[start_tgt], scorce))
                start_tgt = start_tgt + 1

            start = start + 1

        if scorce <= 0.2:
            break
        else:

            yield "{}\n{}\n{} \n\n".format(list_origin[highest_origin], list_target[highest_translated],scorce)

            del(list_origin[highest_origin])
            del (translated_list[highest_translated])
            del (list_target[highest_translated])
            lim = len(list_origin)
            lim_tgt = len(translated_list)
    """
    f = open("thong_ke.txt", "w", encoding="utf-8")
    for line in list_:
        f.write("{}\t{}\t{}\n".format(line[0], line[1], line[2]))
    f.close()
    """
"""
    thay đổi path VnCoreNLP
    Ngôn ngữ đầu vào
    
"""

annotator = VnCoreNLP("./VnCoreNLP/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')
translateDocument("D:/NLP/Paracrawl/test", "lo",  annotator)

