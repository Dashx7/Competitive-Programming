max_consumption = 1_000_001
guess_consumption = max_consumption // 2
min_consumption = 0

num = int(input()) # just to get the first number, 84?
print(guess_consumption, flush=True)

#Binary search

for i in range(2,84):        
    response = input().strip()
    # print("response", response, flush=True)

    if response == "less":
        max_consumption = guess_consumption
        guess_consumption = (max_consumption + min_consumption) // 2
    elif response == "more":
        min_consumption = guess_consumption
        guess_consumption = (max_consumption + min_consumption) // 2
    elif response == "exact":
        exit() # Finished
    print(guess_consumption*i, flush=True)

