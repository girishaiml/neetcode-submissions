class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time_ahead = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time

        return fleets