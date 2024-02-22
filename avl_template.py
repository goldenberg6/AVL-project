# username - goldenberg6
# id1      - 322658782
# name1    - Noa Goldenberg
# id2      - 207919283
# name2    - Ilana Kolody

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
        """
        Time Complexity - O(1)
        """
        if not self.left.is_real_node:
            return None
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        """
        Time Complexity - O(1)
        """
        if not self.right.is_real_node:
            return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        """
        Time Complexity - O(1)
        """
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        """
        Time Complexity - O(1)
        """
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        """
        Time Complexity - O(1)
        """
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        """
        Time Complexity - O(1)
        """
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        """
        Time Complexity - O(1)
        """
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        """
        Time Complexity - O(1)
        """
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        """
        Time Complexity - O(1)
        """
        self.parent = node

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        """
        Time Complexity - O(1)
        """
        self.key = key

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        """
        Time Complexity - O(1)
        """
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        """
        Time Complexity - O(1)
        """
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        """
        Time Complexity - O(1)
        """
        return self.key is not None

    def calc_bf(self):
        """
        Time Complexity - O(1)
        """
        return self.left.height - self.right.height

    @staticmethod
    def create_leaf(key, value, parent):
        """
        Creates and returns a node with the given key and value, and attaches 2 virtual nodes as left and right children,
        and sets the parent to the given parent.
        Time Complexity: O(1)
        """
        leaf = AVLNode(key, value)
        leaf.set_parent(parent)
        leaf.set_right(AVLNode(None, None))
        leaf.get_right().set_parent(leaf)
        leaf.set_left(AVLNode(None, None))
        leaf.get_left().set_parent(leaf)
        leaf.set_height(0)
        return leaf

    def create_subtree(self):
        """
        Create and return a subtree where the root is self
        Time Complexity: O(1) - All operations are of O(1)
        """
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


    def get_size(self):
        """
        Time Complexity - O(1)
        """
        return self.size

    def set_size(self, x):
        """
        Time Complexity - O(1)
        """
        self.size = x

    def set_root(self, node: AVLNode):
        """
        Time Complexity - O(1)
        """
        self.root = node

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        """
        Search for node with given key using BST search.
        Time complexity : O(logn) - n is the number of nodes in the tree.
        """
        current = self.root
        while current and current.is_real_node():
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
        """
        Insert a node with given key, val using BST insert. And then, rotate as necessary.
        Time complexity : O(logn) - n is the number of nodes in the tree.
        """
        self.size += 1
        rotations = 0
        # if tree is empty - insert new sentinel node as root (#1)
        if self.root is None or not self.root.is_real_node():
            self.root = AVLNode.create_leaf(key, val, None)
            self.root.set_height(0)
            return rotations

        # insert according to BST characteristics (#1)
        parent = self.root
        current = self.root
        while current.is_real_node():
            parent = current
            if key < current.key:
                current = current.get_left()
            else:
                current = current.get_right()
        leaf = AVLNode.create_leaf(key, val, parent)
        if parent.key < key:
            parent.set_right(leaf)
        else:
            parent.set_left(leaf)

        if parent.get_key() == self.root.get_key():  # if inserted node is direct child of root - update heights
            parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
            rotations += 1
            return rotations

        current_height = 1
        child = parent
        while parent is not None:  # 3
            prev_bf = parent.calc_bf()  # 3.1
            height_changed = parent.height != current_height
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
                break

        return rotations

    def rotate(self, grand: AVLNode, is_left_child: bool):
        """
        Determine which rotate is needed (RR/RL/LL/LR) and do it. Return "cost" of rotation(s)
        Time complexity : O(logn) - n is the number of nodes in the tree.
        """
        prev = grand.get_left() if is_left_child else grand.get_right()
        prev_bf = prev.calc_bf()
        grand_bf = grand.calc_bf()
        if grand_bf == 2:
            if prev_bf == -1:
                heights_changed_flag = self.LR_rotate(grand)
                return 2, heights_changed_flag
            if prev_bf == 1 or prev_bf == 0:
                heights_changed_flag = self.RR_rotate(grand)
                return 1, heights_changed_flag
        if grand_bf == -2:
            if prev_bf == 1:
                heights_changed_flag = self.RL_rotate(grand)
                return 2, heights_changed_flag
            if prev_bf == -1 or prev_bf == 0:
                heights_changed_flag = self.LL_rotate(grand)
                return 1, heights_changed_flag

    def LL_rotate(self, node: AVLNode):
        """
        Left rotation
        Time Complexity - O(1)
        """
        sentinel = AVLNode(None, None)
        is_root = False
        # if node is root - create and use sentinel
        if node.parent is None:  # is root
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)

        if is_root is False:  # determine if to set as left or right child
            if node.get_key() < node.get_parent().get_key():
                node.get_parent().set_left(node.get_right())
            else:
                node.get_parent().set_right(node.get_right())
        else:
            node.get_parent().set_right(node.get_right())

        # pointer changes according to LL rotate
        node.get_right().set_parent(node.get_parent())
        temp = node.get_right().get_left()
        node.set_parent(node.get_right())
        node.get_parent().set_left(node)
        node.set_right(temp)
        temp.set_parent(node)

        if is_root:  # if a sentinel was used, detach it
            self.root = sentinel.get_right()
            self.root.set_parent(None)
            sentinel.set_right(AVLNode(None, None))

        self.update_height_locally(node)
        self.update_height_locally(node.parent)

        height_changed = node.calc_bf() != node.get_parent().calc_bf  # edge case - if the height of the physical node
        # changed because of a deletion but the new height is coincidentally the height of the replacing node
        return height_changed

    def RL_rotate(self, node: AVLNode):
        """
        Right then left rotation
        Time Complexity - O(1)
        """
        sentinel = AVLNode(None, None)
        is_root = False
        # if node is root - use sentinel
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
        node.get_right().set_parent(node)

        if is_root:  # if a sentinel was used, detach it
            self.root = sentinel.get_right()
            self.root.set_parent(None)
            sentinel.set_right(AVLNode(None, None))

        self.update_height_locally(node.right.right)
        self.update_height_locally(node.right)
        return self.LL_rotate(node)

    def RR_rotate(self, node: AVLNode):
        """
        Right rotation
        Time Complexity - O(1)
        """
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
        node.get_parent().set_right(node)
        node.set_left(temp)
        temp.set_parent(node)

        if is_root:  # if a sentinel was used, detach it
            self.root = sentinel.get_left()
            self.root.set_parent(None)
            sentinel.set_left(AVLNode(None, None))

        self.update_height_locally(node)
        self.update_height_locally(node.parent)

        height_changed = node.calc_bf() != node.get_parent().calc_bf  # edge case - if the height of the physical node
        # changed because of a deletion but the new height is coincidentally the height of the replacing node
        return height_changed

    def LR_rotate(self, node: AVLNode):
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

        # grand's height didnt change, only left child and left left child
        self.update_height_locally(node.left.left)
        self.update_height_locally(node.left)

        return self.RR_rotate(node)

    def update_height_locally(self, node: AVLNode):
        """
        set height of nade based on left and right children
        Time Complexity - O(1)
        """
        node.set_height(max(node.get_left().get_height(), node.get_right().get_height()) + 1)

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node: AVLNode):
        """
        Delete node from tree and rebalance after deletion
        Time complexity : O(logn) - n is the number of nodes in the tree
        """
        if node is None:
            return 0
        pdp: AVLNode = self.BST_delete(node)  # pdp stands for Physically Deleted Parent
        self.size -= 1
        rotations = 0
        if pdp is None:  # physically deleted node was root
            return rotations
        rotations = self.rebalance(pdp)
        return rotations

    def BST_delete(self, node: AVLNode):
        """
        Physically delete node from tree and return the parent of the physically deleted node
        Time Complexity - O(logn) - n is the number of nodes is the tree
        """
        is_left_child = node.get_key() < node.get_parent().get_key() if (node.get_parent() is not None
                                                                         and node.get_parent().is_real_node()) else False

        sentinel = AVLNode(None, None)
        is_root = False

        if not node.left.is_real_node() and not node.right.is_real_node():  # is leaf
            # turn it into virtual child
            node.key = None
            node.value = None
            node.height = -1
            node.left = None
            node.right = None
            return node.parent

        if node.get_parent() is None:  # if node is to be deleted, create sentinel
            is_root = True
            sentinel.set_right(node)
            sentinel.set_left(AVLNode(None, None))
            node.set_parent(sentinel)
        parent = node.parent

        # has right child
        if not node.left.is_real_node():
            if is_root:  # is root
                node.right.parent = node.parent
                self.root = node.right
                sentinel.right = node.right
            else:  # not root
                node.get_parent().set_left(node.get_right()) if is_left_child else node.get_parent().set_right(
                    node.get_right())
                node.get_right().set_parent(node.get_parent())
            if is_root:  # remove sentinel if needed
                self.root = sentinel.get_right()
                self.root.set_parent(None)
                sentinel.set_right(AVLNode(None, None))

        # has left child
        elif not node.right.is_real_node():
            if is_root:  # is root
                node.left.parent = node.parent
                self.root = node.left
                sentinel.right = node.left
            else:  # not root
                node.get_parent().set_left(node.get_left()) if is_left_child else node.get_parent().set_right(
                    node.get_left())
                node.get_left().set_parent(node.get_parent())
            if is_root:  # remove sentinel if needed
                self.root = sentinel.get_right()
                self.root.set_parent(None)
                sentinel.set_right(AVLNode(None, None))

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
            node.get_parent().set_left(successor) if is_left_child else parent.set_right(successor)
            node.set_parent(None)

            if is_root:  # remove sentinel if needed
                self.root = sentinel.get_right()
                self.root.set_parent(None)
                sentinel.set_right(AVLNode(None, None))

            return successor_parent if not adjacent_successor else successor

        return parent

    def rebalance(self, pdp: AVLNode):
        """
        Updates height of nodes from pdp to root and apply rotations if needed. Based on the psuedo-code we saw in class
        Time Complexity: O(logn) when is the number of nodes in the tree
        """
        current_height = max(pdp.get_left().get_height(), pdp.get_right().get_height()) + 1
        height_changed_flag = False
        rotations = 0
        while pdp:
            pdp_bf = pdp.calc_bf()
            height_changed = pdp.height != current_height or height_changed_flag
            if abs(pdp_bf) < 2 and not height_changed:  # 3.2
                return rotations
            elif abs(pdp_bf) < 2 and height_changed:  # 3.3
                pdp.set_height(current_height)
                rotations += 1  # height change that isnt caused by a rotation
                pdp = pdp.get_parent()
                # current_height += 1
                if pdp: current_height = max(pdp.get_left().get_height(), pdp.get_right().get_height()) + 1
                continue
            else:  # (BF=2) 3.4
                is_left = pdp_bf == 2
                add_rotations, height_changed_flag = self.rotate(pdp, is_left)
                rotations += add_rotations
                pdp = pdp.get_parent()
                current_height = max(pdp.get_left().get_height(), pdp.get_right().get_height()) + 1
        return rotations

    def successor(self, node: AVLNode):
        """
        Return successor to pointer of node
        Time Complexity - O(logn) when n is the number of nodes in tree
        """
        if node.get_right().is_real_node():
            return self.min_node(node.get_right())
        current: AVLNode = node.get_parent()
        while current.is_real_node() and node == current.get_right():
            node = current
            current = current.get_parent()
        return current

    def min_node(self, node: AVLNode):
        """
        Return a pointer to the node with the minimal key
        Time Complexity - O(logn) when n is the number of nodes
        """
        while node.get_left().is_real_node():
            node = node.get_left()
        return node

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        """
        Wrapper function of avl_to_array_rec
        Returns an array of the (key,value) pairs s in sorted order by key
        Time Complexity - O(n)
        """
        array = []
        self.avl_to_array_rec(self.get_root(), array)
        return array

    def avl_to_array_rec(self, node, array):
        """
        Returns an array of the (key,value) pairs s in sorted order by key
        Time Complexity - O(n)
        """
        if node and node.is_real_node():
            self.avl_to_array_rec(node.get_left(), array)
            array.append((node.get_key(), node.get_value()))
            self.avl_to_array_rec(node.get_right(), array)

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        """
        Time Complexity - O(1)
        """
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

    def split(self, node):
        """
        Splits the tree into 2 trees while using join as seen in class.
        Time Complexity - O(logn)
        """
        if node is None:
            return [AVLTree(), AVLTree()]
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
        """
        Joins self and tree2 using a new node with the key,value arguments.
        Time Complexity - O(logn)
        """
        # if both trees are empty
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
            height_diff = abs(t1.get_root().get_height() - t2.get_root().get_height())

            if height_diff <= 1:  # join the trees as is (with new node as root)
                new_node = self.connect_nodes(t1.get_root(), t2.get_root(), key, val)
                self.root = new_node

            # join if left is taller (t1)
            elif t1.root.get_height() > t2.get_root().get_height():
                current = t1.get_root()
                # search for subtree with same height as t2
                while current.get_height() > t2.root.get_height():
                    current = current.get_right()
                prev = current.get_parent()

                # create node (x from presentation) and connect it to the trees
                node = self.connect_nodes(current, t2.get_root(), key, val)
                node.set_parent(prev)
                prev.set_right(node)
                self.root = t1.root

                # rebalance from x.parent to node ( #nodes in path <= log(n) )
                self.rebalance(node.parent)
                self.size = t1.size + 1

            # join if right is taller (t2)
            else:
                current = t2.get_root()
                # search for subtree with same height as t1
                while current.get_height() > t1.root.get_height():
                    current = current.get_left()
                prev = current.get_parent()
                # create x (from presentation) and connect it to the trees
                node = self.connect_nodes(t1.get_root(), current, key, val)
                node.set_parent(prev)
                prev.set_left(node)
                self.root = t2.root

                # rebalance from x.parent to node ( #nodes in path <= log(n) )
                self.rebalance(node.parent)
                self.size = t2.size + 1
        return height_diff + 1

    def connect_nodes(self, left, right, key, val):
        """
        Returns a new AVLNode with key and val as key and value, and left as left child and right as right child
        Time Complexity - O(1)
        """
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
        """
        Time Complexity - O(1)
        """
        return self.root
