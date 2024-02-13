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
        leaf.set_left(AVLNode(None, None))
        leaf.set_height(0)
        return leaf


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root: AVLNode = None

    # add your fields here

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
        # if tree is empty - insert new sentinel node as root (#1)
        if self.root is None:
            self.root = AVLNode.create_leaf(key, val, None)
            self.root.set_height(0)
            return

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

        # if the new node is the root's son, no need for height correction or rotations
        if parent.get_key() == self.root.get_key():
            parent.set_height(parent.get_height() + 1)
            return

        current_height = 1
        child = parent
        while parent is not None:  # (#3)
            prev_bf = parent.calc_bf()  # 3.1
            height_changed = parent.height != current_height
            # prev.height hasnt been changed yet
            if abs(prev_bf) < 2 and not height_changed:  # 3.2
                break
            elif abs(prev_bf) <2 and height_changed:  # 3.3
                parent.set_height(parent.get_height() + 1)
                child = parent
                parent = parent.get_parent()
                current_height += 1
                continue
            else:  # (BF=2) 3.4
                printree(self.root)
                node_to_update = self.rotate(child, leaf.get_parent())
                # maintain height on path to leaf
                # self.Update(node_to_update)
                break


    def rotate(self, prev:AVLNode, leaf :AVLNode):
        node_to_update = None
        # determine which rotate is need (RR/RL/LL/LR) and do it
        grand = prev.get_parent()
        if prev.calc_bf() == 1:
            if grand.calc_bf() == 2:
                node_to_update = self.RR_rotate(grand)
            if grand.calc_bf() == -2:
                node_to_update = self.RL_rotate(grand)
        elif prev.calc_bf() == -1:
            if grand.calc_bf() == 2:
                node_to_update = self.LR_rotate(grand,leaf)
            if grand.calc_bf() == -2:
                node_to_update = self.LL_rotate(grand)

        return node_to_update

    def update(self, node: AVLNode):
        # maintaining height
        if node is None:
            return
        current_height = max(node.get_left().get_height(), node.get_left().get_height()) + 1
        while node is not None and current_height != node.height:
            node.set_height(current_height)
            current_height += 1
            node = node.parent

    def LL_rotate(self, node: AVLNode):
        sentinel = AVLNode("sentinal", None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)

        if is_root is False:
            if(node.get_key() < node.get_parent().get_key()):
                node.get_parent().set_left(node.get_right())
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
        node.set_height(node.get_parent().get_height() - 1)

        self.update(node.get_parent().get_parent())

        return node.get_parent()

    def RL_rotate(self, node: AVLNode):
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)

        node.set_right(node.get_right().get_left())
        temp = node.get_right().get_right() if node.get_right().get_right() is not None else AVLNode(None,None)
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

        print("RL rotate:")
        printree(self.root)
        self.update(node.get_right().get_right())  # here
        printree(self.root)
        return self.LL_rotate(node)

        return self.LL_rotate(node)

    def RR_rotate(self, node: AVLNode):
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_left(node)
            sentinel.set_right(AVLNode(None, None))
            node.set_parent(sentinel)

        if is_root is False:
            if(node.get_key() < node.get_parent().get_key()):
                node.get_parent().set_left(node.get_left())
            else:
                node.get_parent().set_right(node.get_left())

        node.get_left().set_parent(node.get_parent())
        temp = node.get_left().get_right()
        node.set_parent(node.get_left())
        node.left = AVLNode(None, None)
        node.get_parent().set_right(node)
        node.set_left(temp)
        temp=None

        if is_root:  # is root
            self.root = sentinel.get_left()
            self.root.set_parent(None)
            sentinel.set_left(AVLNode(None, None))

        # the only height that changes is node.left's
        node.set_height(node.get_parent().get_height() - 1)

        self.update(node.get_parent().get_parent())

        return node.get_parent()

    def LR_rotate(self, node: AVLNode, leaf :AVLNode):
        sentinel = AVLNode(None, None)
        is_root = False
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_left(node)
            sentinel.set_right(AVLNode(None, None))
            node.set_parent(sentinel)

        node.set_left(node.get_left().get_right())
        temp = node.get_left().get_left() if node.get_left().get_left() is not None else AVLNode(None,None)
        node.get_left().set_left(node.get_left().get_parent())
        node.get_left().get_left().set_right(temp)
        temp.set_parent(node.get_left().get_left())
        node.get_left().get_left().set_parent(node.get_left())
        temp = None
        node.get_left().set_parent(node)

        if is_root:  # is root
            self.root = sentinel.get_left()
            self.root.set_parent(None)
            sentinel.set_left(AVLNode(None, None))

        print("LR rotate:")
        printree(self.root)
        self.update(node.get_left().get_left()) #here
        printree(self.root)
        return self.RR_rotate(node)


    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        return -1

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None

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
        return None

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return None
