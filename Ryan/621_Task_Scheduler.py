# Solution 1 - Greedy
# Time: O(task)
# Space: O(1), since we only have at most 26 tasks
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        dic = collections.defaultdict(int)
        for task in tasks:
            dic[task] +=1
        
        fre = [x for x in dic.values()]
        fre.sort() # constant time since we only have at most 26 tasks
        
        fre_max = fre.pop()
        idle = (fre_max-1)*n
        
        for f in fre:
            idle -= min(f, fre_max-1)
        idle = max(0, idle)
        
        return len(tasks)+idle

# solution 2 - math
# Time: O(task)
# Space: O(1)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        dic = collections.defaultdict(int)
        for task in tasks:
            dic[task]+=1

        dic_val = list(dic.values())
        
        fre_max = max(dic_val)
        max_fre_number = dic_val.count(fre_max)

        return max(len(tasks), (n+1)*(fre_max-1)+max_fre_number)