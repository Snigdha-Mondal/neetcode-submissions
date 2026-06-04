class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+','-','*','/']

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                x1=stack.pop()
                x2=stack.pop()
                if c=='+':
                    result=x2+x1
                elif c=='-':
                    result=x2-x1
                elif c=='*':
                    result=x2*x1
                else:
                    result=int(x2/x1)
                stack.append(result)

        return stack[0]