# solution 1 - one pass & hash map
# Time: O(n)
# Space: O(1)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        Count = collections.Counter(secret)  # Space = O(1), since we have at most 10 digits
        
        for idx, g in enumerate(guess):
            s = secret[idx]
            if s == g:
                A+=1
                if Count[s] > 0:
                    Count[s]-=1
                else:
                    B-=1
            elif g in Count and Count[g]>0:
                B+=1
                Count[g]-=1
        return "{}A{}B".format(A,B)

# solution 2 - one pass & balance hashmap
# Time:O(n)
# Space:O(1)
class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		balance = collections.defaultdict(int) # Notice: we use defaultdict but not Counter
		A=B=0

		for idx, g in enumerate(guess):
			s = secret[idx]
			if s==g:
				A+=1
			else:
				B+= int(balance[s]<0) + int(balance[g]>0)
				balance[s]+=1
				balance[g]-=1
		return "{}A{}B".format(A,B)