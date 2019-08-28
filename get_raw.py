from urllib import request
import random
import time
url = 'https://login.sina.com.cn/cgi/pin.php'
for i in range(1000):
    print(i)
    request.urlretrieve(url, 'raw/'+random.randint(10000000, 99999999).__str__()+'.png')
    time.sleep(1)
