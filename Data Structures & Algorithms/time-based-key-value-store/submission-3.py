class TimeMap:

    def __init__(self):
        self.di = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.di[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        def bin(target, vals):
            # upper bound
            left = 0
            right = len(vals)
            while left < right:
                mid = (left+right) // 2
                if vals[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        t = bin(timestamp, self.di[key])
        vals = self.di[key]
        if t < len(vals) and vals[t][0] == timestamp:
            return vals[t][1]
        return self.di[key][t-1][1] if t-1 >= 0 else ""

        
