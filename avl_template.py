# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info
from printree import printree

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.parent = None
        self.height = -1

        # TODO delete this?
        # virtual nodes
        if key and value:
            self.left = AVLNode(None, None)
            self.right = AVLNode(None, None)

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        if not self.left.is_real_node:
            return None
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        if not self.right.is_real_node:
            return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.key is not None

    def calc_bf(self):
        return self.left.height - self.right.height

    @staticmethod
    def create_leaf(key, value, parent):
        leaf = AVLNode(key, value)
        leaf.set_parent(parent)
        leaf.set_right(AVLNode(None, None))
        leaf.get_right().set_parent(leaf)
        leaf.set_left(AVLNode(None, None))
        leaf.get_left().set_parent(leaf)
        leaf.set_height(0)
        return leaf

    def create_subtree(self):
        tree = AVLTree()
        tree.root = self
        self.parent = None
        return tree


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root: AVLNode = None
        self.size: int = 0

    # add your fields here

    def get_size(self):
        return self.size

    def set_size(self, x):
        self.size = x

    def set_root(self, node: AVLNode):
        self.root = node

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        current = self.root
        while current.is_real_node():
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        self.size += 1
        rotations = 0
        # if tree is empty - insert new sentinel node as root (#1)
        if self.root is None or not self.root.is_real_node():
            self.root = AVLNode.create_leaf(key, val, None)
            self.root.set_height(0)
            # rotations += 1 TODO ask in forum
            return rotations

        # insert according to BST characteristics (#1)
        parent = self.root
        current = self.root
        while current.is_real_node():
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        leaf = AVLNode.create_leaf(key, val, parent)
        if parent.key < key:
            parent.set_right(leaf)
        else:
            parent.set_left(leaf)

        if parent.get_key() == self.root.get_key():
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
            rotations += 1
            return rotations

        current_height = 1
        child = parent
        while parent is not None:  # (#3)
            prev_bf = parent.calc_bf()  # 3.1
            height_changed = parent.height != current_height
            # prev.height hasnt been changed yet
            if abs(prev_bf) < 2 and not height_changed:  # 3.2
                break
            elif abs(prev_bf) < 2 and height_changed:  # 3.3
                parent.set_height(parent.get_height() + 1)
                child = parent
                parent = parent.get_parent()
                current_height += 1
                continue
            else:  # (BF=2) 3.4
                is_left = prev_bf == 2
                rotations = self.rotate(child.get_parent(), is_left)
                # maintain height on path to leaf
                break

        return rotations

    def rotate(self, grand: AVLNode, is_left_child: bool):
        node_to_update = None
        # determine which rotate is need (RR/RL/LL/LR) and do it
        # grand = prev.get_parent()
        prev = grand.get_left() if is_left_child else grand.get_right()
        prev_bf = prev.calc_bf()
        grand_bf = grand.calc_bf()
        if grand_bf == 2:
            if prev_bf == -1:
                self.LR_rotate(grand)
                return 2
            if prev_bf == 1 or prev_bf == 0:
                heights_changed_flag = self.RR_rotate(grand)
                return 1, heights_changed_flag
        if grand_bf == -2:
            if prev_bf == 1:
                self.RL_rotate(grand)
                return 2
            if prev_bf == -1 or prev_bf == 0:
                heights_changed_flag = self.LL_rotate(grand)
                return 1, heights_changed_flag

        # return node_to_update

    def update(self, node: AVLNode):
        print("UPDATE")
        # maintaining height until reach a node which doesnt need updating
        if node is None:
            return
        correct_height = max(node.get_left().get_height(), node.get_right().get_height()) + 1
        while node is not None and node.height != correct_height:
            node.set_height(correct_height)
            node = node.get_parent()
            correct_height += 1
            # correct_height = max(node.get_left().get_height(), node.get_left().get_height()) + 1

    def LL_rotate(self, node: AVLNode):
        print("LL_ROTATE")
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)

        if is_root is False:
            if (node.get_key() < node.get_parent().get_key()):
                node.get_parent().set_left(node.get_right())
            else:
                node.get_parent().set_right(node.get_right())
        else:
            node.get_parent().set_right(node.get_right())

        node.get_right().set_parent(node.get_parent())
        temp = node.get_right().get_left()
        node.set_parent(node.get_right())
        node.right = AVLNode(None, None)
        node.get_parent().set_left(node)
        node.set_right(temp)
        temp = None

        if is_root:  # is root
            self.root = sentinel.get_right()
            self.root.set_parent(None)
            sentinel.set_right(AVLNode(None, None))

        # the only height that changes is node.left's
        # node.set_height(node.get_parent().get_height() - 1)

        self.update_height_locally(node)
        self.update(node.get_parent().get_parent())
        height_changed = node.calc_bf() != node.get_parent().calc_bf  # edge case - if the height of the physical node
        # changed because of a deletion but the new height is coincidentally the height of the replacing node
        return height_changed

    def RL_rotate(self, node: AVLNode):
        print("RL_ROTATE")
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)

        node.set_right(node.get_right().get_left())
        temp = node.get_right().get_right() if node.get_right().get_right() is not None else AVLNode(None, None)
        node.get_right().set_right(node.get_right().get_parent())
        node.get_right().get_right().set_left(temp)
        temp.set_parent(node.get_right().get_right())
        node.get_right().get_right().set_parent(node.get_right())
        temp = None
        node.get_right().set_parent(node)

        if is_root:  # is root
            self.root = sentinel.get_right()
            self.root.set_parent(None)
            sentinel.set_right(AVLNode(None, None))

        self.update(node.get_right().get_right())  # here
        return self.LL_rotate(node)

    def RR_rotate(self, node: AVLNode):
        print("RR_ROTATE")
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_left(node)
            sentinel.set_right(AVLNode(None, None))
            node.set_parent(sentinel)

        if is_root is False:
            if node.get_key() < node.get_parent().get_key():
                node.get_parent().set_left(node.get_left())
            else:
                node.get_parent().set_right(node.get_left())
        else:
            node.get_parent().set_left(node.get_left())

        node.get_left().set_parent(node.get_parent())
        temp = node.get_left().get_right()
        node.set_parent(node.get_left())
        node.left = AVLNode(None, None)
        node.get_parent().set_right(node)
        node.set_left(temp)

        if is_root:  # is root
            self.root = sentinel.get_left()
            self.root.set_parent(None)
            sentinel.set_left(AVLNode(None, None))

        self.update_height_locally(node)
        self.update(node.get_parent())  # .get_parent()
        height_changed = node.calc_bf() != node.get_parent().calc_bf  # edge case - if the height of the physical node
        # changed because of a deletion but the new height is coincidentally the height of the replacing node
        return height_changed

    def update_height_locally(self, node: AVLNode):
        node.set_height(max(node.get_left().get_height(), node.get_right().get_height()) + 1)

    def LR_rotate(self, node: AVLNode):
        print("LR ROTATE")
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_left(node)
            sentinel.set_right(AVLNode(None, None))
            node.set_parent(sentinel)

        node.set_left(node.get_left().get_right())
        temp = node.get_left().get_left() if node.get_left().get_left() is not None else AVLNode(None, None)
        node.get_left().set_left(node.get_left().get_parent())
        node.get_left().get_left().set_right(temp)
        temp.set_parent(node.get_left().get_left())
        node.get_left().get_left().set_parent(node.get_left())
        node.get_left().set_parent(node)

        if is_root:  # is root
            self.root = sentinel.get_left()
            self.root.set_parent(None)
            sentinel.set_left(AVLNode(None, None))

        self.update(node.get_left().get_left())  # here
        return self.RR_rotate(node)

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node: AVLNode):
        if node is None:
            return 0
        pdp: AVLNode = self.BST_delete(node)  # pdp stands for Physically Deleted Parent
        rotations = 0
        if pdp is None:  # physically deleted node was root
            return rotations
        current_height = max(pdp.get_left().get_height(), pdp.get_right().get_height()) + 1
        height_changed_flag = False
        while pdp:
            pdp_bf = pdp.calc_bf()
            height_changed = pdp.height != current_height or height_changed_flag
            if abs(pdp_bf) < 2 and not height_changed:  # 3.2
                return rotations
            elif abs(pdp_bf) < 2 and height_changed:  # 3.3
                pdp.set_height(current_height)
                rotations += 1  # height change that isnt caused by a rotation
                pdp = pdp.get_parent()
                current_height += 1
                continue
            else:  # (BF=2) 3.4
                is_left = pdp_bf == 2
                add_rotations, height_changed_flag = self.rotate(pdp, is_left)
                rotations += add_rotations
                pdp = pdp.get_parent()
                current_height = max(pdp.get_left().get_height(), pdp.get_right().get_height()) + 1
        return rotations

    def BST_delete(self, node: AVLNode):
        if self.get_size() == 1:  # is only node
            self.root = None
            return None
        elif self.get_size() <= 3 and node == self.root:  # tree has 2 or 3 nodes and delete root
            if not node.get_left().is_real_node():  # root and right node
                self.root = node.get_right()
                self.root.set_parent(None)
            elif not node.get_right().is_real_node():  # root and left node
                self.root = node.get_left()
                self.root.set_parent(None)
            else:  # root and left and right
                temp = node.get_left()
                self.root = node.get_right()
                self.root.set_parent(None)  # to sentinel HERE
                self.root.set_left(temp)
                temp.set_parent(self.root)
            return None

        sentinel = AVLNode(None, None)
        is_root = False
        if node.get_parent() is None:  # if node is to be deleted, create sentinel
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)

        is_left_child = node.get_key() < node.get_parent().get_key() if (node.get_parent() is not None and
                                                                         node.get_parent().is_real_node()) else False
        virtual_node = AVLNode(None, None)
        temp = node.get_parent()
        if not node.get_right().is_real_node() and not node.get_left().is_real_node():  # is leaf
            node.get_parent().set_left(virtual_node) if is_left_child else node.parent.set_right(virtual_node)
            node.set_parent(None)
            return temp
        elif not node.get_right().is_real_node():  # has only left child
            node.get_parent().set_left(node.get_left()) if is_left_child else node.get_parent().set_right(
                node.get_left())
            node.get_left().set_parent(node.get_parent())
            return temp
        elif not node.get_left().is_real_node():  # has only right child
            node.get_parent().set_left(node.get_right()) if is_left_child else node.get_parent().set_right(
                node.get_right())
            node.get_left().set_parent(node.get_parent())
            return temp

        else:  # has 2 children
            adjacent_successor = True
            successor = self.successor(node)
            successor.set_height(node.get_height())
            successor_parent = successor.get_parent()
            # remove successor from tree
            successor_child = successor.get_right()
            if successor.get_parent().get_key() != node.get_key():
                adjacent_successor = False
                successor.get_parent().set_left(successor_child)
            successor_child.set_parent(successor.get_parent())

            # replace node by successor
            successor.set_parent(node.get_parent())
            successor.set_left(node.get_left())
            if not adjacent_successor:
                successor.set_right(node.get_right())
            successor.get_left().set_parent(successor)
            successor.get_right().set_parent(successor)
            node.get_parent().set_left(successor) if is_left_child else node.get_parent().set_right(successor)
            node.set_parent(None)

        if is_root:  # remove sentinel if needed
            self.root = sentinel.get_right()
            self.root.set_parent(None)
            sentinel.set_right(AVLNode(None, None))

        return successor_parent if not adjacent_successor else successor

    def successor(self, node: AVLNode):
        if node.get_right().is_real_node():
            return self.min_node(node.get_right())
        current: AVLNode = node.get_parent()
        while current.is_real_node() and node == current.get_right():
            node = current
            current = current.get_parent()
        return current

    def min_node(self, node: AVLNode):
        while node.get_left().is_real_node():
            node = node.get_left()
        return node

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        array: list = []
        self.avl_to_array_rec(self.root, array)
        return array

    def avl_to_array_rec(self, node: AVLNode, array: list):
        if node.is_real_node():
            self.avl_to_array_rec(node.get_left(), array)
            array.append((node.key, node.value))
            self.avl_to_array_rec(node.get_right(), array)

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.size

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    # size field doesn't have to be correct after split()
    def split(self, node):
        t1 = node.left.create_subtree()
        t2 = node.right.create_subtree()
        while node.parent is not None:
            parent = node.parent
            if parent.key < node.key:
                t1.join(parent.left.create_subtree(), parent.key, parent.value)
            else:
                t2.join(parent.right.create_subtree(), parent.key, parent.value)
            node = parent

        return [t1, t2]

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):
        # if tree is empty
        if (self.root is None or not self.root.is_real_node()) and (
                tree2.get_root() is None or not tree2.get_root().is_real_node()):
            height_diff = 1
            self.insert(key, val)
        # if self tree is empty
        elif self.root is None or not self.root.is_real_node():
            height_diff = tree2.get_root().get_height() + 2  # because other tree height is -1
            tree2.insert(key, val)
            self.root = tree2.get_root()
        # if tree2 is empty
        elif tree2.get_root() is None or not tree2.get_root().is_real_node():
            height_diff = self.get_root().get_height() + 2
            self.insert(key, val)
        else:  # both trees are not empty
            # determine which tree is bigger (t2) and smaller (t1)
            if self.root.key > key:
                t1 = tree2
                t2 = self
            else:
                t1 = self
                t2 = tree2
            height_diff = abs(t1.get_root().get_height() - t2.get_root().get_height()) + 1

            if height_diff <= 1:  # join the trees as is (with new node as root)
                new_node = self.connect_nodes(t1.get_root(), t2.get_root(), key, val)
                self.root = new_node

            elif t1.root.get_height() > t2.get_root().get_height():  # join if left is taller (t1)
                current = t1.get_root()
                # search for subtree with same height as t2
                while current.get_height() > t2.root.get_height():
                    current = current.get_right()
                prev = current.get_parent()
                # create x (from presentation) and connect it to the trees
                node = self.connect_nodes(current, t2.get_root(), key, val)
                self.update_height_locally(node)
                node.set_parent(prev)
                prev.set_right(node)
                # rebalance from x.parent to node ( #nodes in path <= log(n) )
                current = node.parent
                while current.get_parent():
                    # self.update_height_locally(current)
                    self.rotate(current, True)
                    current = current.get_parent()
                    self.update_height_locally(current)
                self.root = t1.get_root()
            else:  # join if right is taller (t2)
                current = t2.get_root()
                # search for subtree with same height as t1
                while current.get_height() > t1.root.get_height():
                    current = current.get_left()
                prev = current.get_parent()
                # create x (from presentation) and connect it to the trees
                node = self.connect_nodes(t1.get_root(), current, key, val)
                # self.update_height_locally(node)
                node.set_parent(prev)
                prev.set_left(node)
                # rebalance from x.parent to node ( #nodes in path <= log(n) )
                current = node.parent
                while current.get_parent():
                    # self.update_height_locally(current)
                    self.rotate(current, True)  # false???
                    current = current.get_parent()
                    self.update_height_locally(current)
                self.root = t2.get_root()
        return height_diff

    def connect_nodes(self, left, right, key, val):
        node = AVLNode(key, val)
        node.set_left(left)
        node.set_right(right)
        left.set_parent(node)
        right.set_parent(node)
        self.update_height_locally(node)
        return node

    """returns the root of the tree representing the dictionary
    
    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root
