# Data Structures & Algorithms
# Tutorial 11: AVL Tree
# Name: TODO Write your name here
# NPM: TODO Write your NPM here


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(Node: {})".format(self.value)

    def insert(self, node, current):
        """Inserts an already instantiated node into the tree."""
        value = node.value

        # Current node is None, replace None with node
        # to be inserted.
        if current is None:
            current = node

        # The value to be inserted is less than the current
        # node's value. The node is recursively inserted
        # to the current node's left children.
        elif value < current.value:
            current.left = self.insert(node, current.left)

            # If the current node's balance factor is greater
            # than 1, then it is left-heavy. Perform the
            # appropriate rotations.
            # Ex: current = current.rotate_right_left()
            if current.balance() > 1:
                if current.left.value > value:
                    current = current.rotate_right()
                else:
                    current = current.rotate_left_right()

        # The value to be inserted is greater than the current
        # node's value. The node is recursively inserted
        # to the current node's right children.
        elif value > current.value:
            current.right = self.insert(node, current.right)

            # If the current node's balance factor is less
            # than 1, then it is right-heavy. Perform the
            # appropriate rotations.
            # Ex: current = current.rotate_right_left()
            if current.balance() < -1:
                if current.right.value < value:
                    current = current.rotate_left()
                else:
                    current = current.rotate_right_left()
        else:
            raise ValueError("Cannot insert duplicate values")

        return current

    def delete(self, value, current):
        """Searches for a node holding a given value and removes it."""
        # TODO: Implement Me!
        
        # Current node is to be deleted, set current node's
        # value to None, or replace with successor if needed.
        if value == current.value:
            # Deleted node is a leaf
            if current.left is None and current.right is None:
                current = None
            # Deleted node has one child
            elif not (current.left and current.right):
                if current.left:
                    current = current.left
                else:
                    current = current.right
            # Deleted node has two children
            else:
                successor = self.find_min(current.right)
                temp = successor.value
                self.delete(successor.value, current)
                current.value = temp

        # The value to be deleted is less than the current
        # node's value. The node is recursively deleted
        # from the current node's left children.
        elif value < current.value:
            current.left = self.delete(value, current.left)

            # If the current node's balance factor is less
            # than 1, then it is right-heavy. Perform the
            # appropriate rotations.
            # Ex: current = current.rotate_right_left()
            if current.balance() < -1:
                if value < current.right.value:
                    current = current.rotate_left()
                else:
                    current = current.rotate_right_left()

        # The value to be deleted is greater than the current
        # node's value. The node is recursively deleted
        # from the current node's right children.
        elif value > current.value:
            current.right = self.delete(value, current.right)

            # If the current node's balance factor is greater
            # than 1, then it is left-heavy. Perform the
            # appropriate rotations.
            # Ex: current = current.rotate_right_left()
            if current.balance() > 1:
                if value > current.left.value:
                    current = current.rotate_right()
                else:
                    current = current.rotate_left_right()

        return current
        
    def find(self, value):
        """Finds and returns the node whose value matches the
        specified search value. Returns None if no node with a
        matching value is found."""
        # TODO: Implement Me!
        if value == self.value:
            return self
        elif value < self.value:
            if self.left is not None:
                return self.left.find(value)
            else:
                return None
        elif value > self.value:
            if self.right is not None:
                return self.right.find(value)
            else:
                return None
            
    def balance(self):
        """Returns the balance factor of a node, which is the
        height of its left subtree subtracted by the height of
        its right subtree."""
        return self.height(self.left) - self.height(self.right)
        
    def height(self, node):
        if not node:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def rotate_left(self):
        """Case 1, rotate self with left child. Returns new root."""
        root = self
        new = root.right
        root.right = new.left
        new.left = root
        return new

    def rotate_right(self):
        """Case 4, rotate self with right child. Returns new root."""
        root = self
        new = root.left
        root.left = new.right
        new.right = root
        return new

    def rotate_left_right(self):
        """Case 2, rotate self.left with its right child, then
        rotate the new self.left with self. Returns new root."""
        root = self
        root.left = root.left.rotate_left()
        return root.rotate_right()

    def rotate_right_left(self):
        """Case 3, rotate self.right with its left child, then
        rotate the new self.right with self. Returns new root."""
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

    def find_min(self, current):
        """Finds and returns the node holding the minimum value."""
        if current is not None:
            while current.left:
                current = current.left
        return current

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

    def delete(self, value):
        if self.root is None:
            raise ValueError("tree is empty")
        else:
            node = self.root.find(value)
            if node:
                self.root.delete(value, self.root)
            else:
                raise ValueError("value not found")

    def find(self, value):
        if self.root is None:
            return None
        node = self.root.find(value)
        return node

    def print(self):
        print(self.root.print())
        
        
tree = AVLTree()
for value in (8,2,12,1,5,10,14,3,9,11,4):
    tree.insert(value)
tree.print()
