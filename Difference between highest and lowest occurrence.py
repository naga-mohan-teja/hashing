    def findDiff(self, a, n):
        #Code here
        d={}
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
        
        # dd=[k for k,v in sorted(d.items(),key=lambda item: item[0] )]
        maxi=max(d.values())
        mini=min(d.values())
        return maxi - mini
