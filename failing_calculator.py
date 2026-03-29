def average_ratios(numbers):
    total = 0
    valid_count = 0
    for num in numbers:
        if num == 0:
            print(f"Warning: skipping zero value to avoid division by zero")
            continue
        total += 100 / num
        valid_count += 1
    if valid_count == 0:
        return 0
    return total / valid_count

print(average_ratios([10, 5, 0]))
