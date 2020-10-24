def magic_index_brute(arr):
    if arr:
        for idx, n in enumerate(arr):
            if idx == n:
                print(idx,n)
                return idx
    return -1

print(magic_index_brute([-20,0,1,2,3,4,5,7,20]))