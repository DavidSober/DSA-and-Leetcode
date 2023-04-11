# beats 85% in time and 65% in space
# I recalled this from chapter

def dailyTemperatures(temperatures):
    stack = []
    answer = [0] * len(temperatures) # since all elements are initially 0 we dont have to worry about making last element 0 
                                     # last element should always be zero for this problem
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]: # if monotonically decreasing stack is broken 
            j = stack.pop()    # we continuosly pop elements in order to restore the decreasing order
            answer[j] = i - j  # the delta of the curr element and popped element is the days delta between old temp and warmer temp
        stack.append(i)  # if monotonoicllly decreasing stack is preserved we just add the next element to stack
    
    return answer

