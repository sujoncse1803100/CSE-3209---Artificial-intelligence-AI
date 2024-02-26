graph={
    "S":["A","B","C"],
    "A":["D","E"],
    "B":["G"],
    "C":["F"],
    "D":["H"],
    "E":["G"],
    "F":["G"],
    "G":[],
    "H":[]
}

root="S"
visited=[]
queue=[]

def bfs(visited,graph,goal):
    visited.append(root)
    queue.append(root)

    while queue:
        m=queue.pop(0)
        isFound=False

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            if neighbour==goal:
                isFound=True
                break
        if isFound:
            break   

goal="G"
bfs(visited,graph,goal)

def _find_parent(child):
    parent = []
    for p in graph:
        for c in graph[p]:
            if c==child:
                parent.append(p)
                break
    return parent

result=[goal]
child=goal
while True:
    parent=_find_parent(child)

    for x in visited:
        done=False
        for p in parent:
            if p==x:
                result.insert(0,p)
                done=True
                child=p
                break
        if done:
            break
    if child==root:
        break

print(result)