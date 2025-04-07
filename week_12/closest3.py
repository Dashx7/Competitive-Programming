from collections import defaultdict
import bisect

size, queries = map(int, input().split())
arr = list(map(int, input().split()))

lastSeen = defaultdict(lambda: -1)
distances = [None] * size

class AnswerList:
    def __init__(self, leftIndex = -1):
        self.answers = []
        self.leftIndex = leftIndex # The left index of the segment
        # self.rightIndex = -1 # The right index of the segment
    def setAnswers(self, leftIndex, answers):
        self.leftIndex = leftIndex
        self.answers = answers
    def addAnswer(self, index, distance):
        # Find the position of the inserted value
        leftIndex = bisect.bisect(self.answers, (index, distance))
        left = self.answers[leftIndex-1] if leftIndex > 0 else None
        if left is None:
            self.answers.append((index, distance))
            return
        if left[1] >= distance:
            return
        else:
            bisect.insort(self.answers, (index, distance))
            # Remove all elements after the inserted value with distance <= the inserted distance
            self.answers = self.answers[:leftIndex + 1] + [
                item for item in self.answers[leftIndex + 1:] if item[1] > distance # Slow?
            ]
    def getBestScore(self, leftIndex):
        if self.answers:
            #Binary search for the best score where the left index >= the index
            index = bisect.bisect_left(self.answers, (leftIndex, float('-inf')))
            if index < len(self.answers):
                return self.answers[index][1]
        return -1
    def __repr__(self):
        return f"AnswerList(leftIndex={self.leftIndex}, answers={self.answers})"

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [AnswerList() for _ in range(2 * size)]

    def update(self, pos, index, distance):
        # Update a single position in the segment tree
        pos += self.size
        self.tree[pos].addAnswer(index, distance)
        while pos > 1:
            pos //= 2
            self.tree[pos] = AnswerList()
            # Copy the left child
            self.tree[pos].setAnswers(self.tree[2 * pos].leftIndex, self.tree[2 * pos].answers)
            # Merge the right child into the left
            for answer in self.tree[2 * pos + 1].answers:
                self.tree[pos].addAnswer(answer[0], answer[1])

    def query(self, left, right):
        # Query the range [left, right)
        left += self.size
        right += self.size
        result = AnswerList()
        while left < right:
            if left % 2:
                for answer in self.tree[left].answers:
                    result.addAnswer(answer[0], answer[1])
                left += 1
            if right % 2:
                right -= 1
                for answer in self.tree[right].answers:
                    result.addAnswer(answer[0], answer[1])
            left //= 2
            right //= 2
        return result
    
segTree = SegmentTree(size)
for i in range(len(arr)):
    if lastSeen[arr[i]] == -1:
        segTree.update(i, i, 0)
    else:
        segTree.update(i, lastSeen[arr[i]], i-lastSeen[arr[i]])
    lastSeen[arr[i]] = i

print("Segment tree built")
print(segTree.tree)
for i in range(queries):
    left, right = map(int, input().split())
    left -= 1
    right -= 1
    if left == right:
        print(0)
        continue
    result = segTree.query(left, right+1)
    bestScore = result.getBestScore(left)
    print(bestScore)