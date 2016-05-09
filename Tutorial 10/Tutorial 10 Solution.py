# Data Structures & Algorithms
# Tutorial 10: AVL Tree
# Name: TODO Write your name here
# NPM: TODO Write your NPM here


def main():
    # Initialize tree
    def init_tree():
        tree = AVLTree()
        values = []
        for value in values:
            tree.insert(value)
        return tree

    tree = init_tree
    tree.print()


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(Node: {})".format(self.value)

    def insert(self, node, current):
        value = node.value
        if current is None:
            current = node
        
        elif value < current.value:
            current.left = self.insert(node, current.left)
            if current.balance() > 1:
                if current.left.value > value:
                    current = current.rotate_right()
                else:
                    current = current.rotate_left_right()
                    
        elif value > current.value:
            current.right = self.insert(node, current.right)
            if current.balance() < -1:
                if current.right.value < value:
                    current = current.rotate_left()
                else:
                    current = current.rotate_right_left()
        else:
            raise ValueError("Cannot insert duplicate values")

        return current
            
    def balance(self):
        return (self.left.height() if self.left else 0) - \
               (self.right.height() if self.right else 0)
        
    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left and not self.right:
            return 1 + self.left.height()
        elif self.right and not self.left:
            return 1 + self.right.height()
        else:
            return -1

    def rotate_left(self):
        print("{} rotate left..".format(str(self)))
        root = self
        new = root.right
        root.right = new.left
        new.left = root
        return new

    def rotate_right(self):
        print("{} rotate right..".format(str(self)))
        root = self
        new = root.left
        root.left = new.right
        new.right = root
        return new

    def rotate_left_right(self):
        print("lr")
        root = self
        root.left = root.left.rotate_left()
        return root.rotate_right()

    def rotate_right_left(self):
        print("rl")
        root = self
        root.right = root.right.rotate_right()
        return root.rotate_left()

    def print(self, depth=0, child=""):
        space = "    |   " * (depth - 1) if depth > 0 else ""
        line = "    |___" if depth > 0 else ""
        ret = space + line + child + str(self) + "\n"
        if self.left is not None:
            ret += self.left.print(depth + 1, "[L]")
        if self.right is not None:
            ret += self.right.print(depth + 1, "[R]")
        return ret

    def in_order_bal(self):
        if self.left:
            self.left.in_order_bal()
        print(str(self), self.balance)
        if self.right:
            self.right.in_order_bal()


class AVLTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(Node(value), self.root)

    def print(self):
        print(self.root.print())
        
        
tree = AVLTree()
for value in (8,2,12,1,5,10,14,3,9,11,4):
    tree.insert(value)
tree.print()

##tree = AVLTree()
##h = Node('h')
##j = Node('j')
##i = Node('i')
##l = Node('l')
##tree.root = h
##h.right, l.parent = l, h
##l.left, j.parent = j, l
##j.left, i.parent = i, j
##h.balance = -3
##l.balance = 2
##j.balance = 1
##i.balance = 0
##tree.print()
