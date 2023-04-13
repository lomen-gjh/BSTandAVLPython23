class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.balance=0
        self.depth=0

    def updateBalance(self):
        if self.left!=None and self.right!=None:
            self.depth=max(self.left.depth, self.right.depth)+1
            self.balance=self.left.depth-self.right.depth
        elif self.left!=None:
            self.depth=self.left.depth+1
            self.balance=self.left.depth+1
        elif self.right!=None:
            self.depth=self.right.depth+1
            self.balance=-self.right.depth-1
        else:
            self.depth=0
            self.balance=0

    def rebalance(self, parent):
        self.updateBalance()
        if self.balance>1:
            if self.left.balance>0:         #self left left
                self.rightRot(parent)
            else:                           #self left right
                self.leftRightRot(parent)
        elif self.balance<-1:
            if self.right.balance<0:        #self right right
                self.leftRot(parent)
            else:                           #self right left
                self.rightLeftRot(parent)

    def leftRot(self, parent):
        if self.data>parent.data:
            parent.right=self.right
            self.right=parent.right.left
            parent.right.left=self
            self.updateBalance()
            parent.right.updateBalance()

        else:
            parent.left = self.right
            self.right = parent.left.left
            parent.left.left = self
            self.updateBalance()
            parent.left.updateBalance()
        parent.updateBalance()

    def rightRot(self, parent):
        if self.data>parent.data:
            parent.right=self.left
            self.left=parent.right.right
            parent.right.right=self
            self.updateBalance()
            parent.right.updateBalance()

        else:
            parent.left = self.left
            self.left = parent.left.right
            parent.left.right = self
            self.updateBalance()
            parent.left.updateBalance()
        parent.updateBalance()

    def leftRightRot(self, parent):
        if self.data>parent.data:
            parent.right=self.left.right
            self.left.right=parent.right.left
            parent.right.left=self.left
            self.left=parent.right.right
            parent.right.right=self
            parent.right.right.updateBalance()
            parent.right.left.updateBalance()
            parent.right.updateBalance()
        else:
            parent.left = self.left.right
            self.left.right = parent.left.left
            parent.left.left = self.left
            self.left = parent.left.right
            parent.left.right = self
            parent.left.right.updateBalance()
            parent.left.left.updateBalance()
            parent.left.updateBalance()
        parent.updateBalance()
    def rightLeftRot(self, parent):
        if self.data>parent.data:
            parent.right=self.right.left
            self.right.left=parent.right.right
            parent.right.right=self.right
            self.right=parent.right.left
            parent.right.left=self
            parent.right.right.updateBalance()
            parent.right.left.updateBalance()
            parent.right.updateBalance()
        else:
            parent.left = self.right.left
            self.right.left = parent.left.right
            parent.left.right = self.right
            self.right = parent.left.left
            parent.left.left = self
            parent.left.right.updateBalance()
            parent.left.left.updateBalance()
            parent.left.updateBalance()
        parent.updateBalance()
    def insert(self, data, parent):
        if self.data>data:
            if self.left==None:
                self.left=Node(data)
            else:
                self.left.insert(data, self) #rekurzivne poslem dalej
        elif self.data<data:
            if self.right==None:
                self.right=Node(data)
            else:
                self.right.insert(data, self)
        self.rebalance(parent)

    def preorder(self):
        print(self.data, end=" ")
        if self.left!=None:
            self.left.preorder()
        if self.right!=None:
            self.right.preorder()

    def inorder(self):
        if self.left!=None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right!=None:
            self.right.inorder()

    def postorder(self):
        if self.left!=None:
            self.left.postorder()
        if self.right!=None:
            self.right.postorder()
        print(self.data,end=" ")

    def drawNode(self, canvas,x,y):
        pass


class AVLTree:
    def __init__(self):
        self.root=None

    def insert(self, data):  #Will be edited
        if self.root==None:
            self.root=Node(data)
        else:
            fakeparent=Node(-1000)
            fakeparent.right=self.root
            fakeparent.updateBalance()
            self.root.insert(data, fakeparent)
            self.root=fakeparent.right


    def printTree(self):
        if self.root!=None:
            print("Preorder: ",end="")
            self.root.preorder()
            print() #zalomi riadok po vypise preorder
            print("Inorder: ",end="")
            self.root.inorder()
            print()
            print("Postorder: ",end="")
            self.root.postorder()
            print()
            print("---------------")
    def drawTree(self, canvas,x,y):
        pass

avl=AVLTree()
avl.insert(50)
avl.insert(60)
avl.insert(70)
avl.printTree()
avl.insert(80)
avl.insert(90)
avl.printTree()