# from segment_tree import SegmentTree # Ended up copying segtree code because I couldn't import it

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

def count_inversions(arr):
    sorted_arr = sorted(set(arr))  # Sort first
    rank = {v: i for i, v in enumerate(sorted_arr)}  # val to index mapping
    # empty = [0] * len(sorted_arr)
    # seg_tree = SegmentTree(empty)  # Initialize segment tree with zeros
    seg_tree = SegmentTree(len(sorted_arr)+1)  # Initialize segment tree with zeros
    inversions = 0

    for i in range(len(arr)):  # Looping through counting inversions
        pos = rank[arr[i]]  # Get the position of the current element in the sorted array
        inversions += seg_tree.query(pos, len(sorted_arr))
        seg_tree.update(pos, 1) # Update the segment tree to include the current element

    return inversions

# Example usage
n = int(input())
students = [int(input()) for _ in range(n)]
inversions = count_inversions(students)
print(inversions)