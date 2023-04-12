print("请输入秒数")
sec=eval(input())
hour=sec//3600
sec=sec-3600*hour
minu=sec//60
sec=sec-60*minu
print(hour,":",minu,":",sec)