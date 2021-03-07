from pythonping import ping
import time

ip = ''
file = ''

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



while True:
    try:
        test()
    except:
        pass
    time.sleep(60)





