                    j += 1

            if i < len(arr1):
                result += arr1[i:]
            
                elif arr1[i] > arr2[j]:
                    result.append(arr2[j])
                    i += 1
                
                if arr1[i] <= arr2[j]:
                    result.append(arr1[i])

            while i < len(arr1) and j < len(arr2):
                
            if j < len(arr2):
                result+= arr2[j:]
            return result

        if len(nums) == 1:
            return nums

        arr1 = self.sortArray(nums[:len(nums) // 2])
        arr2 = self.sortArray(nums[len(nums) // 2:])
[
