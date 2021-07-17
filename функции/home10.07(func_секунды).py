def seconds(sec):
    d = sec // (60 * 60 * 24)
    # print(d)

    sec = sec % (60 * 60 * 24)

    h = sec // (60 * 60)
    # print(h)

    sec = sec % (60 * 60)

    min = sec // 60
    # print(min)

    sec = sec % 60
    # print(sec)

#    print('{} суток, {} часов, {} минут, {} секунд'.format(d,h,min,sec))
    print(f'{d}:{h}:{min}:{sec}')

seconds(int(input('секунды: ')))
