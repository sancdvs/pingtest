from pythonping import ping
import time
import datetime

ip = ''
file = ''
log = ''

def test():
    p = ping(ip)
    for i in p:
        if i.success:
            print(1)
            with open(file,'w') as f:
                f.write(str(p))
            break
        else:
            print(0)
    with open(log,'r+') as f:
        content = f.read()
        f.seek(0)
        ps = str(p).split('\n')
        s = str(datetime.datetime.now())+'\r'+ps[0]+ps[1]+ps[2]+ps[3]+ps[5]+'\r'
        f.write(s+'\n'+content)



while True:
    try:
        test()
    except:
        pass
    time.sleep(60)





