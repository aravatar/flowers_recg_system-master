# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:08:33 2022

@author: gldz
"""

from wordcloud import WordCloud
from imageio import imread
mask=imread('1.jpg')
with open('1.txt',encoding="utf-8") as f:
    txt=f.read()
wordcloud=WordCloud(background_color="white",\
                    font_path='C:\\Windows\\Fonts\\simfang.ttf',\
                    width=800,\
                    height=600,\
                    max_words=1000,\
                    max_font_size=80,\
                    mask=mask)

wordcloud.generate_from_text(txt)
wordcloud.to_file('1.png')