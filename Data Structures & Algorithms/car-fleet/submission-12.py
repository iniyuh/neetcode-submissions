class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(position[i], speed[i]) for i in range(len(position))]
        stack.sort()

        ret = 0

        while stack:
            new_stack = []
            prev = float('inf')
            time = None

            for i in range(len(stack)):
                p, s = stack.pop()

                if p + s >= prev and prev != target: 
                    print("joined", p, s)
                    continue
                else:
                    if p + s >= target: 
                        if time and (target - p) / s <= time:
                            print("joined", p, s, "time", (target - p) / s, "previous time", time)
                            continue
                        else:
                            print("reached", p, s)
                            time = (target - p) / s
                            ret += 1
                            prev = target
                    else:
                        print("ongoing", p, s)
                        new_stack.append((p + s, s))
                        prev = p + s

            
            new_stack.reverse()
            stack = new_stack
        
        return ret
