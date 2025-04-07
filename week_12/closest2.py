def solve():
    print("Solving")
    import sys,sys
    data = sys.stdin.buffer.read().split()
    # fast I/O: first two numbers: n and m
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    print("GOT N AND M")
    # read array (0-indexed)
    arr = [int(next(it)) for _ in range(n)]
    
    # read queries: store as (r, l, idx) and convert l, r to 0-indexed.
    queries = []
    for idx in range(m):
        l = int(next(it)) - 1
        r = int(next(it)) - 1
        queries.append((r, l, idx))
    queries.sort()  # sort by r
    
    INF = 10**9  # sufficiently large
    # Build an iterative segment tree for point updates and range min queries.
    size = 1
    while size < n:
        size *= 2
    seg = [INF] * (2 * size)
    
    # function to update position pos (0-indexed) with value val in segtree.
    def update(pos, val):
        pos += size
        seg[pos] = val
        pos //= 2
        while pos:
            seg[pos] = seg[2 * pos] if seg[2 * pos] < seg[2 * pos + 1] else seg[2 * pos + 1]
            pos //= 2

    # function to query minimum value in interval [l, r] (0-indexed, inclusive).
    def query(l, r):
        # we query over [l, r+1) in the iterative segtree.
        res = INF
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                if seg[l] < res:
                    res = seg[l]
                l += 1
            if r & 1:
                r -= 1
                if seg[r] < res:
                    res = seg[r]
            l //= 2
            r //= 2
        return res

    # last occurrence dictionary for each value.
    last_occ = {}
    ans = [-1] * m
    q_ptr = 0  # pointer to current query (sorted by r)
    
    # Process the array from left to right.
    for i in range(n):
        a_val = arr[i]
        if a_val in last_occ:
            prev = last_occ[a_val]
            dist = i - prev
            # update segment tree at the position where a_val was last seen
            update(prev, dist)
        last_occ[a_val] = i

        # Process all queries with right endpoint equal to i.
        while q_ptr < m and queries[q_ptr][0] == i:
            r, l, idx = queries[q_ptr]
            res = query(l, r)
            if res == INF:
                ans[idx] = -1
            else:
                ans[idx] = res
            q_ptr += 1

    # Print the answers
    sys.stdout.write("\n".join(map(str, ans)))
    
if __name__ == '__main__':
    solve()
