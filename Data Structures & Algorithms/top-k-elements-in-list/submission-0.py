from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        md = dict()
        lst = []
        for i in nums:
            if i not in md.keys():
                md[i]=1
            else:
                md[i]+=1
        mds = dict(sorted(md.items(),key=itemgetter(1),reverse=True))
        for i in mds.keys():
            lst.append(i)
            k-=1
            if k==0:
                return lst
        
