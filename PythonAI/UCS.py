def ucs(graph , start , goal):
    list=[(0,start)]
    while list:
        list.sort()
        cost,node=list.pop(0)
        if node==goal:
            return f"Reached Goal:{goal} with cost:{cost}"
        for neighbour,p_cost in graph[node]:
            list.append((cost+p_cost,neighbour))

graph={'a':[('b',1),('c',2)],
       'b':[('d',3),('e',4)],
       'c':[('d',3)],
       'd':[]}

print(ucs(graph ,'a','d'))
