class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        w=[]
        messages=[i.split() for i in messages]
        for i in range(len(senders)):
            tmp=[senders[i],len(messages[i])]
            w.append(tmp)

        for i in range(len(w)):
            for j in range(i+1,len(w)):
                if w[i][0]==w[j][0]:
                    w[i][1]+=w[j][1]

        w.sort(key=lambda row: (row[1],row[0]), reverse=True)  
        
        return w[0][0]