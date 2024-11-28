import json

from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from field import field


path = 'lab3-4/data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return list(i for i in Unique(field(arg,'job-name'), ignore_case = True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return dict(zip(arg, gen_random(len(arg), 100_000, 200_000)))


def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()
