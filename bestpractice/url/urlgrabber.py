import urllib.error
import urllib.request


# 封装print，打印可变参数
def print_msg(msg, *params):
    composed = msg
    i = 0
    while i < len(params):
        i += 1
        composed += " %r "

    print(composed % params)


# usage 1 urlopen directly
response = urllib.request.urlopen('http://python.org/')
html = response.read()

# usage 2 use Request
request = urllib.request.Request('http://python.org/')

# 截获异常
try:
    response1 = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print("error code:%d" % e.code)
    print("error message:%s" % e.read.decode("utf8"))

# 请求返回码
print_msg("return code:", response1.getcode())

# login CSDN
url_csdn_login = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
values = {"username":"wilbur.unail@gmail.com","password":"bitsnail"}

url_values = urllib.parse.urlencode(values)
url_values = url_values.encode(encoding='UTF8')

url_last = urllib.request.Request(url_csdn_login, url_values)

try:
    response = urllib.request.urlopen(url_last)
except urllib.error.HTTPError as e:
    print('Error code:',e.code)
except urllib.error.URLError as e:
    print('Reason',e.reason)

print_msg("login csdn with return code ", response.getcode())

the_csdn_page = response.read()

print(the_csdn_page)