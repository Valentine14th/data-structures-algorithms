class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for (g, c) in zip(gas, cost)]
        print(diff)
        if sum(diff) < 0:
            return -1
        run_sum = 0
        answer = 0
        i = 0
        while i < len(diff):
            if run_sum + diff[i] < 0:
                while diff[i] < 0:
                    i += 1
                answer = i
                run_sum = diff[i] 
            else:
                run_sum += diff[i]
            i += 1
            
        return answer



        