class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=len(intervals)
        
        i=0
        intervals=sorted(intervals,key=lambda l:l[0], reverse=False)
        st=[intervals[0]]
        print(st)
        
        print(intervals)
        while i<l:
            t=len(st)-1
            if  st[t][1]>=intervals[i][0]:
                if intervals[i][1]>st[t][1]:
                    st[t][1]=intervals[i][1]
                if intervals[i][0]<st[t][0]:
                    st[t][0]=intervals[i][0]
            else:
                st.append(intervals[i])
            i+=1
        return st
    
        