n = int(input()) # 10^6 songs max
songs = list(map(int,input().split()))

good_combinations = 0
bad_combinations = 0
three_count = songs.count(3)
sum = 0

for i, song in enumerate(songs):
    if song == 1:
        bad_combinations += 1
    elif song == 2:
        good_combinations *= 2; good_combinations += bad_combinations
        bad_combinations = 0
        sum += good_combinations * three_count
        sum %= 10**9 + 7
    elif song == 3:
        three_count -= 1
print(sum)