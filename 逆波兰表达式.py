class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def push(self,item):
        return self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Solution(object):
    def is_number(self,number):
        try:
            int(number)
            return True
        except:
            pass
    def evalRPN(self,tokens):
        S = Stack()
        for i in range(len(tokens)):
            if self.is_number(tokens[i])!=None:
                S.push(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    a = S.pop()
                    b = S.pop()
                    S.push(b+a)
                elif tokens[i] == '-':
                    a = S.pop()
                    b = S.pop()
                    S.push(b-a)
                elif tokens[i] == '*':
                    a = S.pop()
                    b = S.pop()
                    S.push(a*b)
                elif tokens[i] == '/':
                    a = S.pop()
                    b = S.pop()
                    S.push(int(b/a))
        return S.peek()
if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = Solution()
    print(s.evalRPN(tokens))
