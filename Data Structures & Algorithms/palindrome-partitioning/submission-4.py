class Solution:
    def partition(self, s: str) -> List[List[str]]:

        base = list(s)
        out = []

        def isPalindrome(s: str):
            for i in range(math.ceil(len(s)/2)):
                if s[i] != s[-i-1]:
                    print("no", s)
                    return False
            return True

        def recurse(i, curr):
            print(i, curr)
            if i >= len(curr):
                return
            if not isPalindrome(curr[i]):
                if i+1 < len(curr):
                    # we combine with the next
                    recurse(i, curr[:i] + [curr[i]+curr[i+1]] + curr[i+2:])
            else:
                if curr not in out:
                    out.append(curr)
                if i+1 < len(curr):
                    # we combine with the next
                    recurse(i, curr[:i] + [curr[i]+curr[i+1]] + curr[i+2:])
                # we don't combine with the next
                recurse(i+1, curr)

        recurse(0, base)
        return out





        