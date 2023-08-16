# Solution 1 : Binary search
# Time: O(log(min(m,n)))
# Space: O(1)
#https://youtu.be/q6IEA26hvXc

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    	A, B = nums1, nums2

    	if len(A) > len(B):
    		A, B = B, A

    	total = len(A)+len(B)
    	half = total//2

    	l,r = 0, len(A)-1
    	while True:
    		i = (l+r)//2         # A's middle index
    		j = half - (i+1) -1  # B's middle index

    		AleftMax = A[i] if i >= 0 else float("-infinity")
    		ArightMin= A[i+1] if (i+1) < len(A) else float("infinity")
    		BleftMax = B[j] if j >= 0 else float("-infinity")
    		BrightMin= B[j+1] if (j+1) < len(B) else float("infinity")

    		if AleftMax <= BrightMin and BleftMax <= ArightMin:
    			if total % 2:
    				return min(ArightMin, BrightMin)
    			else:
    				return (max(AleftMax, BleftMax)+min(ArightMin, BrightMin))/2
    		elif AleftMax > BrightMin:
    			r = i-1
    		else:
    			l = i+1



#https://youtu.be/q6IEA26hvXc

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2        
        if len(A) > len(B):
            A, B = B, A # A is shorter than B
        
        l, r = 0, len(A)-1
        
        total_len = len(A) + len(B)
        half = total_len//2
        
        while True:
            i = (l+r)//2
            Bleftnum = half-(i+1) # i+1 means how many element in A's left part, 
            j = Bleftnum -1
            
            Aleftmax = A[i] if i>=0 else float("-infinity")
            Arightmin = A[i+1] if i+1<len(A) else float("infinity")
            Bleftmax = B[j] if j>=0 else float("-infinity")
            Brightmin = B[j+1] if j+1<len(B) else float("infinity")
            
            if Aleftmax <= Brightmin and Bleftmax <= Arightmin:
                if total_len % 2: # odd
                    return min(Brightmin, Arightmin)
                else:
                    return (max(Aleftmax, Bleftmax)+min(Brightmin, Arightmin))/2
            elif Aleftmax > Brightmin:
                r = i-1
            else:   
                l = i+1
            
        