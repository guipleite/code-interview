
def check_pal(inp):
    word = inp.lower()

    dict_count = {}

    odd_flag = False

    for i in range(len(word)):
        if word[i] != ' ':
            dict_count[word[i]] = 0

    for c in word:
        if c != ' ':
            dict_count[c]+=1

    for key in dict_count:
        if dict_count[key]%2 != 0:

            if not odd_flag:
                odd_flag  = True
            else:
                return False 

    return True


inp = "azAZ"
print(check_pal(inp))
