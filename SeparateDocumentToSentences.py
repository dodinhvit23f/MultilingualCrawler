import pdb
import re

import Utility

def getPunctuationForLanguage(language):
    """
        :return Punctuation in dictionary follow language
        :key Vietnamese punctuation
        :var Language destination punctuaction
    """
    if(language == "km"):
        return {".": "\u17d4", "?": "\uff1f", "!": "\uff01", ";": ";", "...": "\u2026"}
    if(language == "zh"):
        return {".": "\u3002", "?": "?", "!": "!", ";": "；", "...": "..."}

    return {".": ".", "?": "?", "!": "!", ";": ";", "...": "..."}

def slpit_text_by_sign(text, sign):
    list_text = text.split(sign);
    if (len(list_text) == 1):
        return None

    return list_text


def add_sign_to_text(text, sign):
    text += sign
    return text

def slipt_with_sign(text, sign):

    text = text.strip()

    last_index = 0
    length = len(text)
    list_text = ""
    next_index = 0
    index = 0
    pre_index = 0

    for index in range(length):
        if ((index + 1) < length):
            next_index = index + 1
            pre_index = index - 1
        if text[index] == sign:

            # print( "position {} is digit {} is letters {}".format(index , text[next_index].isdigit(), text[next_index].isalpha()))
            #pdb.set_trace()
            if (text[next_index] != sign):

                if (text[last_index: index] != "" and text[last_index: index] != " "):
                    if( re.search(r'[\u0e80-\u0eff]', text[pre_index]) or
                            (text[pre_index].isalpha() and text[pre_index].islower()) or
                            re.search(r'[\u4e00-\u9fff]', text[pre_index],re.UNICODE) ):

                        add_text = text[last_index: index]
                        add_text = re.sub("^[\s]+", "", add_text)
                        #pdb.set_trace()

                        if not text[next_index].isdigit() and not text[next_index].isalpha():

                            list_text = list_text + add_text + text[index] +"\n"
                            last_index = next_index
                            continue

                        if (re.search(r'[\u4e00-\u9fff]', text[next_index])):

                            list_text = list_text + add_text + text[index]
                            last_index = next_index
        index = next_index

    if (last_index != index):
        list_text = list_text + text[last_index: index + 1]
    return list_text

def add_sign_to_list(list_text, sign, list_sign):
    if (len(list_text) <= 0):
        return list()
    while (list_text[-1] == ''):
        list_text.pop(len(list_text) - 1)

    new_list = list()
    old_text = ""
    last_index = 0
    for text in list_text:

        if (text == ''):
            old_text = add_sign_to_text(old_text, sign)
            if last_index > 0:
                new_list[last_index - 1] = old_text
            continue

        isSign = False
        last_character = text[len(text) - 1]

        for end_sign in list_sign:

            if (last_character == end_sign):
                isSign = True

        if not (isSign):
            old_text = add_sign_to_text(text, sign)
        else:
            old_text = text

        old_text = old_text.strip()

        new_list.append(old_text)

        last_index += 1
    return new_list

def remake_list_text(raw_text, add_list, sign, list_sign):
    new_list = raw_text[:]
    position = add_list[0]
    list_text = add_list[1]

    list_text = add_sign_to_list(list_text, sign, list_sign)

    for text in list_text:
        if (text == ''):
            continue
        new_list.insert(position, text)
        position = position + 1

    new_list.pop(position)

    # print(new_list)

    return new_list

def slpit_text(text, list_sign):
    # print(text)

    last_sign_index = len(list_sign) - 1

    # print("new list")
    skip = 0
    for sign in list_sign:

        if (sign == list_sign[last_sign_index]):
            continue
        index = 0

        text = slipt_with_sign(text, sign)

    text = Utility.formatDocumentWithComma(text, list_sign[0])

    #pdb.set_trace()
    return text

def saveTestFile(list_sentence):
    f = open("result.txt", "w", encoding="utf-8")

    for line in list_sentence:
        f.write(line + "\n")
    f.close()


if __name__ == '__main__':
    map_ = getPunctuationForLanguage("lo")
    text = "ທ່ານນາງ Kamala Harris ຢັ້ງຢືນວ່າ ການພົວພັນຮ່ວມມືຫວຽດນາມ-ອາເມລິກາ ໃນຂົງເຂດເສດຖະກິດ, ຄວາມໝັ້ນຄົງພວມເພີ່ມທະວີ; ee;  "
    print(slpit_text(text, list_sign=list(map_.keys())))
