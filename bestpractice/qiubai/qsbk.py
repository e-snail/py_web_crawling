# -*- coding: cp936 -*-

import urllib.request
import urllib.response
import urllib.error
import re
import threading
import time

# ԭ������ https://my.oschina.net/freestyletime/blog/510724
# __author__ = "christian chen"


# re.compile()����RegexObject����
class Tool:
    def get_title(self):
        return re.compile('<title.*?>(.*?)</', re.S)

    def get_content(self):
        return re.compile('<div class="author.*?>.*?<a.*?<img.*?/>.*?</a>.*?<h2>(.*?)</h2>.*?</a>.*?</div>.*?<div.*?class="content.*?>(.*?)</div>.*?class="number.*?>(.*?)</.*?', re.S)


# �̳���threading.Thread����Ҫ����run()����
class QSBK(threading.Thread):

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
            # content = response.read().decode('utf-8', 'ignore')
            # content = content.encode('gbk', 'ignore')
            return content

        except urllib.error as e:
            if hasattr(e, "reason"):
                print("error: ", e.reason)
                return None

    def get_page_detail(self, c):
        # re.findall(pattern, string, flags=0)
        # �ҵ�REƥ��������Ӵ�������������Ϊһ���б���
        items = re.findall(self.tool.get_content(), c)
        result = []
        for item in items:
            p = {}
            p['������'] = item[0].strip()
            p['id'] = item[2].strip()
            p['����'] = item[1].strip()
            result.append(p)
        return result

    def get_title(self, c):
        result = re.findall(self.tool.get_title(), c)
        return result[0].strip()

    def run(self):
        print("---- " + time.ctime() + " ----\n")
        for page in range(1, self.maxPage):
            c = self.get_page_content(page)
            if c is None:
                print("URL��ʧЧ��������")
                return

            print("---- ����ץȡ��" + str(page) + "ҳ ---- ")
            title = self.get_title(c)
            f = open(title + ' - Page_' + str(page) + '.txt', 'w')
            result = self.get_page_detail(c)
            cut_ine = u'-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.\n'
            for item in result:
                f.write(cut_ine)
                for K, V in item.items():
                    f.write(str(K) + ' : ' + str(V) + '\n')
            print("---- ��" + str(page) + "ҳץȡ��� ----\n")

            f.close()
            del result
            del f
            del cut_ine
            del c
        print("---- " + time.ctime() + " ----")


maxPage = input("������ץȡ�����°ٿƵ����ҳ��: \n")
qsbk = QSBK(maxPage)
qsbk.start()

