def highest_rank(arr):
    frequency = {}  # Dictionary to store frequency of each number
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    highest_freq = max(frequency.values())  # Find the highest frequency
    
    # Find the number with the highest frequency
    highest_rank_num = max([num for num, freq in frequency.items() if freq == highest_freq])
    
    return highest_rank_num
