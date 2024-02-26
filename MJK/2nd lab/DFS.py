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

# depth-first search algorithm...
def dfs(root):
    visited.append(root)
    for child in graph[root]:
        dfs(child)

dfs(root)
print("DFS : ")
print(visited)

# function for find parent of a child
def _find_parent(child):
    parent = []
    for p in graph:
        for c in graph[p]:
            if c==child:
                parent.append(p)
                break
    return parent

# find a path to reach goal...
goal = "G"
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

print("\nHere is the path : ")
print(result)

