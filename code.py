def insertion_sort(values):
    m = len(values)
    for i in range(1, m):
        x = values[i]
        j = i - 1
        while j >= 0 and values[j] > x:
            values[j + 1] = values[j]
            # print(values,f" {j}   {i}   {x}")
            j -= 1
        values[j + 1] = x

        
    return values

print(insertion_sort([67, 34, 90, 12, 56, 83, 11, 3]))
