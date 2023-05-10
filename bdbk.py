# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:18:19 2022

@author: gldz
"""

import re
from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup as sp

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
bracket = re.compile(r'\[\d*]')


def look_up(entry):
    url = "https://baike.baidu.com/item/" + quote(entry)
    req = request.Request(url, headers=header)
    html = request.urlopen(req).read()
    soup = sp(html, "html.parser")
    out='百度百科：\n'
    content=soup.findAll('div',{'class':'para'})
    forei=''
    for i in content:
        # i=i.get_text()
        # # i=i.replace('\n','')
        # i=i.replace('\r','')
        # i=re.sub(bracket,'',i)
        try:
            pic_word = i.find("div",class_="lemma-picture text-pic layout-right").get_text() # 去掉文字中的图片描述
            try:
                pic_word2 = i.find("div", class_="description").get_text() # 去掉文字中的图片描述
                i = i.get_text().replace(pic_word, '').replace(pic_word2, '')
            except:
                i = i.get_text().replace(pic_word, '')
 
        except:
            try:
                pic_word2 = i.find("div", class_="description").get_text() # 去掉文字中的图片描述
                i = i.get_text().replace(pic_word2, '')
            except:
                i = i.get_text()
        
        if forei=='\n' and i[len(i)-1]=='\n':
            forei='\n'
            i=i.replace('\n',' ')
        else:
            forei=i[len(i)-1]
            
        out=out+i
    return out
        
out=look_up("玫瑰")
# print(out)


    
    
    
    
    
    