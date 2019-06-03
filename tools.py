from itertools import *
from generator import *
from chrono import *


def test_tools():
    funct_filter()
    group()
    pass


def funct_filter():
    work1 = [i for i in range(10000)]
    work2 = [i for i in primenumber(100)]

    parity_check = lambda x: x % 2 == 0

    is_prime_number = lambda x: x in primenumber(x)

    #print([i for i in work1 if parity_check(i)])

    #print([i for i in work1 if is_prime_number(i)])

    chrono1 = Chrono()
    chrono1.start()

    test1 = [i for i in work1 if parity_check(i)]

    chrono1.stop()

    chrono2 = Chrono()
    chrono2.start()

    test2 = list(filter(parity_check, work1))

    chrono2.stop()

    print(chrono1.get_duration())
    print(chrono2.get_duration())

    #print(test1)
    #print(test2)


def group():
    work = "aaaeeeerrraae"
    for e, i in groupby(work):
        print(e, " : ", len(list(i)))