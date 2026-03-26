class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        w=[]
        messages=[i.split() for i in messages]
        for i in range(len(senders)):
            tmp=[senders[i],len(messages[i])]
            w.append(tmp)

        names = collections.defaultdict(list)
        for i,j in w: names[i].append(j)

        w.sort(key=lambda row: (row[1],row[0]), reverse=True)  
        
        return w[0][0]