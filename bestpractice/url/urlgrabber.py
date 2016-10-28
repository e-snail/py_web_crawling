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


