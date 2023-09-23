class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        d={}
        c=0
        for i in range(0,len(arr)):
            if k-arr[i] in d:
                c+=d[k-arr[i]]
            if arr[i] not in d :
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        return c
