def nonConstructibleChange(coins):
    coins.sort()
    lpc=0
    for i in range(len(coins)):
        if coins[i]>lpc+1:
            return lpc+1
        else:
            lpc+=coins[i]
    return lpc+1