
from utils import *
from hashlib import *


def solve1(data):

    t = 1
    while 1:
        to_hash = data+str(t)
        to_hash = to_hash.encode()
        ret = md5(to_hash).hexdigest()
        #print(ret, t)

        if ret[:5] == "00000":
            print(t)
            break
        t += 1


def solve2(data):
    t = 1
    while 1:
        to_hash = data+str(t)
        to_hash = to_hash.encode()
        ret = md5(to_hash).hexdigest()
        #print(ret, t)

        if ret[:6] == "000000":
            print(t)
            break
        t += 1


data = "yzbqklnj"

solve1(data)
solve2(data)