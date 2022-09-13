class Re():
    def __init__(self,n):
        self.n=n
    def Reverse_seq(self):
        con = {'A':'T', 'a':'t', 'T':'A', 't':'a', 'C':'G', 'c':'g', 'G':'C', 'g':'c'}
        result = ''.join(con[s] for s in reversed(self))
        print(result)
           
