import math
tree={
    "S":[{"A":1,"h":8},{"B":5,"h":4},{"C":8,"h":3}],
    "A":[{"D":3,"h":math.inf},{"E":7,"h":math.inf},{"G":9,"h":0}],
    "B":[{"G":4,"h":0}],
    "C":[{"G":5,"h":0}],
    "D":[],
    "E":[],
    "G":[],
}

def sorting(data):
    print(data)
    

visited=[{"n":"S","w":0,"h":8,"p":""}]
frontier=[{"n":"S","w":0,"h":8,"p":""}]
root="S"
goal="G"

def sorting(e):
    return e["h"]

def add(c,w):

    for x in tree[c]:
        n=list(x.keys())[0]
        h=list(x.keys())[1]
        child={
            "n":n,
            "w":x[n]+w,
            "h":x[h],
            "p":c,
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
        c=child[keys[0]]
        w=child[keys[1]]

        if c==goal:
            print(child)
            data["cost"]=w
            data["goalParent"]=child[keys[3]]
            print(child[keys[3]])
            break
        else:
            add(c,w)
    return data
        
data = ucs(root)    
print(visited)  

path=[]
def find_path(goal):
    path.append(goal)
    child=data["goalParent"]

    while True:
        for x in visited: 
            key=list(x.keys())
            if x[key[0]] == child:
                path.insert(0,child)
                child=x[key[3]]
        if(child==""):
            break

find_path(goal)

print("Path for GBFS is :-\n",path)
print("Cost of this path is : ",data["cost"])