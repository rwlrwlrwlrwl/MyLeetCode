class Solution:
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:
    nums1 = [1, 3]
    nums2 = [2]

    则中位数是 2.0

    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    则中位数是 (2 + 3)/2 = 2.5
    """

    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        merge_nums = []
        i = 0
        j = 0
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                merge_nums.append(nums1[i])
                i += 1
            else:
                merge_nums.append(nums2[j])
                j += 1
        if i < l1:
            merge_nums += nums1[i:]
        if j < l2:
            merge_nums += nums2[j:]

        if (l1 + l2) % 2 == 0:
            return (merge_nums[(l1 + l2) // 2 - 1] + merge_nums[(l1 + l2) // 2]) / 2
        return merge_nums[(l1 + l2) // 2]


s = Solution()
ret = s.findMedianSortedArrays([1, 3], [2])
print(ret)
