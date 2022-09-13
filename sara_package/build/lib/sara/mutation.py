from random import randint

class Mu():
    def __init__(self,base_seq):
        self.base_seq=base_seq

    def replace_base_randomly_using_names(self):
        """Return a sequence with the base at a randomly selected position of base_seq replaced
        by a base chosen randomly from the three bases that are not at that position"""
        position = randint(0, len(self.base_seq) - 1) # −1 because len is one past end
        base = self.base_seq[position]
        bases = 'TCAG'
        bases.replace(base, '') # replace with empty string!
        newbase = bases[randint(0,2)]
        beginning = self.base_seq[0:position] # up to position
        end = self.base_seq[position+1:] # omitting the base at position
        return beginning + newbase + end






