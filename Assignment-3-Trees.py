#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Python program to introduce Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# In[14]:


def maxDepth(node):
    if node is None:
        return 0
    else:
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Height of tree is %d" % (maxDepth(root)))


# In[16]:


# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # Then print the data of node
        print(root.val, end=" "),
 
        # Now recur on right child
        printInorder(root.right)
print("Inorder traversal of binary tree is")
printInorder(root) 


# In[21]:


#Function to print all the leaves in a given binary tree
def newNode(data): 
    temp = Node(data) 
    return temp 

def printleafNodes(root): 
    # base case 
    if not root: 
        return
    # implement iterative preorder traversal and start 
    # storing leaf nodes. 
    st = [] 
    st.append(root) 
  
    while len(st) > 0: 
        root = st.pop() 
  
        # if node is leafnode, print its data 
        if not root.left and not root.right: 
            print(root.data, end=" ") 
  
        if root.right: 
            st.append(root.right) 
        if root.left: 
            st.append(root.left) 
# Driver program to test above functions 
if __name__ == '__main__': 

    # create a binary tree 
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.right.left = newNode(5) 
    root.right.right = newNode(8) 
    root.right.left.left = newNode(6) 
    root.right.left.right = newNode(7) 
    root.right.right.left = newNode(9) 
    root.right.right.right = newNode(10) 

    # prints leaf nodes of the given tree 
    printleafNodes(root) 


# In[24]:


#Find sum of all left leaves in a given Binary Tree
class Node:
 
    # A constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def leftLeavesSumRec(root, isLeft, summ):
    if root is None:
        return
     
    # Check whether this node is a leaf node and is left
    if root.left is None and root.right is None and isLeft == True:
        summ[0] += root.key
 
    # Pass 1 for left and 0 for right
    leftLeavesSumRec(root.left, 1, summ)
    leftLeavesSumRec(root.right, 0, summ)
     
# A wrapper over above recursive function
def leftLeavesSum(root):
    summ = [0] # initialize result
     
    # Use the above recursive function to evaluate sum
    leftLeavesSumRec(root, 0, summ)
     
    return summ[0]
 
# Driver program to test above function
 
# Let us construct the Binary Tree shown in the
# above figure
root = Node(20);
root.left= Node(9);
root.right   = Node(49);
root.right.left = Node(23);
root.right.right= Node(52);
root.right.right.left  = Node(50);
root.left.left  = Node(5);
root.left.right = Node(12);
root.left.right.right  = Node(12);
 
print ("Sum of left leaves is", leftLeavesSum(root))


# In[26]:


#Find sum of all nodes of the given perfect binary tree
import math
 
def sumNodes(l):
     
    # no of leaf nodes
    leafNodeCount = math.pow(2, l - 1);
 
    sumLastLevel = 0;
 
    # sum of nodes at last level
    sumLastLevel = ((leafNodeCount *
                  (leafNodeCount + 1)) / 2);
 
    # sum of all nodes
    sum = sumLastLevel * l;
 
    return int(sum);
 
# Driver Code
l = 3;
print (sumNodes(l));


# In[27]:


#Count subtress that sum up to a given value x in a binary tree
class getNode:
    def __init__(self, data):
 
        # put in the data
        self.data = data
        self.left = self.right = None
 
# function to count subtrees that
# Sum up to a given value x
 
def countSubtreesWithSumX(root, count, x):
 
    # if tree is empty
    if (not root):
        return 0
 
    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    # Sum of nodes in the subtree
    # rooted with 'root.data'
    Sum = ls + rs + root.data
 
    # if true
    if (Sum == x):
        count[0] += 1
 
    # return subtree's nodes Sum
    return Sum
 
# utility function to count subtrees
# that Sum up to a given value x
 
def countSubtreesWithSumXUtil(root, x):
 
    # if tree is empty
    if (not root):
        return 0
 
    count = [0]
 
    # Sum of nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    # Sum of nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    # if tree's nodes Sum == x
    if ((ls + rs + root.data) == x):
        count[0] += 1
 
    # required count of subtrees
    return count[0]
 
# Driver Code
if __name__ == '__main__':
 
    # binary tree creation
    #         5
    #         / \
    #     -10     3
    #     / \ / \
    #     9 8 -4 7
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)
 
    x = 7
 
    print("Count =",
          countSubtreesWithSumXUtil(root, x))


# In[28]:


#Find maximum level sum in Binary Tree
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
# Function to get sum of each level 
def dfs(root, level, mm): 
    # Base condition 
    if not root: 
        return
  
    # Adding root value to its level sum 
    mm[level] = mm.get(level, 0) + root.data 
  
    # Increasing level 
    level += 1
  
    # Moving left 
    dfs(root.left, level, mm) 
  
    # Moving right 
    dfs(root.right, level, mm)  
# Function to find the maximum sum of a level in the tree 
def maxLevelSum(root): 
    # Base case 
    if not root: 
        return 0
  
    # Map to store the sum of each level 
    mm = {} 
  
    # Calling the function to calculate the sum of each level 
    dfs(root, 0, mm) 
  
    # Variable to store the answer 
    result = float('-inf') 
  
    # Iterating over the map to find the maximum sum 
    for val in mm.values(): 
        result = max(result, val) 
  
    return result 
  
# Helper function to allocate a new node with the given data and NULL left and right pointers 
def newNode(data): 
    node = Node(data) 
    return node 
  
# Driver code 
if __name__ == "__main__": 
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 
    root.right.right = newNode(8) 
    root.right.right.left = newNode(6) 
    root.right.right.right = newNode(7) 
    print("Maximum level sum is", maxLevelSum(root)) 


# In[29]:


#Print the nodes at odd levels of a tree
def printOddNodes(root, isOdd = True):
     
    # If empty tree 
    if (root == None): 
        return
 
    # If current node is of odd level 
    if (isOdd): 
        print(root.data, end = " ")
 
    # Recur for children with isOdd 
    # switched. 
    printOddNodes(root.left, not isOdd) 
    printOddNodes(root.right, not isOdd)
# Driver code 
if __name__ == '__main__':
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 
    printOddNodes(root)


# In[ ]:




