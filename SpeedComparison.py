
#挿入法による並び替えを行う関数の為に数値の大小関係を判別する関数
def searcher(lis, item):

    r = len(lis)

    for i in lis:

        if i > item:

            r = lis.index(i)

            break

    return r


#挿入法による並び替えを行う関数
def inserter(lis):

    c = len(lis) - 1

    while c >= 0:

        t = lis.pop(0)

        idx = searcher(lis[c: ], t)

        lis.insert(c + idx, t)

        c = c - 1

    return lis


#不規則な数列を生成し並び替えて速度を表示する
def main():

    import random, time


    o = [random.randint(0, 9) for x in range(10)]

    print(o)


    s = time.perf_counter()

    r = inserter(o)

    e = time.perf_counter()


    print("self-defined: ", e - s)


    s = time.perf_counter()

    o.sort()

    e = time.perf_counter()


    print("Bulit-in: ", e - s)



if __name__ == "__main__":

    main()
