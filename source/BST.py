class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

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

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.root.insert(data)

    def delete(self, target):
        if self.root==None:
            print("BST is empty")
            return None
        elif self.root.data==target:
            rep=self.root.findReplacement() #najdi nahradcu
            rep.left=self.root.left #nahradcovi pridaj lavu stranu rootu
            rep.right=self.root.right #nahradcovi pridaj pravu stranu rootu
            forreturn=self.root
            self.root=rep # root pointer nastav teraz na nahradcu, povodny root vyzbiera GC
            return forreturn
        else:
            if self.root.data>target:
                if self.root.left!=None:
                    return self.root.left.delete(target, self.root)
                else:
                    print("No such value in BST")
                    return None
            else:
                if self.root.right!=None:
                    return self.root.right.delete(target, self.root)
                else:
                    print("No such value in BST")
                    return None


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
stromcek=BinarySearchTree()
for i in 50, 30, 90, 80,20,13, 44,57,78,12:
    stromcek.insert(i)
stromcek.printTree()
stromcek.delete(90)
stromcek.delete(80)
stromcek.delete(12)
stromcek.delete(50)
stromcek.printTree()