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

data=[{"n":"S","g":0,"h":8,"f":8,"h_s":9,"p":""}]
frontier=[{"n":"S","g":0,"h":8,"f":8,"h_s":9,"p":""}]

root="S"

def to_do(child):
    keys=list(child.keys())
    for x in tree[child[keys[0]]]:
        cKeys=list(x.keys())
        c={
            "n":cKeys[0],
            "g":x[cKeys[0]]+child[keys[1]],
            "f":0,
            "h_s":0,
            "p":child[keys[0]]
        }

        data.append(c)
        frontier.append(c)

def A_Star():
    while frontier:
        child=frontier.pop(0)
        to_do(child)

A_Star()

print(data)