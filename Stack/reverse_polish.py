# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


# trick : push each token into stack, when operator got, pop two times and do operation and push into stack


from math import ceil, floor


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "-", "*", "/"]
        
        def cal(token, num1, num2):
            
            if token=="+":
                return num1+num2
            if token=="*":
                return num1*num2
            if token=="-":
                return num1-num2
            if token=="/":
                return int(num1/num2)
            
                
                
        for token in tokens:
            
            # base case
            if token in operator:
                num2 = stack.pop()
                num1 = stack.pop()
                res = cal(token, num1, num2)
                stack.append(res)
                continue
                
            stack.append(int(token))
            
        return stack.pop()
            