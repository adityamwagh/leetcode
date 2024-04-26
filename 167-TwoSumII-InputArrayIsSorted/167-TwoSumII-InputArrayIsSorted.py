                elif array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            # -1 if not found
            return -1
        
        for i, num in enumerate(numbers):
                tmp = numbers[i+1:]
                j = search(tmp, target - num)
                    return mid
                if array[mid] == target:
                mid = (left + right) // 2
            while left <= right:
                if j != -1:
                    return [i + 1, i + j + 2]
[
