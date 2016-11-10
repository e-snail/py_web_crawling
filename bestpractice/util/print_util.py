

# 封装print，打印可变参数
def print_msg(msg, *params):
    composed = msg
    i = 0
    while i < len(params):
        i += 1
        composed += " %r "

    print(composed % params)

