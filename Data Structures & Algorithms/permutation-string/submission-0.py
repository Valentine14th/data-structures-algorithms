class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = [0 for i in range(26)]
        for s in s1:
            s1count[ord(s) - ord('a')] += 1
        left = 0
        right = 0
        currcount = [0 for i in range(26)]
        while left < len(s2) and right < len(s2):
            index = ord(s2[right]) - ord('a')
            currcount[index] += 1
            while currcount[index] > s1count[index]:
                print("too many ", chr(index + ord('a')))
                indexl = ord(s2[left]) - ord('a')
                currcount[indexl] -= 1
                left += 1
                print("adapt left", left, right)
                if right < left:
                    right = left - 1
                    print("adapt right", left, right)
            if right - left + 1 == len(s1):
                return True
            else:
                right += 1
                print("add right", left, right)
        return False




        