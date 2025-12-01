def median_of_medians(arr, k):
    n = len(arr)
    if n == 0:
        raise ValueError("Array is empty.")
    if n <= 5:
        return sorted(arr)[k]

    # Step 1: Split arr into groups of 5 and take medians
    groups = [arr[i:i+5] for i in range(0, n, 5)]
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Step 2: Find pivot as median of medians
    pivot = median_of_medians(medians, len(medians)//2)

    # Step 3: Partition
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]

    # Step 4: Recurse into correct partition
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))
