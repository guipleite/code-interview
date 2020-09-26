def flipBitToWin(number):

    n_b = bin(number)[2:]

    arr = n_b.split('0')
    lenght = 0

    print(arr)

    for i in range(len(arr)-1):

        seq = len(arr[i]) + len(arr[i+1]) + 1

        if seq > lenght:
            lenght = seq

    return lenght

print(flipBitToWin(1775))


# 11011101111

# 11 2
# 111 3
# 1111 4