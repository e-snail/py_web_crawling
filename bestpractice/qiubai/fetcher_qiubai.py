# -*- coding: utf-8 -*-
# refer to http://blog.csdn.net/a472770699/article/details/52524168

import urllib.request
import re
import _thread
import time


# ----------- 加载处理糗事百科 -----------
class Spider_Model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

        # 将所有的段子都扣出来，添加到列表中并且返回列表

    def GetPage(self, page):
        myUrl = " http://www.qiushibaike.com/8hr/page/" + page
        #      myUrl =" http://www.qiushibaike.com/8hr/page/2"
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(myUrl, headers=headers)
        myResponse = urllib.request.urlopen(req)
        myPage = myResponse.read()
        # encode的作用是将unicode编码转换成其他编码的字符串
        # decode的作用是将其他编码的字符串转换成unicode编码
        unicodePage = myPage.decode("utf-8")
        #    print(unicodePage)
        # 找出所有class="content"的div标记
        # re.S是任意匹配模式，也就是.可以匹配换行符
        myItems = re.findall('<div.*?class="content".*?>\n*<span>(.*?)</span>\n*</div>', unicodePage, re.S)
        items = []
        for item in myItems:
            # item 中第一个是div的标题，也就是时间
            # item 中第二个是div的内容，也就是内容
            items.append(item.replace("\n", ""))
        return items

        # 用于加载新的段子

    def LoadPage(self):
        # 如果用户未输入quit则一直运行
        while self.enable:
            # 如果pages数组中的内容小于2个
            if len(self.pages) < 2:
                try:
                    # 获取新的页面中的段子们
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print('无法链接糗事百科！')
            else:
                time.sleep(1)

    def ShowPage(self, nowPage, page):
        for items in nowPage:
            print(u'第%d页' % page, items)
            myInput = input()
            if myInput == "quit":
                self.enable = False
                break

    def Start(self):
        self.enable = True
        page = self.page
        print(page)
        print(u'正在加载中请稍候......')

        # 新建一个线程在后台加载段子并存储
        _thread.start_new_thread(self.LoadPage, ())

        # ----------- 加载处理糗事百科 -----------
        while self.enable:
            # 如果self的page数组中存有元素
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1


                # ----------- 程序的入口处 -----------


print(u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.4
   作者：why 修正：cferz
   日期：2016-09-13
   语言：Python 3.5.2
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
""")

print(u'请按下回车浏览今日的糗百内容：')
input(' ')
myModel = Spider_Model()
myModel.Start()