# from collections import defaultdict
# import bisect
# size, queries = map(int, input().split())

# arr = list(map(int, input().split()))

# lastSeen = defaultdict(lambda: -1)
# distances = [0] * size

# for i in range(len(arr)):
#     if lastSeen[arr[i]] == -1:
#         distances[i] = -1
#     else:
#         distances[i] = i-lastSeen[arr[i]]
#     lastSeen[arr[i]] = i

# print(distances)

# for _ in range(queries):
#     left, right = map(int, input().split())
#     pass

# class QueryAnswer:
#     def __init__(self):
#         self.validAnswer = float('inf') # The best valid answer
#         self.fallback = [] # Sorted array of tuples (index, distance)
#     def merge(self, QueryAnswer):
#         self.validAnswer = min(self.validAnswer, QueryAnswer.validAnswer)
#         for fallback in QueryAnswer.fallback:
#             self.addFallback(fallback[1], fallback[0])
#     def setValidAnswer(self, minDistance):
#         self.validAnswer = min(self.validAnswer, minDistance)
#     def addFallback(self, distance, validIndex):
#         if distance >= self.validAnswer:
#             return # Don't add to the fallback if we already have a better valid answer      
#         index = bisect.bisect_left(self.fallback, (validIndex, distance))
#         if index > 0: # Make sure we don't go out of bounds
#             left_tuple = self.fallback[index-1]
#             if left_tuple[1] >= distance:
#                 return # Dont need to insert if its not better
#             else:
#                 bisect.insort(self.fallback, (validIndex, distance))
#                 # Find the position of the inserted value
#                 index = bisect.bisect_left(self.fallback, (validIndex, distance))

#                 # Remove all elements after the inserted value with distance <= the inserted distance
#                 self.fallback = self.fallback[:index + 1] + [
#                     item for item in self.fallback[index + 1:] if item[1] > distance
#                 ]

#     def getBestScore(self, leftIndex):
#         if self.fallback:
#             #Binary search for the best score where the left index >= the index
#             index = bisect.bisect_left(self.fallback, (leftIndex, float('-inf')))
#             if index < len(self.fallback): # Found something valid
#                 return self.fallback[index][1] # Return distance
#         return self.validAnswer if self.validAnswer else -1

# class SegmentTreeModified:

#     def __init__(self, size):
#         self.size = size
#         self.tree = [QueryAnswer() for _ in range(2 * size)]

#     def update(self, pos, distance, validIndex):
#         pos += self.size
#         self.tree[pos].addFallback(distance, validIndex)
#         while pos > 1:
#             pos //= 2
#             self.tree[pos] = QueryAnswer()
#             self.tree[pos].merge(self.tree[2 * pos])
#             self.tree[pos].merge(self.tree[2 * pos + 1])

#     def query(self, left, right):
#         result = QueryAnswer()
#         left += self.size
#         right += self.size
#         while left < right:
#             if left % 2:
#                 result.merge(self.tree[left])
#                 left += 1
#             if right % 2:
#                 right -= 1
#                 result.merge(self.tree[right])
#             left //= 2
#             right //= 2
#         return result
    
