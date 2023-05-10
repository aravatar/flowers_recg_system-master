import requests
from lxml import etree
import os

def code(nam):
    if not os.path.exists('./{}/'.format(nam)):
        os.mkdir('./{}'.format(nam))
    
    url = 'https://www.plantplus.cn/cn/sp/'+nam
    #爬取到页面源码数据
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49'
    }
    response = requests.get(url=url,headers=headers)
    #手动设定编码
    # response.encoding = 'utf-8'
    # print(response)
    page_text = response.text
    # print(page_text)
    #数据解析：src属性值 alt属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="wbkbar"]/div[1]')
    for li in li_list:
        img_src = 'https://www.plantplus.cn'+li.xpath('./img/@src')[0]
    
    r=requests.get(img_src)
    with open('./'+nam+'/0.png', 'wb') as f: 
        f.write(r.content)
     
        
nam='向日葵'
code(nam)