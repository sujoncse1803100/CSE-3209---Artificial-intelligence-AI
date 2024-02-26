
# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))

# def gcd(x,y):
#     if y==0:
#         return x
#     else:
#         return gcd(y,x%y)
    
# print(gcd(100,70))


# str=input("Enter your string : ")
# arr=str.split(" ")
# i=len(arr)-1
# while i>=0:
#     print(arr[i],end=" ")
#     i-=1


# import math
# if 10>math.inf:
#     print("not working")
# else:
#     print("working")

# myDict = {'a': 10, 'a': 9,
#         'b': 15, 'c': 2, 'd': 32}

# def sorting():
#     keys=list(myDict.keys())
#     keys.sort()
#     s_d = {i:myDict[i] for i in keys}
#     return s_d
    
# tree = sorting()
 
# print(tree)

tree = {
    "X":[{"A":5},{"B":7}],
}

print(len(tree["X"]))

# for x in tree["X"]:
#     key=list(x.keys())[0]
#     print(key)
#     print(x[key])


# frontier=[
#     {"node":"S","weight":5,"parent":"","visited":False},
#     {"node":"A","weight":2,"parent":"","visited":False},
# ]
# def sorting(e):
#   return e['weight']
# frontier.sort(key=sorting)
# print(frontier)
