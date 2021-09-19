from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests
import os
from datetime import datetime
import re
import pdb
import traceback
import sys
import json
import TextToLine as ttl
from multipledispatch import dispatch

def save_data(src_text, file_path):    
            
    if not src_text:
        print("empty file: ")
    else:
        if os.path.isfile(file_path +".txt"):
            return
        
        f = open(file_path +".txt", "w", encoding='utf-8')                
        
        #code này để tạm thời
        lim_src = len(src_text)                    
       
        text_src = ""
        
        for index in range(0, lim_src):
            
            text_src = src_text[index]                                      
            #if tgt_text[index] != "" and 
            f.write(text_src+"\n")                  
            text_src = ""
            
        f.close()
        
    return

def getLink(url):
    list_url = list()
    
    
    try:
        page_index = 1
        
        while( True ):
            print(url.format(page_index))
            #pdb.set_trace()
            response = requests.get(url.format(page_index))
            soup = BeautifulSoup(response.text, "lxml")
            
            div_tag = soup.findAll("div", {"class":"boxtinmoi"})
            
            if not div_tag:
                break
                
            li_tags = div_tag[0].findAll("li")
            
            
            if not li_tags:
                break
                
            for li_tag in li_tags:
                
                href = li_tag.a.attrs['href']
                title = li_tag.a.h3.text
                title = title.replace("\n","")
                title = title.replace("\t","")
                title = title.replace("\a","")
                title = title.replace("\r","")
                title = title.replace("&nbsp","")
                
                
                response = requests.get(href)
                soup = BeautifulSoup(response.text, "lxml")
                
                if( soup.find( "span", {"class":"pubdate"}) ):
                    date = soup.find( "span", {"class":"pubdate"}).text
                    date = date.split("-")[0].strip()
                    date = date.replace("\t","").replace("&nbsp","")
                    list_url.append( (href, date, title) )
            page_index = page_index + 1
    except:
        traceback.print_exc()
        pass    
    return list_url
    
def getContent(url, title , lang):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    list_sentence = list()
    
    list_sentence.append(title)
    
    if(lang == "vi"):
        list_sign = list(map_vi2ja_end_sign.keys())
    else: 
        list_sign = list(map_vi2ja_end_sign.values())
    
    div_tag = soup.find("div", {"id":"newscontents"})
    
    list_sentence = list_sentence + ttl.slpit_text(div_tag.text,list_sign)
    
    return list_sentence
    
def crawlFormLink(url , title ,file_path, lang):

    sentences = getContent(url, title , lang)
    
    file_name = url.split("-")
    file_name = file_name[len(file_name) - 1]
    
  
    
    file_path = file_path + "{}.{}".format(file_name, lang)
    print(file_path +".txt")
 
    if os.path.isfile(file_path +".txt"):
        
        return
    print(file_name)
    
    save_data(sentences, file_path)
     
    
map_vi2ja_end_sign = {}

