def rec_string(s):
    s = s.lower()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

if __name__ == '__main__':
    test = rec_string('BAASTTTTTA')
    print(test)
