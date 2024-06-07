class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
                print("i : ", i)
                print("current_temp : ", curr_temp)
                print("prev_index : ", prev_index)
                print("result[prev_index : ", result[prev_index])
                print("------------------------------------------")

            # add the current day's index into the stack
            stack.append(i)

        return result



temperature = [73, 71, 69, 67, 72,76]
solution = Solution()
print(solution.dailyTemperatures(temperature))  