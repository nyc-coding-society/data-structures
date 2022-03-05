
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
        else:
            p = self.root
            while True:
                if value > p.value: # check right
                    if p.right == None:
                        p.right = new_node
                        break
                    else:
                        p = p.right
                else: # check left
                    if p.left == None:
                        p.left = new_node
                        break
                    else:
                        p = p.left


    def inorder(self):
        self.visit(self.root)

    def visit(self, p):
        if p == None:
            return
        self.visit(p.left)
        print(p.value)
        self.visit(p.right)

    def print_tree(self):
        stack = []
        p = self.root
        while True:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                if len(stack) == 0:
                    break
                else:
                    p = stack.pop(-1)
                    print(p.value, end=" ")
                    p = p.right

    def remove(self, value):
        pass


bst = BST()
bst.insert(100)
bst.insert(35)
bst.insert(220)
bst.insert(44)
bst.insert(101)
bst.insert(3)
bst.insert(105)
bst.insert(78)
bst.insert(189)
# bst.inorder()
bst.print_tree()