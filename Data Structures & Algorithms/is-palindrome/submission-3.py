class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        same = True
        left = 0
        right = len(s) - 1
        #better_s = [ord(s[i]) - ord("a") if ord(s[i]) >= ord("a") else ord(s[i]) - ord("A") for i in range(len(s))]
        while left < right:
            while not self.alphaNum(s[left]) and left < right:
                left +=1
            while not self.alphaNum(s[right]) and right > left:
                right -= 1
            #print(better_s[left], better_s[right])
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


 #       for i in range(len(s)):
 #           if s[i] != s[-i]:
 #               return False
 #       return True
        