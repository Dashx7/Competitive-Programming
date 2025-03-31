n = int(input())

base1 = "A" # -> AAA or ABBA, can't be AA
base2 = "BB" # -> fine to stick wherever, BBBB is accepted
base2A = "AA"

if n == 1 or n == 2:
    print(1)

# 3 A -> only 2s, BB or AA next to it, If 2B sandwhiched, then A can be added with others
# A has 0 A slots, 2 (2) slots
# BB has 2 A slots on edges, 2 (2) slots as everything
# Adding BB gives 1 more (2) slot, but if next to BB 1 more (A) slot
# Adding 