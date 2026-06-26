class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []

        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hm:
            for v, t in reversed(self.hm[key]):
                if t <= timestamp: return v

        return ""
