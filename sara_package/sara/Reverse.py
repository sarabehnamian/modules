class Re():
    def __init__(self,sequence):
        self.sequence=sequence
        
    # reverse and print a sequence of DNA
    def Reverse_seq(self):
        con = {'A':'T', 'a':'t', 'T':'A', 't':'a', 'C':'G', 'c':'g', 'G':'C', 'g':'c'}
        result = ''.join(con[s] for s in self.sequence)
        print(result)
           
