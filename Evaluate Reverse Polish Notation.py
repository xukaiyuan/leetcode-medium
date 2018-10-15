class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = [tokens[0]]

        operation = set(["+", "-", "*", "/"])

        for i in range(1, len(tokens)):
            if(tokens[i] not in operation):
                stack.append(tokens[i])
            else:
                op2 = int(stack.pop(-1))
                op1 = int(stack.pop(-1))
                
                tmp_res = 0

                if(tokens[i] == "+"):
                    tmp_res = op1 + op2                  
                elif(tokens[i] == "-"):
                    tmp_res = op1 - op2
                elif(tokens[i] == "*"):
                    tmp_res = op1 * op2
                else:
                    tmp_res = int(op1 / op2)
                stack.append(str(tmp_res))
                
        return int(stack[0])
