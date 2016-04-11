# Data Structures & Algorithms
# Tutorial 8: Trees
# Name: TODO Write your name here
# NPM: TODO Write your NPM here


def main():
    tree = BinaryTree(
        TreeNode('A',
                 TreeNode('B'),
                 TreeNode('C',
                          TreeNode('D',
                                   None,
                                   TreeNode('E')),
                          TreeNode('F',
                                   TreeNode('G'),
                                   None))))
    print(tree.height())
    tree.preOrder()
    tree.inOrder()
    tree.postOrder()
    print(len(tree))

class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def height(self):
        return "Tree height: " + str(self.root.height(self.root))

    def preOrder(self):
        print("Pre-order traversal:")
        self.root.preOrder(self.root)

    def inOrder(self):
        print("In-order traversal:")
        self.root.inOrder(self.root)

    def postOrder(self):
        print("Post-order traversal:")
        self.root.postOrder(self.root)

    def __len__(self):
        return self.root.count(self.root)
    

class TreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "(Node) {}".format(self.data)

    def height(self, current):
        # TODO: Implement Me!
        if current is None:
            return -1
        else:
            return 1 + max(self.height(current.left),
                           self.height(current.right))

    def preOrder(self, current):
        """Prints the tree nodes using pre-order traversal."""
        print(current)
        if current.left is not None:
            self.preOrder(current.left)
        if current.right is not None:
            self.preOrder(current.right)

    def inOrder(self, current):
        """Prints the tree nodes using in-order traversal."""
        # TODO: Implement Me!
        if current.left is not None:
            self.inOrder(current.left)
        print(current)
        if current.right is not None:
            self.inOrder(current.right)

    def postOrder(self, current):
        """Prints the tree nodes using post-order traversal."""
        # TODO: Implement Me!
        if current.left is not None:
            self.postOrder(current.left)
        if current.right is not None:
            self.postOrder(current.right)
        print(current)

    def count(self, current):
        """Returns the length of the nodes in the tree."""
        # TODO: Implement Me!
        # HINT: Similar to any of the 3 tree traversal algorithms!
        #       Think recursively, use base case and general case!
        if current is None:
            return 0
        else:
            n = 1
            if current.left is not None:
                n += self.count(current.left)
            if current.right is not None:
                n += self.count(current.right)
            return n

if __name__ == '__main__':
    main()
