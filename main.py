from printree import printree
from avl_template import AVLTree, AVLNode

t = AVLTree()
to_insert = [10,6,12,13,14]
for x in to_insert:
    t.insert(x,0)
printree(t.root)
t.LL_rotate(t.root.get_right())
printree(t.root)
t.insert(7,0)
printree(t.root)

