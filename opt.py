def main():
    x, n = map(int, input().split())
    a=[]
    for i in range(n):
        arr =list(map(int, input().split()))
        arr.append(i+1)
        a.append(arr)
    a.sort()
    a.reverse()
    rest_weight=x
    l=[]
    for j in range(n):
        p=rest_weight//(10**a[j][0])
        if p>0 and p<=a[j][1]:
            rest_weight=rest_weight-(p*10**a[j][0])
            l.append(a[j][2])
    if rest_weight==0:
        print(len(l))
        for w in range(len(l)):
            print(l[w], end=" ")
    else:
        print(-1)
    return
if __name__ == '__main__':
    main()


