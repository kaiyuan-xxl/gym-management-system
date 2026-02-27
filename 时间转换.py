import datetime
def time_tra():
    mid = str(datetime.datetime.today())
    x = list(mid)
    result = []
    for i in range(10):
        result.append(x[i])
    last = ''.join(result)
    b = datetime.date(*map(int, last.split('-')))
    return b
if __name__ == '__main__':
    print(time_tra())
    print(type(time_tra()))
