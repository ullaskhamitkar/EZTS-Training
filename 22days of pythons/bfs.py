a={
    1:[(1,2,0),(1,3,0)],
    2:[(2,1,0),(2,7,0)],
    3:[(3,1,0),(3,6,0),(3,5,0)],
    4:[(4,7,0),(4,8,0)],
    5:[(5,3,0),(5,7,0)],
    6:[(6,3,0),(6,8,0)],
    7:[(7,2,0),(7,5,0),(7,4,0)],
    8:[(8,4,0),(8,6,0),(8,1,0)]
}
e=1
def bfs(a,e):
    Q=[e]
    v={}
    for i in a.keys():
        v[i] = False
    while len(Q) != 0:
        curr = Q.pop(0)
        print(curr)
        if v[curr] == False:
            v[curr] = True
        for i in a[curr]:
            if v[i[1]]==False:
                Q.append(i[1])
                v[i[1]] = True
dog = bfs(a,1)
print(dog)