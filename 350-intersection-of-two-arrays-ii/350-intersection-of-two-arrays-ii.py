class Solution(object):
    def intersect(self, nums1, nums2):
        arr=[]
        for s in nums1:
            if s in nums2:
                arr.append(s)
                nums2.pop(nums2.index(s))
        return arr
      