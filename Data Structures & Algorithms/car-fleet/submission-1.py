class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a car's position at time i is position+i*speed (hours)
        # the fastest car will catch up to any before
        # if the one before doesn't reach the end first
        # we could just update a car's position at every i
        # using formula, but if go over any before, downgrade its speed
        # as soon as one reaches the end, take all the ones before
        # a wait they are at the same position, not one after the other
        # simulation, okay but slow
        # take leading car, it will arrive first no matter what
        # calculate tiem to reach end
        # calculate time to reach end of next cars
        # if lower than the first, cannot, bounded by it
        # p + x*speed = target <=> target-p // speed
        # wait I don't want time to end
        # i want arrival time, mmm same
        prevTime = -1
        fleets = 0
        mixed = [(position[i], speed[i]) for i in range(len(position))]
        mixed.sort(key=lambda x: x[0])
        print(mixed)
        for p in range(len(mixed)-1, -1, -1):
            time_to_end = (target - mixed[p][0]) / mixed[p][1]
            print(time_to_end)
            if prevTime < time_to_end:
                prevTime = time_to_end
                fleets += 1
        return fleets



        