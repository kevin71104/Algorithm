#==== Algorithm 2017 -- Hw4 ====
#==== Collaborator : B03901134 袁培傑 ====
c, r = (int(x) for x in input().split(' '))
graph = [list() for k in range(c)] # adjacent list
for k in range(r):
    c1, c2 = (int(x) for x in input().split(' '))
    graph[c1-1].append(c2-1)
    graph[c2-1].append(c1-1)

#==== pick vertex by largest degree ====
sel = []
graph = sorted(enumerate(graph), key = lambda adjList: len(adjList[1]), reverse=True)
for idx, adjList in graph:
    for node in adjList:
        if node not in sel:
            sel.append(idx) # if there is still an edge not yet covered by
            break
#==== For Output ====
sel = sorted(sel)         # sorted the selected city
print(len(sel))
for k in range(len(sel)):
    if k == len(sel) - 1:
        print(sel[k]+1)
    else:
        print(str(sel[k]+1), end=' ')
