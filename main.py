from printree import printree
from avl_template import AVLTree, AVLNode

LL = [6, 7, 8]
RL = [6, 8, 7]
LR = [8, 6, 7]
RR = [8, 7, 6]

bigtree_with_LR = [15, 10, 22, 4, 11, 20, 24, 2, 7, 12, 18, 1, 6, 8, 5]

bigtree_with_RL = [20, 10, 30, 35, 34, 45]  # 45,34,46,33

bigtree_with_RR = [12, 8, 15, 6, 10, 14, 24, 11, 13, 20, 29, 19, 18]

bigtree_with_LR2 = [15, 10, 25, 4, 11, 20, 26, 2, 18, 23, 27, 17, 22, 24, 21]

test = [7, 2, 8, 1, 5, 10, 6, 9, 4]

test2 = [10, 6, 20, 4, 8, 15, 40, 2, 5, 11, 30, 43, 25, 35]

test3_delete_edge_case = [13, 8, 18, 5, 11, 16, 20, 3, 7, 10, 12, 15, 17, 19, 2, 4, 6, 9, 14, 1]
test3_symmetric = [-13, -8, -18, -5, -11, -16, -20, -3, -7, -10, -12, -15, -17, -19, -2, -4, -6, -9, -14,
                   -1]  # add 30 in for loop!!

t4 = [2887,2559,6815, 2780]


t1 = AVLTree()
for x in t4:
    t1.insert(x, 0)
printree(t1.root)

t1.delete(t1.search(2559))
printree(t1.root)

# t1 = AVLTree()

# for x in [2,1,3]:
#     # print("ROTATIONS:   ", t.insert(x,0))
#     t1.insert(x,0)
#     # printree(t.root)
# print("T1--------")
# printree(t1.root)
#
#
# t2 = AVLTree()
# for x in [20,10,30,8,16,25,33,6,9,13,18,27,32,5,7]:
#     # print("ROTATIONS:   ", t.insert(x,0))
#     t2.insert(x,0)
# print("T2--------")
# printree(t2.root)
#
# print("HEIGHT DIFF: ", t1.join(t2, 4,0))
# printree(t1.root)
