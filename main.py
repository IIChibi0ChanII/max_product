def max_product(arr):
    if arr is None or len(arr) < 2:
        return None

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return max(max1 * max2, min1 * min2)


arr = [1, 2, 6, 4, 5, 3, 7]
print(max_product(arr))
