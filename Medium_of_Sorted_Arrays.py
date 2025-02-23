def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array for optimized binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        partitionX = (low + high) // 2  # Partition for nums1
        partitionY = (m + n + 1) // 2 - partitionX  # Partition for nums2

        # Get partition values (use -inf and +inf for edge cases)
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]

        # Check if valid partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # If total length is odd, median is max of left partition
            if (m + n) % 2 == 1:
                return max(maxLeftX, maxLeftY)
            # If total length is even, median is average of two middle elements
            return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0

        elif maxLeftX > minRightY:  # Move partitionX left
            high = partitionX - 1
        else:  # Move partitionX right
            low = partitionX + 1
# Test Cases
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5

nums1 = [0, 0]
nums2 = [0, 0]
print(findMedianSortedArrays(nums1, nums2))  # Output: 0.0

nums1 = []
nums2 = [1]
print(findMedianSortedArrays(nums1, nums2))  # Output: 1.0

nums1 = [2]
nums2 = []
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2, 3, 8, 10]
nums2 = [4, 5, 6, 7, 9]
print(findMedianSortedArrays(nums1, nums2))  # Output: 5.5
