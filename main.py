from printree import printree
from avl_template import AVLTree, AVLNode

LL = [6,7,8]
RL = [6,8,7]
LR = [8,6,7]
RR = [8,7,6]

bigtree_with_LR = [15,10,22,4,11,20,24,2,7,12,18,1,6,8,5]

t = AVLTree()

for x in bigtree_with_LR:
    t.insert(x,0)
    printree(t.root)

print(t.avl_to_array())




#to_insert = [6,8,7]



