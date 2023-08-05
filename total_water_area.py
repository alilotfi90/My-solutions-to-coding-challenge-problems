def max_exp(lis):
    n=len(lis)
    dp_a=[0]*n
    dp_a_b=[0]*n
    dp_a_b_c = [0] * n
    dp_a_b_c_d = [0] * n

    print(lis)
    for i in range(n):
        if i==0:
            dp_a[i]=lis[i]
            continue
        dp_a[i] = max(lis[i],dp_a[i-1])

    for i in range(1,n):
        if i==1:
            dp_a_b[i]=dp_a[i-1]-lis[i]
            continue
        dp_a_b[i] = max(dp_a_b[i-1],dp_a[i]-lis[i])

    for i in range(2,n):
        if i==2:
            dp_a_b_c[i]=dp_a_b[i-1]+lis[i]
            continue
        dp_a_b_c[i] = max(dp_a_b_c[i-1],dp_a_b[i]+lis[i])

    for i in range(3,n):
        if i==3:
            dp_a_b_c_d[i]=dp_a_b_c[i-1]-lis[i]
            continue
        dp_a_b_c_d[i] = max(dp_a_b_c_d[i-1],dp_a_b_c[i]-lis[i])
    print(dp_a)
    print(dp_a_b)
    print(dp_a_b_c)
    print(dp_a_b_c_d)

    return max(dp_a_b_c_d[i] for i in range(3,n))








lis=[3, 6, 1, -3, 2, 7]
max_exp(lis)
