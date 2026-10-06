class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token == "+":
                res.append(res.pop() + res.pop())
            elif token == "-":
                b = res.pop()
                a = res.pop()
                res.append(a - b)
            elif token == "*":
                res.append(res.pop() * res.pop())
            elif token == "/":
                b = res.pop()
                a = res.pop()
                res.append(int(a / b))
            else:
                res.append(int(token))
        return res[0]