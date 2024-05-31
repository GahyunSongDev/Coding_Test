## Queue 
- Array list based
- Linked list based
- FIFO ( First In First Out ) 특성 활용

- Why queue에서 array list based를 사용하지 않는 이유? 
    : Dequeue를 할 때 time complexity가 big-O(n) 이기 때문에.
- Queue에서 linked list based를 사용하는 이유?
    : python 의 deque를 사용하면 dequeue 할 때 time complexity가 big-O(1) 이기 때문에.
- 보통 queue 알고리즘 문제에서는 deque 를 사용하지 않고 보통 BFS 위해서 사용함.

## Stack 
- python의 push와 pop의 time complexity가 big-O(1) 으로 연산 되기때문에 Array list based를 사용해도 괜찮음.
- LIFO ( Last In First Out ) 특성 활용
- DFS(깊이 우선 탐색 = Depth-First Search)에 사용

[ 20. Valid Paranthese ]
1) Understand the problem
2) Think about it intuitively
    a. The data list must have an even number of elements.
    b. If there's an open bracket, it must have close the same type of bracket.
    c. It can’t have close bracket before the same type of an open bracket.
    d. The time complexity must be under n^2.

        Approach 1> Simply thinking of this problem when there’re only ‘()’, 
        S = “[()(())((()))]”
        valid = 0
        When there is an open bracket, valid increases by 1. When there is a corresponding close bracket, valid decreases by 1. Therefore, when it ends, if valid is 0 AND ‘valid’ never becomes negative, it returns True. If not, it returns False.

        Approach 2> Now, there’re all type of brackets such as (), [], {}.
        S = “()[[{}]]”
        Divide the bracket types and adjusting their counts accordingly, while also maintaining the order of brackets, you can ensure the validity of the bracket sequence. So, the important thing to consider is that if there’re a few open brackets first, there should be the same type of a close bracket of last open bracket in the list ‘S’
        => S = “()[[{}]]” -> it means that I can think of LIFO to solve this problem, which is ‘Stack’.
        
        <img width="404" alt="스크린샷 2024-05-31 오후 12 47 42" src="https://github.com/GahyunSongDev/Coding_Test/assets/160058929/9f0a258c-fa1c-4167-b205-db94f07c269c">

<img width="404" alt="스크린샷 2024-05-31 오후 12 47 42" src="https://github.com/GahyunSongDev/Coding_Test/assets/160058929/e0eb16d3-d8db-49c0-a522-79d92fd886cb">


        Finally, this Stack is empty and it returns TRUE.

3) Design psuedo code.
    For i in s
        If i == “(, [, {”
        Stack.push()
        If i == “), ], }”
        it’s a even number of elements
            Stack.pop()
    It’s not a even number of elements
    Returns False

                    After all elements are scanned,
                    If Stack.isEmpty(), True
                    If not, False

4) Implementation of this approach for the problem.
    class Solution(object):
        def isValid(self, s):
            Stack = [] # initiate the stack
            map_bracket = {‘)’ : ‘(’, ‘]’ : ‘[’, ‘}’ : ‘{’}

            for i in s:
                # See the element is an open bracket
                if i in map_bracket.values():
                    Stack.append(i)
                #See the element is a close bracket
                elif i in map_bracket.keys() :
                    if not Stack or map_bracket[i] != Stack.pop() :
                        return False
            return not Stack
