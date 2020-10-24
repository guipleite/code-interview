def troca(n):
    coins=[25, 10, 5, 1]
    ans = []


    for i in range(n+1):
        ans.append(0)
	
    ans[0] = 1

    for coin in coins:

        for curr in range(coin,n+1):

            nval = curr - coin
            ans[curr] += ans[nval]

    return ans[-1]
