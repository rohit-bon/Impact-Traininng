def get_max_occuring_char(str1):
    ASCII_SIZE = 256
    ctr = [0] * ASCII_SIZE
    max = -1
    ch = ''
    for i in str1:
        ctr[ord(i)] += 1
    for i in str1:
        if max < ctr[ord(i)]:
            max = ctr[ord(i)] 
            ch = i 
    return ch

strin = input()
rep = input()

freq = get_max_occuring_char(strin)
print(strin.replace(freq, rep))
