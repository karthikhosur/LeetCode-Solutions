class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        s1=set(nums1)
        s2=set(nums2)
        for s in s1:
            if s in s2:
                arr.append(s)
        return arr

        