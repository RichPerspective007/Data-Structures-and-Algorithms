all_paths = []
def findAllPaths(vertices,gList,source,destination,path = []):
    global all_paths
    path.append(source)
    for i in gList[source]:
        if i in path:
            continue
        elif i == destination:
            path.append(i)
            all_paths.append(path)
            return
        else:
            path.append(i)
            return (findAllPaths(vertices,gList,i,destination,path))
    
    return all_paths