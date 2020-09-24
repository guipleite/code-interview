def flipBitToWin(number):

    n_b = bin(number)[2:]

    arr = n_b.split('0')
    l = 0

    for i in range(len(arr)-1):

        if len(arr[i]) + len(arr[i+1]) > l:
            l = len(arr[i]) + len(arr[i+1])

    l+=1

    return l

print(flipBitToWin(1775))