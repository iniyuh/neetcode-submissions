class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hm[key]

        if not arr: return ""

        l, r = 0, len(arr) - 1

        ret_ts = 0
        ret_val = ""

        while l <= r:
            m = (l + r) // 2
            ts, val = arr[m]

            if ts == timestamp: return val
            elif ts < timestamp: 
                if ret_ts < ts:
                    ret_ts = ts
                    ret_val = val
                l = m + 1
            else: r = m - 1

        return ret_val


