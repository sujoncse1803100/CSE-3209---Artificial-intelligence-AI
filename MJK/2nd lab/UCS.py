tree={
    "S":[{"A":5},{"B":2},{"C":4}],
    "A":[{"D":9},{"E":4}],
    "B":[{"G":6}],
    "C":[{"F":2}],
    "D":[{"H":7}],
    "E":[{"G":6}],
    "F":[{"G":1}],
    "G":[],
    "H":[]
}

def sorting(data):
    print(data)
    

visited=[{"node":"S","weight":0,"parent":""}]
frontier=[{"node":"S","weight":0,"parent":""}]
root="S"
goal="E"

def sorting(e):
    return e["weight"]

def add(n,w):

    for x in tree[n]:
        key=list(x.keys())[0]
        child={
            "node":key,
            "weight":x[key]+w,
            "parent":n,
        }
        frontier.append(child)
        visited.append(child)

def ucs(root):
    data={
        "cost":0,
        "goal":"G",
        "goalParent":""
    }
    while frontier:
        frontier.sort(key=sorting)
        child=frontier.pop(0)
        keys=list(child.keys())
        n=child[keys[0]]
        w=child[keys[1]]

        if n==goal:
            data["cost"]=w
            data["goalParent"]=child[keys[2]]
            break
        else:
            add(n,w)
    return data
        
data = ucs(root)      

path=[]
def find_path(goal):
    path.append(goal)
    child=data["goalParent"]
    print("child : "+child)
    while True:
        for x in visited: 
            key=list(x.keys())
            if x[key[0]] == child:
                path.insert(0,child)
                child=x[key[2]]
        if(child==""):
            break

find_path(goal)

print("Path is :-\n",path)
print("Cost of this path is : ",data["cost"])