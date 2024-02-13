from printree import printree
from avl_template import AVLTree, AVLNode

LL = [6,7,8]
RL = [6,8,7]
LR = [8,6,7]
RR = [8,7,6]

bigtree_with_LR = [15,10,22,4,11,20,24,2,7,12,18,1,6,8,5]

bigtree_with_RL = [20,10,30,35,34,45] #45,34,46,33

bigtree_with_RR = [12,8,15,6,10,14,24,11,13,20,29,19,18]

bigtree_with_LR2 = [15, 10, 25, 4, 11, 20, 26, 2, 18, 23, 27, 17, 22, 24, 21]

test = [7,2,8,1,5,10,6,9,4]

t = AVLTree()

for x in bigtree_with_RR:
    # print("ROTATIONS:   ", t.insert(x,0))
    t.insert(x,0)
    printree(t.root)

# t.delete(t.search(2))
printree(t.root)

# print(t.avl_to_array())




#to_insert = [6,8,7]



