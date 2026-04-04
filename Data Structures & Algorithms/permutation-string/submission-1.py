class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        subcount = [0]*26
        count = [0]*26
        for i in range(len(s1)):
            subcount[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] += 1
        if subcount == count:
            return True
        left = 0
        right = len(s1)
        while right < len(s2):
            count[ord(s2[right]) - ord('a')] += 1
            count[ord(s2[left]) - ord('a')] -= 1
            if count == subcount:
                return True
            left += 1
            right += 1
        return False



        