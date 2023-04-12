import time
def t():
    return(time.localtime())
print("现在是{}.{}.{} {}:{}:{}".format(t()[0],t()[1],t()[2],t()[3],t()[4],t()[5]))
