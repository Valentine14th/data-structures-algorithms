class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checkRate(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h
        # any pile which has less than k is a waste of time
        # if all piles are divisible by k we don't waste any time
        # we can safely eat all bananas if we take the max of the array (given h > len(piles))
        # how much can we decrease it to still be safe? How can we check?
        # let's say from max we divide by 2, takes 2x more to eat max, 
        # every pile where m > m/2 > p takes 2x or 2x+1 more time to eat 
        # where m/2 < p constant amount
        # if m-1, either I need +1 or the same to eat a pile
        maxi = max(piles)
        l = 1
        r = maxi
        test = -1
        res = maxi

        while l <= r:
            test = (l + r) // 2
            print(test, l, r)
            if checkRate(test):
                # we can eat, we need to look for smaller
                res = test
                r = test - 1
            else:
                l = test + 1
        return res
        






        # stuuuupid
        # hooolyyyy
        # gooood stuffff
        # maths
        # divide and stuff
        # find maximum and do cool things
        # just eat all the bananas come on not that hard
        # just chomp chomp chomp
        # say just eat faster
        # you can do it
        # wooohoooooooo
        # gogogogogogogo
        # this should be good enough for the interview