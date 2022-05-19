c=0
while True:
    c+=1
    W=int(input())
    if W==0:
        break
    n=int(input())
    dp=[0]*(W+1)
    for i in range(n):
        v,w=map(int,input().split(','))
        for j in range(W,w-1,-1):
            dp[j]=max(dp[j],dp[j-w]+v)
    wg=0
    md=max(dp)
    for i in range(W+1):
        if md==dp[i]:
            wg=i
            break
    print("Case {0}:".format(c))
    print(md)
    print(wg)
