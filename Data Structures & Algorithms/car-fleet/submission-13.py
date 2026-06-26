class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        combined.sort(reverse=True)

        stack = []

        for p, s in combined:
            time = (target - p) / s

            if not stack: stack.append(time)
            else: 
                if time > stack[-1]: stack.append(time)

        return len(stack)