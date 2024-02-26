tree = {
    "X":["A"],
    "Y":["A","B"],
    'A':['C','D'],
    'B':['E'],
    'C':['F']
}



def _find_parent(child):
    parent = []
    for p in tree:
        for c in tree[p]:
            if c==child:
                parent.append(p)
    return parent


def _find_grandParent(child):
    grand_parent = []
    parent = _find_parent(child)
    for p in parent:
        gp = _find_parent(p)
        for i in gp:
            grand_parent.append(i)
    return grand_parent


t=int(input("Enter your test case : "))
for x in range(t):
    print('For parent press p or for grand-parent press g ....')
    s = input('Enter your choice :')

    if s=='p':
        child = input('Enter Child : ')
        parent = _find_parent(child)
        print("Here is your parent :\n",parent)
    elif s=='g':
        child = input('Enter Child : ')
        parent = _find_grandParent(child)
        print("Here is your grand-parent :\n",parent)
    else:
        print('You press worng key')