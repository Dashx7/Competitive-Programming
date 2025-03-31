max_num = 1_001
guess_num = max_num // 2
min_num = 1

#Binary search
print(guess_num, flush=True)
for i in range(10):        
    response = input().strip()
    if response == "lower":
        max_num = guess_num
        guess_num = (max_num + min_num) // 2
    elif response == "higher":
        min_num = guess_num
        guess_num = (max_num + min_num) // 2
    elif response == "correct":
        exit() # Finished
    print(guess_num, flush=True)