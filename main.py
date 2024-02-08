from printree import printree
from avl_template import AVLTree, AVLNode

LL = [6,7,8]
RL = [6,8,7]
LR = [8,6,7]
RR = [8,7,6]

t = AVLTree()

for x in RL:
    t.insert(x,0)
    printree(t.root)



#to_insert = [6,8,7]



