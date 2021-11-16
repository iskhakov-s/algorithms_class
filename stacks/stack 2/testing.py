from ..stack import Stack


def q1():
    stk = Stack()
    stk.push(3)
    print(stk.pop())
    stk.push(2)
    stk.push(1)
    print(stk.pop())
    print(stk.pop())
    

def q2():
    # pops 5,2,3,4,1,6
    stk = Stack()
    stk.push(6)
    stk.push(5)
    print(stk.pop())
    stk.push(4)
    stk.push(3)
    stk.push(2)
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    stk.push(1)
    print(stk.pop())
    print(stk.pop())
    

if __name__ == '__main__':
    q1()

