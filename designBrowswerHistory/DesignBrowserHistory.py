class BrowserHistory(object):

    def __init__(self, homepage):
        self.hist = [homepage]
        self.currentPos = 1 #initiate the current position to 1

    def visit(self, url):
        self.hist = self.hist[0:self.curr_pos] # extract the part of the list from index 0 to currentPos
        self.hist.append(url) # insert the 'url' in the list
        self.curr_pos = len(self.hist)  # include the url's index in the length of the list

    def back(self, steps):
        self.curr_pos = max(1, self.curr_pos - steps)
        return self.hist[self.curr_pos-1]

    def forward(self, steps):
        self.curr_pos = min(len(self.hist), self.curr_pos + steps)
        return self.hist[self.curr_pos-1]
    
# # Doubly linked list
# class ListNode:
#     def __init__(self, val):
#         self.previous = None
#         self.next = None
#         self.val = val # Url represented by the node

# class BrowserHistory(object):

#     def __init__(self, homepage: str):
#         self.current = ListNode(homepage)
        
#     def visit(self, url:str) -> None:
#         node = ListNode(url)
#         node.previous = self.current
#         self.current.next = node
#         self.current = self.current.next
        

#     def back(self, steps: int) -> str:
#         while(steps and self.current.previous):
#             self.current = self.current.previous
#             steps -= 1
#         return self.current.val
        
#     def forward(self, steps: int) -> str:
#         while(steps and self.current.next):
#             self.current = self.current.next
#             steps -= 1
#         return self.current.val