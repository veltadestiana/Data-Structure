# Data Structures & Algorithms
# Tutorial 9: Binary Search Tree
# Name: TODO Write your name here
# NPM: TODO Write your NPM here


def main():
    
    # Initialization
    def init_tree():
        tree = BinarySearchTree()
        values = [8,2,12,1,5,10,14,3,9,11,4]
        for value in values:
            tree.insert(value)
        return tree
    
    print("Initial tree: ")
    init_tree().print()

    # Remove node with one child (Remove 3)
    print("\nTest 1: Remove node with one child")
    tree = init_tree()
    tree.remove(3)
    tree.print()

    # Remove node with two children (Remove 2)
    print("\nTest 2: Remove node with two children")
    tree = init_tree()
    tree.remove(2)
    tree.print()

    # Remove root
    print("\nTest 3: Remove root")
    tree = init_tree()
    tree.remove(tree.root.value)
    tree.print()

    # Find a value, min, and max (Find 10, find min, find max)
    print("\nTest 4: Find a value, min, and max")
    tree = init_tree()
    print(tree.find(10))
    print(tree.find_min())
    print(tree.find_max())

    # Remove min and max (Insert -16, insert 99, remove min, remove max)
    print("\nTest 5: Remove min and max")
    tree = init_tree()
    tree.remove_min()
    tree.remove_max()
    tree.print()


class BinarySearchTree:
    """ An implementation of a binary search tree with basic functions.
    All binary search tree operations are accessed via this object, not
    the BSTNode object. Uses the BSTNode class for its tree nodes."""

    def __init__(self, root=None):
        self.root = root

    def find_min(self):
        return self.root.find_min(self.root)

    def find_max(self):
        return self.root.find_max(self.root)

    def find(self, value):
        if self.root is None:
            return None
        node = self.root.find(value)
        return node

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self.root.insert(value, self.root)

    def remove(self, value):
        node = self.find(value)
        if node is not None:
            self.root.remove(node)
        else:
            raise ValueError("value not found")

    def remove_min(self):
        # TODO: Implement Me!
        node = self.find_min()
        print("Min: " + str(node))
        if node is not None:
            self.root.remove(node)

    def remove_max(self):
        # TODO: Implement Me!
        node = self.find_max()
        print("Max: " + str(node))
        if node is not None:
            self.root.remove(node)

    def height(self):
        return "Tree height: " + str(self.root.height(self.root))

    def print(self):
        if self.root is None:
            print("Empty tree.")
        else:
            q = []
            q.insert(0, self.root)
            while q:
                current = q.pop()
                print(current)
                if current.has_left():
                    q.insert(0, current.left)
                if current.has_right():
                    q.insert(0, current.right)
                

    def __getitem__(self, value):
        """Makes the tree subscriptable. Example: print(tree[8])"""
        return self.find(value)

    def __contains__(self, value):
        """Allows the 'in' operator to be used on the tree."""
        return True if self.find(value) is not None else False


class BSTNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def has_left(self):
        return True if self.left is not None else False

    def has_right(self):
        return True if self.right is not None else False

    def is_leaf(self):
        return True if not self.left and not self.right else False

    def find_min(self, current):
        """Finds and returns the node holding the minimum value."""
        # TODO: Implement Me!
        if current is not None:
            while current.has_left():
                current = current.left
        return current

    def find_max(self, current):
        """Finds and returns the node holding the maximum value."""
        # TODO: Implement Me!
        if current is not None:
            while current.has_right():
                current = current.right
        return current

    def find(self, value):
        """Finds and returns the node whose value matches the
        specified search value. Returns None if no node with a
        matching value is found."""
        # TODO: Implement Me!
        if value == self.value:
            return self
        elif value < self.value:
            if self.has_left():
                return self.left.find(value)
            else:
                return None
        elif value > self.value:
            if self.has_right():
                return self.right.find(value)
            else:
                return None

    def insert(self, value, current):
        """Inserts a value into the binary search tree. Is called
        by BinarySearchTree as a helper function."""
        # TODO: Implement Me!
        if current is None:
            current = BSTNode(value)
        elif value < current.value:
            if current.left:
                self.insert(value, current.left)
            else:
                current.left = BSTNode(value)
        elif value > current.value:
            if current.right:
                self.insert(value, current.right)
            else:
                current.right = BSTNode(value)
        else:
            raise ValueError("Cannot insert duplicate values")
        return current

    def remove(self, node):
        """Removes a specified node once BinarySearchTree.find()
        finds the node to be removed. Is called by BinarySearchTree
        as a helper function."""
        # TODO: Implement Me!
        # Deleted node is a leaf
        if node.is_leaf():
            node = None
        else:
            # Deleted node has one child
            if not node.has_left() and not node.has_right():
                if node.has_left():
                    node = node.left 
                else:
                    node = node.right
            # Deleted node has two children
            else:
                successor = self.find_min(self.right)
                node.value = successor.value
                self.remove(successor)
                
    def __str__(self):
        left_value = self.left.value if self.left is not None else None
        right_value = self.right.value if self.right is not None else None
        return "(Node: {}, left={}, right={}) ".format(
            self.value, left_value, right_value)


if __name__ == '__main__':
    main()
