'''
    
    program5.py
    Jali Purcell
    11/8/21-11/12/21 v. 4
    For program 5 of Algorithms
    

    CLASSES

        Node-represents a node on a binary search tree. Contains
        data, a pointer to a left node, and a pointer to a right node.
        Initially, the node has none for left and right, until more
        nodes are added onto the tree it's in.

        Tree-contains the structure for a binary search tree. Contains
        a root node, which is initialized as None.
        A root node is given when a node is added (using the add method)
        to the tree.

        

    METHODS

        add-adds a value to a tree, makes the value the root
        if there is no root, and calls to addNode if tree
        has nodes

        addNode-when passed a value, tree, and node, adds
        a node to the tree

        printInOrderTree-calls to printTreeFromNode if tree
        has a node. If no nodes are in the tree, an empty array
        is returned. If the root is not none, the results from
        printTreeFromNode are returned in list form.

        MODIFICATION: used return instead of print

        printTreeFromNode-performs an in order traversal given
        a tree and node,
        and returns in list form

        MODIFICATION instead of "self.printTreeFromNode(node.left)
                                 print(str(node.data)
                                 self.printTreeFromNode(node.right)"
        , changed to return the traversal in list form
        First traverses the left tree, the prints the root,
        then traverses the right tree

        Returned left+[node.data]+right instead of building an array with
        these values

        printPreOrderTree-calls to printPreTreeFromNode if the root
        is not none, and returns results in list form

        MODIFICATION: used return instead of print
        
        printPreTreeFromNode-performs a pre order traversal and
        returns in list form

        MODIFICATION instead of 
                                "print(str(node.data))
                                self.printPreTreeFromNode(node.left)
                                self.printPreTreeFromNode(node.right)"
        First prints the root, then traverses the left tree,
        then traverses the right tree

        Returns [node.data]+left+right
        
        printPostOrderTree-calls to printPostTreeFromNode if root is not
        none, returns the result in list form.

        MODIFICATION: used return instead of print
        
        printPostTreeFromNode-performs a post order traversal given
        a tree and a node, returns result in list form

        MODIFICATION instead of 
                                "self.printPostTreeFromNode(node.left)
                                self.printPostTreeFromNode(node.right)
                                print(str(node.data))",
        changed to return the traversal in list form
        First traverses the left tree, then traverses the right tree,
        then prints the root

        Returns left+right+[node.data]
        
        printCountLeaves-given a tree, calls to countLeaves if root is
        not none. A tree with no nodes has 0 leaves, so 0 is returned for
        an empty tree.
        
        countLeaves-Given a tree, and a node, the method looks for all the
        nodes on the left, and all the nodes on the right,
        whose right and left are both none
        (meaning, they have no children)

    OUTSIDE METHODS

        testTreeFunctions-basic test for add, node initializer,
        and tree initializer

        main-represets a layout of results from the traversals and
        leaf counter on one pre-made tree

        testTree-given test number, tree array, expected InOrder,
        expectedPreOrder, expectedPostOrder, and expected numbers
        of leaves, compares these values with the actual values given
        by the methods. Will print pass or fail.

        test-gives 6 examples of tests using testTree

        
'''

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Tree():
    def __init__(self):
        self.root=None

    # adds value to binary search tree
    def add(self,value):
        
        if(self.root==None):
            
            self.root=Node(value)
            
        else:
            
            self.addNode(value,self.root)

    # adds a node to a binary search tree
    def addNode(self,value, node):

        # adds left if less than root
        if value<node.data:
            
            if(node.left is None):
                
                node.left=Node(value)
            else:
                
                self.addNode(value,node.left)
        else:

            # adds right if greater than root
            if(node.right is None):
                
                node.right=Node(value)
                
            else:
                
                self.addNode(value,node.right)
        

    # use to print in order
    def printInOrderTree(self):
        
        if self.root is not None:

            # call with root
            return self.printTreeFromNode(self.root)
        
        else:
            
            return []

    
    def printTreeFromNode(self,node):
        
        if node is not None:
            
            left=[]
            right=[]
            
            if(node.left!=None):
                
                left=self.printTreeFromNode(node.left)
                
            if(node.right!=None):
                
                right=self.printTreeFromNode(node.right)

            # in order traverses left, then views root,
            # then traverses right
            return left+[node.data]+right
            

    # use to print pre-order 

    def printPreOrderTree(self):
        if self.root is not None:

            # call with root
            return self.printPreTreeFromNode(self.root)
        
        else:
            
            return []
      
    def printPreTreeFromNode(self,node):
        if node is not None:

            left=[]
            right=[]
            
            if(node.left!=None):
                
                left=self.printPreTreeFromNode(node.left)
                
            if(node.right!=None):
                
                right=self.printPreTreeFromNode(node.right)

            # pre order prints root, then traverses left,
            # then traverses right
            return [node.data]+left+right
        

    # use to print post-order

    def printPostOrderTree(self):
        if self.root is not None:

            # call with root
            return self.printPostTreeFromNode(self.root)
        
        else:
            
            return []
            
      
    def printPostTreeFromNode(self,node):
        if node is not None:

            left=[]
            right=[]
            
            if(node.left!=None):
                left=self.printPostTreeFromNode(node.left)
                
            if(node.right!=None):
                
                right=self.printPostTreeFromNode(node.right)
       
            # in order traverses left, then traverses right,
            # then adds root
            return left+right+[node.data]
            
    # use to print number of leaves
    def printCountLeaves(self):
        if self.root is not None:

            # call with root
            return self.countLeaves(self.root)
        
        else:

            # no leaves if no root
            return 0
    
    def countLeaves(self,node):
        left=0
        right=0
        leafcounter=0
        
        if(node.left!=None):
            
            left=self.countLeaves(node.left)
            
        if(node.right!=None):
            
            right=self.countLeaves(node.right)

        # if node has no children    
        if(node.left==None and node.right==None):

            # iterate leaf counter
            leafcounter=leafcounter+1
            
        leafcounter=leafcounter+left+right
        
        return leafcounter
        
