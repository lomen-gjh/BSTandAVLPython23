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

    def rebalance(self):
        pass

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
    def insert(self, data):
        if self.data>data:
            if self.left==None:
                self.left=Node(data)
            else:
                self.left.insert(data) #rekurzivne poslem dalej
        elif self.data<data:
            if self.right==None:
                self.right=Node(data)
            else:
                self.right.insert(data)

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

    def delete(self, target, parent):
        if target<self.data:
            if self.left!=None:
                return self.left.delete(target, self)
            else:
                print("Neexistuje")
                return None
        elif target>self.data:
            if self.right!=None:
                return self.right.delete(target,self)
            else:
                print("Neexistuje")
                return None
        else:
            replacement=self.findReplacement()
            if parent.data>self.data:
                parent.left=replacement
            else:
                parent.right=replacement
            if replacement != None:
                replacement.left=self.left
                replacement.right=self.right

    def findReplacement(self):
        if self.left!=None:
            if self.left.right!=None:
                return self.left.right.findMax(self.left)
            else:
                forreturn=self.left
                self.left=self.left.left
                return forreturn
        elif self.right!=None:
            if self.right.left!=None:
                return self.right.left.findMin(self.right)
            else:
                forreturn=self.right
                self.right=self.right.right
                return forreturn
        else:
            return None

    def findMax(self, parent):
        if self.right==None:
            parent.right=self.left
            return self
        else:
            return self.right.findMax(self)

    def findMin(self, parent):
        if self.left==None:
            parent.left=self.right
            return self
        else:
            return self.left.findMin(self)

class AVLTree:
    def __init__(self):
        self.root=None

    def insert(self, data):  #Will be edited
        if self.root==None:
            self.root=Node(data)
        else:
            self.root.insert(data)




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
    def drawTree(self, canvas,x,y):
        pass
