class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []

        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dict:
            return ""

        values = self.dict[key]   # THIS LINE

        l = 0
        r = len(values) - 1

        ans = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                ans = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans