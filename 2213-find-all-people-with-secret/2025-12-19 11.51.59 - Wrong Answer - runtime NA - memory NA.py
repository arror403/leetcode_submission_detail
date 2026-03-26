class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        s=set([firstPerson,0])
        t=inf

        for a,b,c in meetings:
            if a==firstPerson or b==firstPerson:
                t=min(t,c)

        meetings.sort(key=lambda x:x[2])
        # print(t)
        for a,b,c in meetings:
            if c<t: 
                continue
            if a in s or b in s:
                s.add(a)
                s.add(b)


        return list(s)