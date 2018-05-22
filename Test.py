import re
import bs4
import urllib.request
from janome.tokenizer import Tokenizer

#########################################################################
# Utility functions 
def messageBox():
    from tkinter import Tk, messagebox

    root = Tk()
    root.withdraw()
    messagebox.showinfo('title', 'message')
    root.quit()

def split_sentence( sentence ):
    from janome.tokenizer import Tokenizer

    data = []
    each_data = []

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize( sentence )

    for token in tokens:
        partOfSpeech = token.part_of_speech.split(',')[0]
        # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
        if partOfSpeech == u'名詞':
            data.append(token.surface )

    return data
"""
url='http://it-trend.jp/erp'
soup = bs4.BeautifulSoup( urllib.request.urlopen(url).read(),"html.parser")
title = soup.title.string
description = soup.find(attrs={"name":re.compile(r'Description',re.I)}).attrs['content']
h1=soup.h1.string
contents = title+description+h1
output_words=[]

print( split_sentence(contents) )
"""

#########################################################################
#   Version Ckeck functions
def listmaler_FireFox(url):
    soup = bs4.BeautifulSoup( urllib.request.urlopen(url).read(),"html.parser")
    # description = soup.find(attrs={"id":re.compile(r'main-content',re.I)})
    # 上みたいな書き方もできる
    description = soup.find("div", attrs={"id":"main-content"})
    versionList=description.find_all("a")

    for item in versionList:
        from urllib.parse import urljoin
        
        print( item.string, urljoin(url,item.get("href")) )

url='https://www.mozilla.org/en-US/firefox/releases/'
listmaler_FireFox(url)



