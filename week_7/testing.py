import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    students = []
    for _ in range(n):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask = (mask << 1) | (1 if c == 'T' else 0)
        students.append(mask)
    
    max_min = 0
    # Iterate through all possible keys
    for key in range(0, 1 << m):
        current_max_hd = 0
        threshold = m - (max_min + 1)
        for student in students:
            hd : int = (key ^ student).bit_count()
            if hd > current_max_hd:
                current_max_hd = hd
                if current_max_hd > threshold:
                    break  # No need to check further students
        # Update max_min if current key gives a better min score
        current_min = m - current_max_hd
        if current_min > max_min:
            max_min = current_min
            if max_min == m:  # Early exit if perfect score found
                break
    print(max_min)

if __name__ == "__main__":
    main()