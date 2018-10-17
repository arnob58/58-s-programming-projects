def finding_zeros(n):
    power = 0
    num = n
    trailing = 0
    for i in range(1000):
        if round(num/5)>0:
            power += 1
            num = num/5
        else:
            break
    if power>0:
        for i in range(0,power+1):
            trailing += n/(5**i)
            #print(trailing)
    else:
        trailing = 0
        n =0
    return int(trailing-n)


print(finding_zeros(1100))

