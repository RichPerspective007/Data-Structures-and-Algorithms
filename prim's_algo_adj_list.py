def FiberLink(distance_map):
    small = float('inf')
    tree = []
    total_cost = 0
    vertices = list(distance_map.keys())
    for i in distance_map.keys():
        for j in distance_map[i]:
            if j[1]<small:
                small = j[1]
                tree = [i,j[0]]
    total_cost+=small
    while (len(tree)<len(vertices)):
        small = float('inf')
        nextv = -1
        for i in tree:
            for j in distance_map[i]:
                if j[0] in tree:
                    continue
                if j[1]<small:
                    small = j[1]
                    nextv = j[0]
        total_cost+=small
        tree.append(nextv)
    
    print(tree)
    return total_cost
    

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))