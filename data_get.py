
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 09:28:40 2022

@author: gldz
"""

import re
import requests
import time 
from urllib import parse 
import os #文件操作
from fake_useragent import UserAgent #随机生成一个user-agent

class Picture:

    #请求30张图片的链接
    def get_one_html(self,url,pn):
        response = requests.get(url=url.format(self.name,self.name, pn, self.times), headers=self.headers).content.decode('utf-8')
        return response

    #请求单张图片内容
    def get_two_html(self,url):
        response = requests.get(url=url, headers=self.headers).content
        return response

    #解析含30张图片的html的内容
    def parse_html(self,regex,html):
        content = regex.findall(html)
        return content

    #主函数
    def run(self,tar,totalnum):
        # self.name_ = tar
        if tar=='玫瑰':
            self.name_ = 'roses'
        if tar=='雏菊':
            self.name_ = 'daisy'
        if tar=='向日葵':
            self.name_ = 'sunflowers'
        if tar=='郁金香':
            self.name_ = 'tulips'
        if tar=='蒲公英':
            self.name_ = 'dandelion'
        
        self.name = parse.quote(self.name_) 
        self.times = str(int(time.time()*1000)) 
        self.url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8032920601831512061&ipn=rj&ct=201326592&is=&fp=result&fr=&word={}&cg=star&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn={}&rn=30&gsm=1e&{}='
        self.headers = {'User-Agent':UserAgent().random}
        nu=0
        # #判断该目录下是否存在与输入名称一样的文件夹 如果没有则创建 有就不执行if下的创建
        # if not os.path.exists('./flower_data2/flower_photos/{}/'.format(self.name_)):
        #     os.mkdir('./flower_data2/flower_photos/{}'.format(self.name_))
        response = self.get_one_html(self.url,0)
        regex1 = re.compile('"displayNum":(.*?),')
        num = self.parse_html(regex1,response)[0] #获取总的照片数量
        print('该关键字下一共有{}张照片'.format(num)) #打印总的照片数量

        #判断总数能不能整除30
        if int(num)%30 == 0:
            pn = int(num)/30
        else:
            # 总数量除30是因为每一个链接有30张照片 +2是因为要想range最多取到该数就需要+1
            # 另外的+1是因为该总数除30可能有余数，有余数就需要一个链接 所以要+1
            pn = int(num)//30 + 2
        for i in range(pn): #遍历每一个含30张图片的链接
            resp = self.get_one_html(self.url, i * 30)
            regex2 = re.compile('"middleURL":"(.*?)"')
            urls = self.parse_html(regex2,resp) #得到30张图片的链接（30个）
            for u in urls:  #遍历每张图片的链接
                content = self.get_two_html(u) #请求每张图片的内容
                # 打开该关键字下的文件写入图片
                with open('./flower_data/flower_photos/{}/{}.jpg'.format(self.name_,u[28:35]),'wb') as f:
                    f.write(content)
                nu=nu+1
                if nu==totalnum:
                    return
                #print('完成一张照片') #下载完一张图片后打印


if __name__ == '__main__':
    tar='玫瑰'
    totalnum=85
    spider = Picture()
    spider.run(tar,totalnum)