# tests add/initializer          
def testTreeFunctions(array, expectedLeft, expectedRight, expectedRoot):
    tree=Tree()
    for value in array:
        tree.add(value)
    if(expectedRoot!=tree.root.data):
        print("Test for root failed")
    elif(expectedLeft!=tree.root.left.data):
        print("Test for left failed")
    elif(expectedRight!=tree.root.right.data):
        print("Test for right failed")
    else:
        print("All tests passed!")
    
# first tree traversal "test"
def main():


    tree=Tree()
    array=[5,3,4,9,1,6]
    print("Given "+str(array))
    for value in array:
        tree.add(value)
    print("In order")
    print(tree.printInOrderTree())

    
    print("")
    print("Pre order")
    print(tree.printPreOrderTree())
    print("")
    
    print("Post order")
    tree.printPostOrderTree()
    print(tree.printPostOrderTree())
    print("")
    
    print("Number of leaves: ")
    print(tree.printCountLeaves())
    print("")

def testTree(number, array, expectedIn, expectedPre, expectedPost, leaves):
    tree=Tree()
    for value in array:
        tree.add(value)
        
    # check in order
    inOrderTree=tree.printInOrderTree()
    if(inOrderTree==expectedIn):
        print("Test "+str(number)+" In order pass")
    else:
        print("Test "+str(number)+" In order fail")
        print("Expected "+str(expectedIn)+ " but found " + str(inOrderTree))

    # check pre order
    preOrderTree=tree.printPreOrderTree()
    if(preOrderTree==expectedPre):
        print("Test "+str(number)+" Pre order pass")
    else:
        print("Test "+str(number)+" Pre order fail")
        print("Expected "+str(expectedPre)+ " but found " + str(preOrderTree))

    # check post order
    postOrderTree=tree.printPostOrderTree()
    if(postOrderTree==expectedPost):
        print("Test "+str(number)+" Post order pass")
    else:
        print("Test "+str(number)+" Post order fail")
        print("Expected "+str(expectedPost)+ " but found " + str(postOrderTree))

    # check leaves count
    leavesCount=tree.printCountLeaves()
    if(leavesCount==leaves):
        print("Test "+str(number)+" Leaves count pass")
    else:
        print("Test "+str(number)+" Leaves count fail")
        print("Expected "+str(leaves)+ " but found " + str(leavesCount))
    

def test():

    # given tests
    testTree(1, [1,2,3,4,5,6,7,8],
             [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],1)
    
    testTree(2, [7,2,11,5,10,3,6,9,1,8],[1,2,3,5,6,7,8,9,10,11],
             [7,2,1,5,3,6,11,10,9,8],[1,3,6,5,2,8,9,10,11,7],4)
    
    testTree(3,[],[],[],[],0)

    # my tests
    testTree(4,[8,3,1,10,6,4,7,14,13],[1,3,4,6,7,8,10,13,14],
             [8,3,1,6,4,7,10,14,13],[1,4,7,6,3,13,14,10,8],4)
    
    testTree(5,[3,1,4,0,2,9,5,10],[0,1,2,3,4,5,9,10],
             [3,1,0,2,4,9,5,10],[0,2,1,5,10,9,4,3],4)
    
    testTree(6,[9,7,5,3,1,2,4,6,8],[1,2,3,4,5,6,7,8,9],
             [9,7,5,3,1,2,4,6,8],[2,1,4,3,6,5,8,7,9],4)
    

    
    

    
    


