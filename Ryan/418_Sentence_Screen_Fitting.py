# solution 1 - brute force - time limit exceed
# Time: O(r*c)
# Space: O(1)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ans = 0
        wordidx = 0
        for _ in range(rows):
            c = 0
            while cols - c - len(sentence[wordidx]) >= 0:
                c += (len(sentence[wordidx])+1)
                wordidx+=1
                if wordidx == len(sentence):
                    ans+=1
                    wordidx = 0
        return ans

# solution 2 - DP
# Time: O(r+n*c), where n is the number of word
# Space: O(n)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ans = 0
        dp = {}
        r, startidx = 0, 0
        
        while r < rows:
            c = 0
            if startidx not in dp:
                finish = 0
                nowidx = startidx
                while cols - c - len(sentence[nowidx]) >= 0:
                    c += len(sentence[nowidx])+1
                    nowidx+=1
                    if nowidx == len(sentence):
                        nowidx = 0
                        finish += 1
                dp[startidx] = [nowidx, finish]
            startidx, finish = dp[startidx]
            ans+=finish
            r+=1
        return ans

# solution 2 - DP - improve by me!!
# Time: O(r+n*c), where n is the number of word
# Space: O(n)
class Solution:
	def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
	    ans = 0 
	    dp = {}  
		# dp[i] = [j, finish]:  
		#    When a row start from the word with index i, we will repeat the whole sentence in 'finish' times, 
		#    and next row will start from the word with index j
			
	    r, startidx = 0, 0

	    total_len = sum([len(s) for s in sentence])+len(sentence)  # to speed up dp building
	    
	    while r < rows:
	        c = 0
	        if startidx not in dp:
	            finish = 0   # repeat time
	            nowidx = startidx    # remain startidx for the key of dp table
				
				# input as many as possible sentence if there is enough space in this row
	            if cols / total_len > 1:   
	            	finish += cols//total_len
	            	c += total_len*finish
					
				# input word by word into this row
	            while cols - c - len(sentence[nowidx]) >= 0:
	                c += len(sentence[nowidx])+1
	                nowidx+=1
	                if nowidx == len(sentence):
	                    nowidx = 0
	                    finish += 1
				# fill up dp table
	            dp[startidx] = [nowidx, finish]
			
	        startidx, finish = dp[startidx]
	        ans+=finish
	        r+=1
	    return ans
                    

