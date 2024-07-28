def bubble_sort(nums):
    n = 0
    for _ in nums:
        n += 1

    # Bubble Sort algorithm
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            j += 1
        i += 1

    return nums




def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0

        # Manually calculating the lengths of left and right arrays
        len_left = len_right = 0
        for _ in left:
            len_left += 1
        for _ in right:
            len_right += 1

        while i < len_left and j < len_right:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len_left:
            result.append(left[i])
            i += 1

        while j < len_right:
            result.append(right[j])
            j += 1

        return result

    # Manually calculating the length of the array
    n = 0
    for _ in arr:
        n += 1

    if n > 1:
        mid = n // 2

        # Dividing the array manually
        left = []
        right = []
        i = 0
        for item in arr:
            if i < mid:
                left.append(item)
            else:
                right.append(item)
            i += 1

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)
    else:
        return arr


### There was no way I could optimize the bubble sort algorithm to beat the O(n*n), it requires a loop in a loop to sort that way and will automatically lean to worst case scenario of n times n
### every bubble sort attempt caused it to fail test case ten, with a large array being passed it pushed a time exceeded warning that I was never able to escape.
### Merge sort with a complexity of n log n, still optimized and not using any built in methods is a long line of logic, so the processing time is high, and it isnt efficient. But it did address the sort without timeout.

