class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        relation = {}
        st = []
        for i in range(len(nums2)):
            while(len(st) != 0 and st[-1] < nums2[i]):
                relation[st[-1]] = nums2[i]
                st.pop(-1)
            st.append(nums2[i])
        
        res = []
        for i in nums1:
            if(i in relation):
                res.append(relation[i])
            else:
                res.append(-1)
            
        return res