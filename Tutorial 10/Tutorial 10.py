# Data Structures & Algorithms
# Tutorial 10: AVL Tree
# Name: TODO Write your name here
# NPM: TODO Write your NPM here


def main():
    tree = AVLTree()
    for value in (8,2,12,1,5,10,14,3,9,11,4):
        tree.insert(value)
    tree.print()


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(Node: {})".format(self.value)

    def insert(self, node, current):
        # TODO: Implement Me!
        value = node.value

        # Current node is None, replace None with node
        # to be inserted.
        if current is None:
            pass

        # The value to be inserted is less than the current
        # node's value. The node is recursively inserted
        # to the current node's left children.
        elif value < current.value:
            pass

            # If the current node's balance factor is greater
            # than 1, then it is left-heavy. Perform the
            # appropriate rotations.
            # Ex: current = current.rotate_right_left()
            if current.balance() > 1:
                if current.left.value > value:
                    pass
                else:
                    pass

        # The value to be inserted is greater than the current
        # node's value. The node is recursively inserted
        # to the current node's right children.
        elif value > current.value:
            pass

            # If the current node's balance factor is less
            # than 1, then it is right-heavy. Perform the
            # appropriate rotations.
            # Ex: current = current.rotate_right_left()
            if current.balance() < -1:
                if current.right.value < value:
                    pass
                else:
                    pass
        else:
            raise ValueError("Cannot insert duplicate values")

        return current
            
    def balance(self):
        # TODO: Implement Me!
        # Return the balance factor of a node, which is the
        # height of its left subtree subtracted by the height
        # of its right subtree.
        pass
        
    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left and not self.right:
            return 1 + self.left.height()
        elif self.right and not self.left:
            return 1 + self.right.height()
        else:
            return -1

    def rotate_right(self):
        # TODO: Implement Me!
        # Case 1, rotate self with left child. Returns new root.
        pass
        return new

    def rotate_left(self):
        # TODO: Implement Me!
        # Case 4, rotate self with right child. Returns new root.
        pass
        return new

    def rotate_left_right(self):
        # TODO: Implement Me!
        # Case 2, rotate self.left with its right child, then
        # rotate the new self.left with self. Returns new root.
        pass
        return root.rotate_right()

    def rotate_right_left(self):
        # TODO: Implement Me!
        # Case 3, rotate self.right with its left child, then
        # rotate the new self.right with self. Returns new root.
        pass
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
        
