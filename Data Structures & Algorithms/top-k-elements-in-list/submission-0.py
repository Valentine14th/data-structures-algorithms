class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] = frequency[i] + 1
            else:
                frequency[i] = 1
        maxim = max(frequency.values())
        buckets = [[] for i in range(maxim+1)]
        for (val, freq) in frequency.items():
            buckets[freq].append(val)
        out = []
        return [val for lis in buckets for val in lis][-k:]




        