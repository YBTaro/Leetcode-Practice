# solution 1 - hashmap and heap
# Time: O(nlogn)
# Space: O(n) for hashmap and heap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = collections.defaultdict(int)
        heap = []
        
        for word in words:
            dic[word]-=1
            heapq.heappush(heap, (dic[word], word))
        
        ans = []
        i = 0
        while i!=k:
            _, w = heapq.heappop(heap)
            if dic[w] !=0:
                ans.append(w)
                dic[w]=0
                i+=1
            else:
                continue
        return ans
            
# solution 2 - sort (much faster)
# Time: O(nlong)
# Space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        c = Counter(words)
        return sorted(c, key=lambda x:(-c[x], x))[:k]
        #faster than return sorted(c.keys(), key=lambda x:(-c[x],x))[:k]