if __name__ == '__main__':
    
    src_lang_ = "vi"
    tgt_lang_ = "km"
    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    with open(current_dir + "/Sign/sign-default.txt", 'r',encoding='utf8') as file:
            map_vi2ja_end_sign = json.load(file)
        
    if os.path.exists(current_dir + "/Sign/sign-"+tgt_lang_+".txt"):
       with open(current_dir + "/Sign/sign-"+tgt_lang_+".txt", 'r') as file:
            map_vi2ja_end_sign = json.load(file)
            
    TH1_folder = current_dir + "/Data/crawler_success/CanTho/vi/"
    TH2_folder = current_dir + "/Data/crawler_success/CanTho/km/"
    
    if not os.path.exists(TH1_folder):
        os.makedirs(TH1_folder)

    if not os.path.exists(TH2_folder):
        os.makedirs(TH2_folder)
        
    folder_lang = src_lang_+"-"+tgt_lang_
    
    crawl_folder = current_dir + "/CanThoCrawler"
    
    file_resoucre = crawl_folder+"/linkauto/"+folder_lang+".txt"
    
    f = None
    
    if os.path.isfile(file_resoucre):
        f = open(file_resoucre,'r', encoding='utf-8')
        
    else:
        folder_lang = tgt_lang_+"-"+src_lang_
        file_resoucre = crawl_folder+folder_lang+".txt"
        
        if os.path.isfile(file_resoucre):
            f = open(file_resoucre,'r', encoding='utf-8')         
        
    
    folder_list = list()
    
    if(f != None):
            
        for line in f:           
            folder_list.append(line.replace('\n',''))         
        f.close()
        
        for folder in folder_list:
            
            src_link = list()
            tgt_link = list()
            
            print(folder)
            #kiem tra xem folder co ton tai hay khong
            if not os.path.isfile(crawl_folder+"/link/{}/{}/link.txt".format(src_lang_, folder)) or  not os.path.isfile(crawl_folder+"/link/{}/{}/link.txt".format(tgt_lang_, folder)):
                # Tao thu muc
                
                if not os.path.exists(( crawl_folder+"/link/{}/{}/".format(src_lang_, folder ))):
                    os.makedirs(crawl_folder+"/link/{}/{}/".format(src_lang_, folder) )
                    
                if not os.path.exists(( crawl_folder+"/link/{}/{}/".format(tgt_lang_, folder ))):   
                    os.makedirs(crawl_folder+"/link/{}/{}/".format(tgt_lang_, folder) )
                
                link_file = open(crawl_folder+"/linkauto/{}/{}.txt".format(folder_lang, folder) , "r", encoding="utf-8")
                array_link = link_file.readline().replace('\n','').split("\t")
                link_file.close()
                
                #Lay link tat ca cac bai viet. Roi dua vao giong hang.
                if not os.path.isfile(crawl_folder+"/link/{}/{}/link.txt".format(src_lang_, folder)):
                
                    src_link = getLink(array_link[0])
                    f = open(crawl_folder+"/link/{}/{}/link.txt".format(src_lang_, folder), "w", encoding="utf-8" )
                    for line in src_link:
                        
                            f.write( "{}\t{}\t{}\n".format(line[0], line[1], line[2]) )
                    f.close()
                    
                if not os.path.isfile(crawl_folder+"/link/{}/{}/link.txt".format(tgt_lang_, folder)):
                
                    tgt_link = getLink(array_link[1])
                    f = open(crawl_folder+"/link/{}/{}/link.txt".format(tgt_lang_, folder), "w", encoding="utf-8" )
                    for line in tgt_link:
                            
                            f.write( "{}\t{}\t{}\n".format(line[0], line[1], line[2]) )
                    f.close()      
            else:
                
                f = open(crawl_folder+"/link/{}/{}/link.txt".format(src_lang_, folder), "r", encoding="utf-8" )
                
                for line in f:
                    line = line.replace("\n","")
                    if(line != "" and line != " "):
                        src_link.append(line.split("\t"))
                f.close()
                
                f = open(crawl_folder+"/link/{}/{}/link.txt".format(tgt_lang_, folder), "r", encoding="utf-8" )
                
                for line in f:
                    line = line.replace("\n","")
                    if(line != "" and line != " "):
                        tgt_link.append(line.split("\t"))
                f.close()
                
               
                link_file = open(crawl_folder+"/linkauto/{}/{}.txt".format(folder_lang, folder) , "r", encoding="utf-8")
                array_link = link_file.readline().replace('\n','').split("\t")
                link_file.close()
                
            for link in src_link:
                try:
                    time = datetime.strptime(link[1] , '%d/%m/%Y')
                    time = time.strftime("%Y/%m")
                    
                    save_folder = "{}/{}/{}/".format(TH1_folder, folder, time)
                    if not os.path.exists(save_folder):
                        os.makedirs(save_folder)
                    
                
                    crawlFormLink(link[0] , link[2] ,save_folder, "vi")
                   
                except:
                    traceback.print_exc()
                        
            for link in tgt_link:
                try:
                    time = datetime.strptime(link[1] , '%d/%m/%Y')
                    time = time.strftime("%Y/%m")
                    
                    save_folder = "{}/{}/{}/".format(TH2_folder, folder, time)
                    if not os.path.exists(save_folder):
                        os.makedirs(save_folder)
                        
                
                    crawlFormLink(link[0] , link[2] ,save_folder, "km")
                    
                except:
                    traceback.print_exc()
            os.system("cls")        