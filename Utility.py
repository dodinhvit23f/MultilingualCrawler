import re
import json
import pdb

def deleteEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        u"\U0001F1E0-\U0001F1FF"
                                        "]+", flags=re.UNICODE)

    return regrex_pattern.sub(r'', text)


def formatString(text):
    text = deleteEmojify(text)
    text = formatSentence(text)
    return text

def removeNBSP(text):
    return text.replace("&nbsp", '')

def splipWithEndLine(text):
    list_ = list()
    leng = len(text) - 1
    next_ = 0
    start = 0
    crop_at = 0

    while start < leng:
        if(next_ >= leng):
            break


        if(text[start] != '\n'):
            start = start + 1
            next_ = start
            continue

        if(text[next_] !='\n'):
            line = text[crop_at: start + 1]
            line = formatSentence(line)
            #pdb.set_trace()


            list_.append(line)
            crop_at = next_
            start = next_


            continue

        next_ = next_ + 1

    if(crop_at != next_):
        list_.append(formatSentence(text[crop_at: start + 1]))

    newString = ""

    for line in list_:
        if line == "" or line == "":
            continue
        newString += "{}".format(line)

    return newString

def formatSentence(text):
    text = bytes(text, "utf-8").decode('utf-8', 'ignore')

    text = text.replace('\a', "   ")
    text = text.replace('\r', " ")

    text = re.sub('\xa0', " ", text)
    text = re.sub("&nbsp", " ", text)
    text = re.sub("\u200b", " ", text)
    text = re.sub("./", " ", text)
    text = re.sub("•", "", text)
    text = re.sub("\”", "", text)
    text = re.sub("", "", text)
    text = re.sub("\t+", " ", text)
    text = re.sub(' +', " ", text)

    return text

def formatDocumentWithComma(text, comma):
    text = re.sub("[\n]+?[ ]+?[\n]+", "\n", text)
    # trường hợp trên đáng ra phải bao quá hết cả ở dưới nhưng vì 1 lý do nào đó mà không có tác dụng
    text = re.sub("[\n]+?[ ]+", "\n", text)
    text = splipWithEndLine(text)


    text = text.replace("…", "{}{}{}".format(comma, comma, comma))


    return text

def stringJsonToOject(str):
    return json.loads(str)

def objectToJson(object):
    jsonSTring = json.dumps(object, ensure_ascii = False).encode('utf8')
    return jsonSTring.decode()
