class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(",")
        for i in preorder:
            stack.append(i)
            while(self.isTopTwoSharp(stack)):
                tmp = stack.pop()
                tmp = stack.pop()
                
                if(len(stack) == 0):
                    return False
                tmp = stack.pop()
                stack.append("#")
        if(len(stack) == 1 and stack[0] == "#"):
            return True
        return False


    def isTopTwoSharp(self, stack):
        top = len(stack) - 1
        if(top < 1):
            return False
        if(stack[top] == "#" and stack[top - 1] == "#"):
            return True
        return False