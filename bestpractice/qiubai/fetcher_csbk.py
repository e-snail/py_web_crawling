# -*- coding: cp936 -*-
__author__ = "christian chen"
import urllib.error
import urllib.response
import urllib.request
import re
import threading
import time


class Tool:
    def pTitle(self):
        return re.compile('<title.*?>(.*?)</', re.S)

    def pContent(self):
        return re.compile(
            '<div class="author.*?>.*?<a.*?<img.*?/>(.*?)</a>.*?</div>.*?<div.*?class="content.*?>(.*?)</div>.*?class="number.*?>(.*?)</.*?', re.S)


# CSBK类继承自threading.Thread
class CSBK(threading.Thread):
    def __init__(self, max_page):
        threading.Thread.__init__(self, name='christian_thread')
        self.baseUrl = "http://www.qiushibaike.com/hot/page/"
        self.maxPage = int(max_page) + 1
        self.tool = Tool()

    def get_page_content(self, page_num):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        url = self.baseUrl + str(page_num)
        try:
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            # content = content.encode('gbk', 'ignore')
            return content
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                print("error: ", e.reason)
                return None

    def get_page_detail(self, c):
        items = re.findall(self.tool.pContent(), c)
        result = []
        for item in items:
            p = {}  #???这里有啥问题
            p['发布人'] = item[0].strip()
            p['id'] = item[2].strip()
            p['内容'] = item[1].strip()
            result.append(p)
        return result

    def getTitle(self, c):
        result = re.findall(self.tool.pTitle(), c)
        return result[0].strip()

    def run(self):
        print("---- " + time.ctime() + " ----\n")
        for page in range(1, self.maxPage):
            c = self.get_page_content(page)
            if c is None:
                print("URL已失效，请重试")
                return

            print("---- 正在抓取第" + str(page) + "页 ---- ")
            title = self.getTitle(c)
            f = open(title + ' - Page_' + str(page) + '.txt', 'w')
            result = self.get_page_detail(c)
            cutLine = u'-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.\n'
            for item in result:
                f.write(cutLine)
                for K, V in item.items():
                    f.write(str(K) + ' : ' + str(V) + '\n')
            print("---- 第" + str(page) + "页抓取完毕 ----\n")

            f.close()
            del result
            del f
            del cutLine
            del c
        print("---- " + time.ctime() + " ----")


maxPage = input("输入想抓取的糗事百科的最大页数: \n")
csbk = CSBK(maxPage)
csbk.start()


