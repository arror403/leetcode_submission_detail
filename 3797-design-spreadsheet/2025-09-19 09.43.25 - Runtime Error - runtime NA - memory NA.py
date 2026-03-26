class Spreadsheet:

    def __init__(self, rows: int):
        # self.s=[[0]*26 for _ in range(rows)]
        self.d=defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        # r=int(cell[1:])-1
        # c=ord(cell[0])-65
        # self.s[r][c]=value
        self.d[cell]=value

    def resetCell(self, cell: str) -> None:
        # r=int(cell[1:])-1
        # c=ord(cell[0])-65
        # self.s[r][c]=0
        del self.d[cell]

    def getValue(self, formula: str) -> int:
        a,b=formula[1:].split('+')
        # a=int(a) if a.isnumeric() else self.s[int(a[1:])-1][ord(a[0])-65]
        # b=int(b) if b.isnumeric() else self.s[int(b[1:])-1][ord(b[0])-65]
        a=int(a) if a.isnumeric() else self.d[a]
        b=int(b) if b.isnumeric() else self.d[b]

        return a+b