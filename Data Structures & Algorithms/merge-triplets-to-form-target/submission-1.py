class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # okay we need to pick the lowest possible triplet
        # if all lower than the target, continue
        # check if any of the triplets have the number we want
        triplets.sort()
        print(triplets)
        curr = [0,0,0]
        for t in triplets:
            match = False
            bigger = False
            for i, v in enumerate(t):
                if v > target[i]:
                    bigger = True
                if v == target[i]:
                    match = True
            if match and not bigger:
                curr[0] = max(curr[0], t[0])
                curr[1] = max(curr[1], t[1])
                curr[2] = max(curr[2], t[2])
        return curr == target


        
        