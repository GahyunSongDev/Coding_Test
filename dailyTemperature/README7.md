[ 739. Daily Temperature ]

=> I’m going to use stack for this problems.
1. Understand the problem
2. Think about it intuitively
    - First Approach : I can think of this problems solving using 2 for loops. 
    - Second Approach : I can use stack which has the feature of LIFO as well as DFS.
        a. Initiate a stack and the result list
        b .Scan the temperature list
        c. While scanning the temperature list, I compare the current i-th temperature to the temperature on the top of the stack.
        d. If the current temperature is higher than the one on the top of the stack, the element gets popped,calculates the days, and updates the days in the result list I Initiated at first.

![alt text](<스크린샷 2024-06-07 오후 2.35.34.png>)
![alt text](<스크린샷 2024-06-07 오후 2.35.50.png>)
![alt text](<스크린샷 2024-06-07 오후 2.36.00.png>)

=> The time complexity : big-O(n) because it just needs to push and pop the elements from the stack during scanning the temperature list.
		
3. Design pseudo code
```python
    # use 2 lists
    Stack = []	# using for LIFO
    result = []	# using for printing the results of the days needed to wait to get warmer weather.

    For t in temperature
        While t > Stack[-1]
            Stack.pop()
            Update the days waited
            Put the day in result[]
        Stack.push(t)
    Return result
```

4. Implementation of this approach
