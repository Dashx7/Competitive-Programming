n, k = map(int, input().split())

memory = []

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def update(self, pos, value):
        pos += self.size
        self.tree[pos] += value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        result = 0
        left += self.size
        right += self.size
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

memory = SegmentTree(n+1)

for _ in range(k):
    query = input().split()
    if query[0] == "F":
        query_val = memory.query(int(query[1]), int(query[1])+1)
        # print(query_val)

        if query_val == 0:
            memory.update(int(query[1]), 1)
        else:
            memory.update(int(query[1]), -1)
    elif query[0] == "C":
        # print(memory.tree)
        print(memory.query(int(query[1]), int(query[2])+1))